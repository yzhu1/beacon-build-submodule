#!/opt/wgen-3p/python26/bin/python
import os
import sys
import datetime
import json
import itertools
import re

# file-access constants:

classesJSONFile = "demo_classes.json"
classesRawFile = "demo_classes_raw.txt"
studentsJSONFile = "demo_students.json"
studentsRawFile = "demo_students_raw.txt"
coursesJSONFile = "demo_courses.json"
staffJSONFile = "EXTERNAL_STAFF_EXPORT.json"
instJSONFile = "EXTERNAL_INSTITUTION_EXPORT.json"

def openResourceFile(basename,mode='r'):
    filename = os.environ["COMMON_HOME"] + "/src/main/resources/demo/" + basename
    return open(filename,mode)

def autoGenNagComment():
    now =  datetime.datetime.now().ctime()
    return "// DO NOT EDIT BY HAND--generated automatically by " + sys.argv[0] + " on " + now 

# hand-rolling outer structure to allow insertion of comments
def writeJSONFile(filename,filedata):
    outfile = openResourceFile(filename,'w')
    nag = autoGenNagComment() + "\n"
    joinstr = "," + nag
    outfile.write( "{\n" + nag  )
    outfile.write( joinstr.join(
        ['"%s": %s' % (k,json.dumps(filedata[k],indent=4)) for k in filedata.keys()]
        ))
    outfile.write("\n" + nag + "}\n")

def readJSONFile(filename):
    infile = openResourceFile(filename)
    nocomment = re.compile("// D.*$")
    stripped_lines = [ nocomment.sub("", line) for line in infile.readlines() ]
    bigstr = "".join(stripped_lines)
    return json.loads(bigstr)

# lookup hashes
class DataLookup:
    _courseDataLookup = None
    _instDataLookup = None
    _staffDataLookup = None
    
    def _loadStaff(self):
        staffJSON = readJSONFile(staffJSONFile)
        self._staffDataLookup = {}
        # this would be one-line dictionary comprehension in Python 3.  *sigh* 
        for row in staffJSON :
            login = str(row["mas"]["username"])
            self._staffDataLookup[login] = row["napi"]
    def _loadCourses(self):
        courseJSON = readJSONFile(coursesJSONFile)
        self._courseDataLookup = {}
        for row in courseJSON["courses"] :
            uid = str(row["course_uid"])
            self._courseDataLookup[uid] = row
    def _loadInsts(self):
        instJSON = readJSONFile(instJSONFile)
        self._instDataLookup = {}
        for row in instJSON:
            uid = str(row["institution_uid"])
            self._instDataLookup[uid] = row

    def getStaff(self,login):
        if None == self._staffDataLookup:
            self._loadStaff()
        return self._staffDataLookup[login]
    def getCourse(self,id):
        if None == self._courseDataLookup:
            self._loadCourses()
        return self._courseDataLookup[str(id)]
    def getInst(self,id):
        if None == self._instDataLookup:
            self._loadInsts()
        return self._instDataLookup[str(id)]

globalDataLookup = DataLookup()

def newStudentObject(sid,first,middle,last,suffix):
    return { "student_uid": "%d" % sid,
             "first_name": first,
             "middle_name": middle,
             "last_name": last,
             "suffix": suffix
             }

def newClasseObject(classId, className, instId, courseUID, gradeLevel, staffUIDs):
    staffObjects = []
    # we could also look up the correct inst/course metadata, if we cared enough
    for uid in staffUIDs:
        fullStaff = globalDataLookup.getStaff(uid)
        staffObjects.append(
            {
            "first_name" : fullStaff["name"]["first"],
            "last_name" : fullStaff["name"]["last"],
            "is_primary": False,
            "staff_uid" : fullStaff["staff_uid"]
            }
            )
    if staffObjects: # first is always primary in our fixtures, if there's any staff at all
        staffObjects[0]["is_primary"] = True

    return {
        "classe_uid": classId, 
        "course_code": None, 
        "course_title": None, 
        "course_uid": courseUID, 
        "grade_level": gradeLevel, 
        "institution_name": "Stella by Starlight", 
        "institution_uid": instId, 
        "is_demo": False, 
        "name": className,
        "primary_id": "1234567", 
        "school_year": 2011, 
        "staff" : staffObjects,
        "subject_area_code": None, 
        "subject_area_name": None
    }

def newClassList(classid, students):
    return {"classe" : "%d"%classid, "students": students}

studentSIDgenerator = itertools.count(1)
classSIDgenerator = itertools.count(1)

def printClasseData():
    datalines = openResourceFile(classesRawFile).readlines();
    datalines.pop(0) # take off header row
    classeobjects = []
    blank = re.compile("^\s*$")
    for inputline in datalines:
        fields = inputline.rstrip().split(",")
        #        print fields
        (classeID,classeName,courseUID,gradeLevel,instUID,teachers) = fields
        if "" == gradeLevel:
            gradeLevel = None
        if "" == courseUID:
            courseUID = None
        if blank.match(teachers):
            teacherUIDs = []
        else:
            teacherUIDs = teachers.split()
        classe = newClasseObject(classeID,classeName,instUID, courseUID, gradeLevel, teacherUIDs)
        classeobjects.append(classe)
    writeJSONFile(classesJSONFile,{"classes":classeobjects})

def printStudentData():
    classconfig = [
            [], [4], [0,1,2,3,4,5], range(6,24), range(24,36),
            range(37,43), range(44,56), range(57,75),
            range(76,88,2) + range(89,95), #the 9th class
            range(90,95) + range(77,89,2), #the 10th class
            range(85,105), #the 11th class
            range(76,106,3), #the 12th class
            range(77,106,5), #the 13th class
            range(107,140,3) + range(160,165),
            range(108,141,3) + range(160,165),
            range(121,140,2) + range(165,175,2),
            range(122,141,2) + range(185,200,3),
            range(130,150) + range(107,113),
            range(151,171,3) + range(109,141,3),
            range(107,140,3),
            range(172,196,2) + range(198,225,5),
            range(173,197,2) + range(199,226,3),
            range(198,225,2) + range(172,196,4),
            range(199,226,2) + range(173,197,4),
            [],[],[],[], # Merge conflict classes: no students listed
            range(200,227,2) + range(174,198,4), #29th class PurpleParrotsEnglishLit
            range(201,228,2) + range(175, 199, 4), #30th class PurpleParrotsHistory
            range(175,200),
            range(200,225),
            range(225,250),
            range(250,275),
            range(275,300),
            range(300,325),
            range(325,350),
            range(350,375),
            range(375,400),
            range(400,405), # 40
        ]
    studentlist = []
    classlist = []

    studentfile =  openResourceFile(studentsRawFile)
    for student_line in studentfile.readlines():
        if student_line.startswith("#"):
            continue
        splitline = student_line.rstrip().split(",",4)
        lname = splitline[0]
        fname = splitline[1]
        mname = splitline[2]
        suffix= splitline[3]
        studentlist.append(newStudentObject(studentSIDgenerator.next(), fname,mname,lname,suffix))

    for classstudents in classconfig:
        classlist.append(
            newClassList(
                classSIDgenerator.next(),
                [studentlist[i]["student_uid"] for i in classstudents])
            )

    studentEnrollmentData = {"students": studentlist, "student_class_mappings": classlist}
    writeJSONFile(studentsJSONFile, studentEnrollmentData)

def printProfiles():
    printStudentData()
    printClasseData()

if __name__ == '__main__':
    printProfiles()
