#!/opt/wgen-3p/python26/bin/python

import os
import json
from optparse import OptionParser
from collections import defaultdict

INST_TYPE_FROM_CODE      = {1 : "school",                2 : "district",          3 : "muni"}
ENROLLMENT_ROLE_FROM_SID = {0 : "system-access",         1 : "full-access",       2 : "standard-access"}
ITEM_ROLE_FROM_SID       = {1 : "item-non-manager",      2 : "item-manager"}
STANDARDS_ROLE_FROM_SID  = {0 : "standards-non-manager", 1 : "standards-manager", 2 : "curriculum-manager"}

class o(object): pass
maps, sources = o(), o()

def buildSourcesAndMaps():

  def slurp(jsonFile):
    jsonString = "".join([line.split("//")[0] # ignore comments in json file
      for line in open(os.getenv("COMMON_HOME") + "/src/main/resources/demo/" + jsonFile, "r")])
    try:
      return json.loads(jsonString)
    except ValueError, e:
      errorChar = int(str(e)[(str(e).find("char") + 5):-1])
      print "JSON-parsing error in %s from here (probably a stray comma preceding this line): %s" % (jsonFile, jsonString[errorChar:])
      exit(1)

  # slurp sources
  sources.insts = slurp("EXTERNAL_INSTITUTION_EXPORT.json")
  sources.staff = slurp("EXTERNAL_STAFF_EXPORT.json")
  sources.classes = slurp("demo_classes.json")
  sources.students = slurp("demo_students.json")
  sources.courses = slurp("demo_courses.json")

  # build inst map
  maps.instUidToInst = {}
  for inst in sources.insts:
    maps.instUidToInst[inst["institution_uid"]] = inst

  # build inst tree
  class InstTree(object):
    def __init__(self, inst):
      self.inst = inst
      self.childTrees = []
      self.staff = []
      self.isTopLevelAndHasStaffUnderneath = False
    def placeInst(self, parentTree, inst):
      instTree = InstTree(inst)
      parentTree.childTrees.append(instTree)
      maps.instTree.instStringToInstTree[str(inst)] = instTree
      maps.instTree.unmappedInsts.remove(inst)
    def placeInstIfPossible(self, inst):
      if not inst.get("parent"):
        self.placeInst(self, inst)
      else:
        parent = maps.instUidToInst[inst["parent"]["institution_uid"]]
        for childTree in self.childTrees:
          if childTree.inst == parent:
            self.placeInst(childTree, inst)
          else:
            for grandkidTree in childTree.childTrees:
              if grandkidTree.inst == parent:
                self.placeInst(grandkidTree, inst)
    def printRecursive(self, printer):
      printer.write(self.inst["institution_name"])
      if self.staff:
        printer.writeAnywhere(" " * 12 + ("\n" + " " * 12).join(map(getUsernameAndRoles, self.staff)) + "\n")
      printer.indent()
      for childTree in self.childTrees:
        childTree.printRecursive(printer)
      printer.dedent()
  maps.instTree = InstTree(None)
  maps.instTree.instStringToInstTree = {}
  maps.instTree.unmappedInsts = list(sources.insts)
  while maps.instTree.unmappedInsts:
    for inst in maps.instTree.unmappedInsts:
      maps.instTree.placeInstIfPossible(inst)

  # build staff map
  maps.usernameToStaff = {}
  maps.staffUidToStaff = {}
  for staff in sources.staff:
    maps.usernameToStaff[staff["mas"]["username"]] = staff
    maps.staffUidToStaff[staff["napi"]["staff_uid"]] = staff
    homeInst = getHomeInst(staff)
    maps.instTree.instStringToInstTree[str(homeInst)].staff.append(staff)
    maps.instTree.instStringToInstTree[str(getTopLevelInst(homeInst))].isTopLevelAndHasStaffUnderneath = True

  # read demo_classes.json
  maps.instUidToClasseSids = defaultdict(list)
  maps.classeSidToClasse = {}
  maps.classeSidToStaffSid = {}
  for classe in sources.classes["classes"]:
    uid = classe["classe_uid"]
    maps.classeSidToClasse[uid] = classe
    maps.instUidToClasseSids[classe["institution_uid"]].append(uid)
    for staff in classe["staff"]:
      staffUID = staff["staff_uid"]
      if (staff["is_primary"]):
          maps.classeSidToStaffSid[uid] = staffUID

  # read demo_students.json
  maps.classeSidToStudentSids = defaultdict(list)
  for studentClasse in sources.students["student_class_mappings"]:
    maps.classeSidToStudentSids[studentClasse["classe"]].extend(studentClasse["students"])
  maps.studentSidToStudent = {}
  for student in sources.students["students"]:
    maps.studentSidToStudent[student["student_uid"]] = student

  # build course map
  maps.courseUidToCourse = {}
  for course in sources.courses["courses"]:
    maps.courseUidToCourse[course["course_uid"]] = course

def getHomeInst(staff):
  instUids = staff["napi"]["visible_institutions"]
  if len(instUids) > 1:
    raise Exception("not handling SPA")
  return maps.instUidToInst[instUids[0]]

def getTopLevelInst(inst):
  while 1:
    if inst.get("parent"):
      inst = maps.instUidToInst[inst["parent"]["institution_uid"]]
    else:
      return inst

def getAccountStyle(inst):
  return INST_TYPE_FROM_CODE[getTopLevelInst(inst)["institution_type"]]

def getRoles(staff):
  return " ".join([ENROLLMENT_ROLE_FROM_SID[staff["mas"]["role_sid"]],
                   ITEM_ROLE_FROM_SID[staff["mas"]["item_pool_role_sid"]],
                   STANDARDS_ROLE_FROM_SID[staff["mas"]["standards_role_sid"]]])

def getUsernameAndRoles(staff):
  return staff["mas"]["username"] + " (a %s)" % getRoles(staff)

def printDetailedStaffInfo(username, courseFilter=None):

  enrollmentInfoPrinter = IndentPrinter()

  def walkInst(i):

    enrollmentInfoPrinter.write(i["institution_name"])

    classeSids = maps.instUidToClasseSids.get(str(i["institution_uid"]))
    if classeSids:
      enrollmentInfoPrinter.indent()
      for classeSid in classeSids:
        classe = maps.classeSidToClasse[classeSid]
        classeName = classe["name"]
        courseName = maps.courseUidToCourse[classe["course_uid"]]["course_title"] \
            if classe["course_uid"] \
            else "Other"
        gradeName = "Grade %s" % classe["grade_level"]
        primaryTeachers = filter(lambda staff: staff["is_primary"], classe["staff"])
        teacherName = primaryTeachers[0]["first_name"] + " " + primaryTeachers[0]["last_name"] if primaryTeachers else "unknown teacher"
        if courseFilter and courseFilter != courseName:
          continue
        enrollmentInfoPrinter.write("%s (%s, %s) taught by %s" % (classeName, courseName, gradeName, teacherName))
        studentSids = maps.classeSidToStudentSids.get(classeSid)
        if studentSids:
          enrollmentInfoPrinter.indent()
          for studentSid in studentSids:
            student = maps.studentSidToStudent[studentSid]
            enrollmentInfoPrinter.write(student["first_name"] + " " + student["last_name"])
            students.add(student["student_uid"])
          enrollmentInfoPrinter.dedent()
      enrollmentInfoPrinter.dedent()

    children = i.get("children")
    if children:
      enrollmentInfoPrinter.indent()
      for child in children:
        walkInst(maps.instUidToInst[child["institution_uid"]])
      enrollmentInfoPrinter.dedent()

  staff = maps.usernameToStaff[username]
  homeInst = getHomeInst(staff)
  homeInstLevel = INST_TYPE_FROM_CODE[homeInst["institution_type"]]
  roles = getRoles(staff)
  accountStyle = getAccountStyle(homeInst)
  homeInstName = homeInst["institution_name"]
  students = set()
  walkInst(homeInst)

  print "%s @ %s is a %s-level %s in a %s-style account (%i students)" % \
    (username, homeInstName, homeInstLevel, roles, accountStyle, len(students))
  print enrollmentInfoPrinter.text

def printInstTreeWithStaffInfo():
  printer = IndentPrinter()
  for instTree in maps.instTree.childTrees:
    if instTree.isTopLevelAndHasStaffUnderneath:
      instTree.printRecursive(printer)
  print printer.text

class IndentPrinter(object):
  def __init__(self):
    self.indentation = 0
    self.text = ""
  def write(self, line):
    self.text += " " * self.indentation + line + "\n"
  def writeAnywhere(self, line):
    self.text += line
  def indent(self):
    self.indentation += 2
  def dedent(self):
    self.indentation -= 2

if __name__ == "__main__":

  usage = "usage: %prog [USERNAME] [-c COURSE]..."
  desc = "Examples: %prog (print all demo users) | " \
                 + "%prog demoCA100102_SA (print details for user demoCA100102_SA) | " \
                 + "%prog demoCA100102_SA -c \"Reading Lab\" (print details for all of demoCA100102_SA's Reading Lab classes)"
  parser = OptionParser(usage=usage, description=desc)
  parser.add_option("-c", "--course", dest="courseFilter", default=None, help="course to filter on")
  options, args = parser.parse_args()

  buildSourcesAndMaps()

  if args:
    printDetailedStaffInfo(username = args[0], courseFilter = options.courseFilter)
  else:
    printInstTreeWithStaffInfo()
