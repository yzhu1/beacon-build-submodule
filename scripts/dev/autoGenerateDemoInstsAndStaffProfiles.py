'''Autogenerates 

      src/main/resources/DemoInstitutions.txt,
      src/main/resources/DemoAccounts.txt and 
      src/main/resources/DemoStaffProfiles.txt.

Creates five users per state, e.g.:
    demoPA - full access, item access, default standards access 
    demoPA2 - full access, item access, default standards access
    demoPA_SM - full access, item access, standards manager
    demoPA_CM - full access, item access, curriculum manager
    demoPA_IM - full access, item manager, default standards access

along with demo1 and demo2, our original California users.

See http://wiki.wgenhq.net/wiki/index.php/3-12_Platform/Demo_Users.'''

import os
import sys
import json
import itertools

'''[
    {"institution_type":1,
     "institution_name":"Quihuiz Anon Inst",
     "address":{"state":"TX","country":"United States","city":"El Paso"},
     "institution_uid":"10057354",
     "current":{"appconfig":{},"school_year":2010},
     "parent":{"institution_type":2,"institution_name":"Longus Anon Inst","institution_uid":"10026562"},
     "account":{"account_uid":"10026564","account_name":"Longval AnonAcName"},
     "applications":[],
     "policies":{"modify_classes":"0","transferred_student_data":"0","data_sharing":"1","historical_data_access":"1"},
     "primary_id":{"Anon Id Config 39-1":null},
     "contacts":{"technical":{"name":{"last":"Adcox","first":"Anna"}},"administrative":{"name":{"last":"Adcock","first":"Ann"}}}
    }
   ]
'''

instUidGenerator = itertools.count(100000)

def newInstObject(stateCode, accountUid):
    return {
         "address"   : {"city" : "Philly", "country" : "United States", "postal_code" : "19105", "state" : stateCode, "street" : ["1000 Shareville Lane"]},
         "institution_name" : "%s District" % stateCode,
         "institution_type" : 1,
         "institution_uid"  : instUidGenerator.next(),
         "current" : {"school_year":2011},
            }

def newAccountJSON(stateCode, accountUid, inst):
    return newAccountJSONWithInstId(stateCode, accountUid, inst["institution_uid"])

def newAccountJSONWithInstId(stateCode, accountUid, instId):
    return json.dumps(
           {"account"   : {"account_name" : "%s Account %s" % (stateCode, accountUid), "account_uid" : accountUid},
            "institution_uid"  : instId,
           })
    
#added by jeremy joyce?
def newInstPCObject(stateCode, instUid, parentInst, childInstIds):

    return {
         "address"   : {"city" : "NYC", "country" : "United States", "postal_code" : "10001", "state" : stateCode, "street" : ["1234 Broadway"]},
         "institution_name" : "%s District" % stateCode,
         "institution_type" : 1,
         "institution_uid"  : instUidGenerator.next(),
         "current" : {"school_year":2011},
         "parent"  : parentInst,

            }

#definitely added by Jeremy Joyce
def newNamedInstCObject(stateCode, accountUid, instUid, instName, instType, childInst):

    return {
         "address"   : {"city" : "NYC", "country" : "United States", "postal_code" : "10001", "state" : stateCode, "street" : ["1234 Broadway"]},
         "institution_name" : instName,
         "institution_type" : instType,
         "institution_uid"  : instUid,
         "current" : {"school_year":2011},
         "children" : [ childInst , ],
            }
#definitely added by Jeremy Joyce
def newNamedInstPObject(stateCode, accountUid, instUid, instName, instType, parentInst):

    return {
         "address"   : {"city" : "NYC", "country" : "United States", "postal_code" : "10001", "state" : stateCode, "street" : ["1234 Broadway"]},
         "institution_name" : instName,
         "institution_type" : instType,
         "institution_uid"  : instUid,
         "current" : {"school_year":2011},
         "parent"  : parentInst,
            }

#definitely added by Jeremy Joyce
def newNamedInstPCObject(stateCode, accountUid, instUid, instName, instType, parentInst, childInst):

    return {
         "address"   : {"city" : "NYC", "country" : "United States", "postal_code" : "10001", "state" : stateCode, "street" : ["1234 Broadway"]},
         "institution_name" : instName,
         "institution_type" : instType,
         "institution_uid"  : instUid,
         "current" : {"school_year":2011},
         "parent"  : parentInst,
         "children" : [ childInst , ],
            }
    
#added by jeremy joyce?
def newParentChild(iD, name, type):
    return {"institution_uid"  :   iD,
            "institution_name"  :   name,
            "institution_type"  :   type,
            }

staffUidGenerator = itertools.count(0)

def newStaffJSON(stateCode, inst, userPerStateSuffix, role_sid, item_pool_role_sid, standards_role_sid):
    staff_uid = staffUidGenerator.next()
    username = "demo%s%s" % (stateCode, userPerStateSuffix)
    email = "test@domain.org"
    firstname = "Al" + stateCode
    lastname = "User%s" % userPerStateSuffix
    return json.dumps(
        {"mas"        : newStaffMASDict(staff_uid, username, email, firstname, lastname, role_sid, item_pool_role_sid, standards_role_sid),
         "napi"       : newStaffNAPIdict(inst, staff_uid, username, email, firstname, lastname),
         })

def newNamedStaffJSON(stateCode, inst, role_sid, item_pool_role_sid, standards_role_sid, firstName, lastName, userName):
    staff_uid = staffUidGenerator.next()
    username = userName
    email = "test@domain.org"
    firstname = firstName
    lastname = lastName
    return json.dumps(
        {"mas"        : newStaffMASDict(staff_uid, username, email, firstname, lastname, role_sid, item_pool_role_sid, standards_role_sid),
         "napi"       : newStaffNAPIdict(inst, staff_uid, username, email, firstname, lastname),
         })

def newStaffMASDict(staff_uid, username, email, firstname, lastname, role_sid, item_pool_role_sid, standards_role_sid):
    return {
        "app_sids": "7,28",
        "auth_token": "xxx",
        "email": email,
        "first_name": lastname,
        "inst_sid": 2000051944,
        "is_email_verified": 1,
        "is_password_temp": 0,
        "last_name": lastname,
        "program_sids": None,
        "sid": staff_uid,
        "role_sid": role_sid,
        "item_pool_role_sid": item_pool_role_sid,
        "standards_role_sid": standards_role_sid,
        "username": username
        }
    
def newStaffNAPIdict(inst, staff_uid, username, email, firstname, lastname):
    return {
         "staff_uid"  : staff_uid,
         "name"       : {"first" : firstname, "last" : lastname},
         "handle"     : username,
         "email"      : {"address" : email, "verified" : "true"},
         "roles"      : {"sujet_role" : 1},
         "primary_id" : {"Staff Id" : "abcde"},
         "other_ids"  : {"District Id" : "aaaaa", "State Id" : "00000"},
         "current"    : { "institutions" : [{"assignment_uid" : "0", "institution_uid" : inst["institution_uid"], "institution_name" : inst["institution_name"], "institution_type" : inst["institution_type"], "school_year" : "2010"}]},
         "visible_institutions" : [ inst["institution_uid"] ],
         }

def joinedJSON(jsons):
    return "[ // Don't edit me by hand!  I was auto-generated by " \
           + sys.argv[0] \
           + ".  " \
           + "See http://wiki.wgenhq.net/wiki/index.php/3-12_Platform/Demo_Users." \
           + "\n" \
           + ",\n".join(jsons) \
           + "]"

def fullPathTo(filename):
    return os.environ["COMMON_HOME"] + "/src/main/resources/demo/" + filename
    
class fixtureDataObject(object): 
    def __init__(self, attribute_dict):
        self.attribute_dict = attribute_dict

    def get_attribute_json(self):
        return(json.dumps(self.attribute_dict))

class fixtureInstObject(fixtureDataObject):
    def __init__(self, stateCode, accountUid, instUid, instType):
        institution_type_dict = { 1 : 'School', 
                           2 : 'District',
                           3 : 'Municipality' }

        institution_type_name = institution_type_dict[instType]

        self.attribute_dict = {
         "address"   : {"city" : "Philly", "country" : "United States", "postal_code" : "19105", "state" : stateCode, "street" : ["1000 Shareville Lane"]},
         "institution_name" : "%s %s %s" % (stateCode, institution_type_name, instUid),
         "institution_type" : instType,
         "institution_uid"  : instUid,
         "current" : {"school_year":2011},
            }

class fixtureInstHierarchy(object):
    def __init__(self, state_code, account_uid, number_of_children, top_institution_type):
        self.state_code = state_code
        self.account_uid = account_uid
        self.number_of_children = number_of_children
        self.top_institution_type = top_institution_type
        self.top_level_institution_uid = None
        self.inst_dict = {}

    def createInstObject(self, institution_uid, institution_type):
        inst = fixtureInstObject(self.state_code, self.account_uid, institution_uid, institution_type)
        self.inst_dict[institution_uid] = inst

    def createNamedInstObject(self, institution_uid, institution_type, institution_name):
        inst = fixtureNamesInstObject(self.state_code, self.account_uid, institution_uid, institution_type, institution_name)
        self.inst_dict[institution_uid] = inst

    def createTopLevelInst(self):
        institution_uid = instUidGenerator.next()
        self.createInstObject(institution_uid, self.top_institution_type)
        self.top_level_institution_uid = institution_uid

    def _get_parent_child_dict(self, institution_uid):
        inst = self.inst_dict[institution_uid]
        return_dictionary = { "institution_name" : inst.attribute_dict['institution_name'], "institution_type" : inst.attribute_dict['institution_type'], "institution_uid" : institution_uid }
        return return_dictionary

    def _add_inst_child(self, parent_institution_uid, child_institution_uid):
        parent = self.inst_dict[parent_institution_uid]
        child_values = self._get_parent_child_dict(child_institution_uid) 
    

        if 'children' in parent.attribute_dict:
            parent.attribute_dict['children'].append(child_values)
        else:
            parent.attribute_dict['children'] = [ child_values ]

    def _add_inst_parent(self, parent_institution_uid, child_institution_uid):
        child = self.inst_dict[child_institution_uid]
        parent_value = self._get_parent_child_dict(parent_institution_uid)

        if 'parent' in child.attribute_dict:
            raise Exception('this is crazy.  there should only be one parent')
        else :
            child.attribute_dict['parent'] = parent_value


    def createChildInstObject(self, parent_institution_uid):
        child_institution_uid = institution_uid = instUidGenerator.next()
        parent = self.inst_dict[parent_institution_uid]
        child_institution_type = parent.attribute_dict['institution_type'] - 1
        self.createInstObject(child_institution_uid, child_institution_type)
        self._add_inst_child(parent_institution_uid, child_institution_uid)
        self._add_inst_parent(parent_institution_uid, child_institution_uid)

    def createInstHierarchy(self):
    #TODO remove the ugly double while loop.  
        self.createTopLevelInst()
        level_of_tree = self.top_institution_type
        #inst_dict = self.inst_dict
        institution_uid_list = []
        if level_of_tree >= 2:
            for key in self.inst_dict :
                inst = self.inst_dict[key]
                if inst.attribute_dict["institution_type"] == level_of_tree:
                    institution_uid_list.append(inst.attribute_dict["institution_uid"])    
        level_of_tree -= 1

        for uid in institution_uid_list:
            n = 1
            while n <= self.number_of_children:
                self.createChildInstObject(uid)
                n += 1

        institution_uid_list = []

        if level_of_tree >= 2:

            for key in self.inst_dict :
                inst = self.inst_dict[key]
                if inst.attribute_dict["institution_type"] == level_of_tree:
                    institution_uid_list.append(inst.attribute_dict["institution_uid"])   

        for uid in institution_uid_list:
            n = 1
            while n <= self.number_of_children:
                self.createChildInstObject(uid)
                n += 1
                            

    def get_inst_list(self):
        inst_list = []
        for key in self.inst_dict:
            inst_list.append(self.inst_dict[key])
        return inst_list

def genHillsideElementary(Account_uid, Staff, Insts, Accounts):
    
    #Beginning crazy JJ stuff
    
    inst1 = instUidGenerator.next()
    inst2 = instUidGenerator.next()
    inst3 = instUidGenerator.next()
    
    muniName = "New York Public Schools"
    distName = "Evansville Central School District"
    schoolName = "Hillside Elementary School"
    
    Account_uid += 1
    
    stateCode = "NY"
    muni = newNamedInstCObject(stateCode, Account_uid, inst1, muniName, 3, newParentChild(inst2, distName, 2))
    Insts.append(json.dumps(muni))
    Accounts.append(newAccountJSON(stateCode, Account_uid, muni))
    
    dist = newNamedInstPCObject(stateCode, Account_uid, inst2, distName, 2, newParentChild(inst1, muniName, 3), newParentChild(inst3, schoolName, 1))
    Insts.append(json.dumps(dist))
    Accounts.append(newAccountJSON(stateCode, Account_uid, dist))
    
    school =  newNamedInstPObject(stateCode, Account_uid, inst3, schoolName, 1, newParentChild(inst2, distName, 2))
    Insts.append(json.dumps(school))
    Accounts.append(newAccountJSON(stateCode, Account_uid, school))
                                  
    
    # System Admin Tim Brewster
    Staff.append(newNamedStaffJSON(stateCode, school, 0, 1, 1, "Tim", "Brewster", "tbrewster"))
    
    # System Admin Claire Wilson
    Staff.append(newNamedStaffJSON(stateCode, school, 0, 1, 1, "Claire", "Wilson", "cwilson"))
    
    #end crazy JJ stuff
    
    return Account_uid

def genHierInstsAndUsers(State, Staff, Account_uid, Insts, Accounts):
        # Create new hierarchy-based muni in CA with full compliment of users:
    Account_uid += 1
    num_children = 2
    top_level_hier = 3

    muni = fixtureInstHierarchy(State, Account_uid, num_children, top_level_hier)
    muni.createInstHierarchy()
    muni_list = muni.get_inst_list()
    

    for inst in muni_list:
    #TODO make a function that creates all users

        Insts.append(inst.get_attribute_json())
        

        institution_uid = inst.attribute_dict["institution_uid"]
        state_code = muni.state_code

        Accounts.append(newAccountJSONWithInstId(state_code, Account_uid, institution_uid))

        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s" %institution_uid, 2, 1, 0))
        # Standards Manager
        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_SM" %institution_uid, 2, 1, 1))
        # Another Standards Manager for same account
        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_SM_B" %institution_uid, 2, 1, 1))
        # Curriculum Manager
        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_CM" %institution_uid, 2, 1, 2))
        # Item Manager 
        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_IM"%institution_uid, 2, 2, 0))
        # Full Access
        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_F"%institution_uid, 1, 1, 1))
        # System Admin
        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_SA"%institution_uid, 0, 1, 1))


    # Create new hierarchy-based muni in CA with no users:
    Account_uid += 1
    num_children = 2
    top_level_hier = 3

    muni = fixtureInstHierarchy(State, Account_uid, num_children, top_level_hier)
    muni.createInstHierarchy()
    muni_list = muni.get_inst_list()

   # Create new hierarchy-based district in CA with full compliment of users:
    Account_uid += 1
    num_children = 2
    top_level_hier = 2

    muni = fixtureInstHierarchy(State, Account_uid, num_children, top_level_hier)
    muni.createInstHierarchy()
    muni_list = muni.get_inst_list()
    

    for inst in muni_list:
        Insts.append(inst.get_attribute_json())
        

        institution_uid = inst.attribute_dict["institution_uid"]
        state_code = muni.state_code

        Accounts.append(newAccountJSONWithInstId(state_code, Account_uid, institution_uid))

        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s" %institution_uid, 2, 1, 0))
        # Standards Manager
        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_SM" %institution_uid, 2, 1, 1))
        # Another Standards Manager for same account
        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_SM_B" %institution_uid, 2, 1, 1))
        # Curriculum Manager
        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_CM" %institution_uid, 2, 1, 2))
        # Item Manager 
        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_IM"%institution_uid, 2, 2, 0))
        # Full Access
        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_F"%institution_uid, 1, 1, 1))
        # System Admin
        Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_SA"%institution_uid, 0, 1, 1))

    # Create new hierarchy-based district in CA with no users:
    Account_uid += 1
    num_children = 2
    top_level_hier = 2

    muni = fixtureInstHierarchy(State, Account_uid, num_children, top_level_hier)
    muni.createInstHierarchy()
    muni_list = muni.get_inst_list()
    state_code = muni.state_code

    for inst in muni_list:
        Insts.append(inst.get_attribute_json())
        institution_uid = inst.attribute_dict["institution_uid"]
        Accounts.append(newAccountJSONWithInstId(state_code, Account_uid, institution_uid))

                    
    # Create new hierarchy-based muni in CA with no users in the muni & district level but with users in school:
    Account_uid += 1
    num_children = 2
    top_level_hier = 3

    muni = fixtureInstHierarchy(State, Account_uid, num_children, top_level_hier)
    muni.createInstHierarchy()
    muni_list = muni.get_inst_list()
    
    for inst in muni_list:
        Insts.append(inst.get_attribute_json())
  
        institution_uid = inst.attribute_dict["institution_uid"]
        state_code = muni.state_code

        Accounts.append(newAccountJSONWithInstId(state_code, Account_uid, institution_uid)) 
        
        if "School" in inst.attribute_dict["institution_name"]:
            # System Admin
            Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_SA"%institution_uid, 0, 1, 1))
            Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_SA_B"%institution_uid, 0, 1, 1))
            # Full Access
            Staff.append(newStaffJSON(state_code, inst.attribute_dict, "%s_F"%institution_uid, 1, 1, 1))
    return Account_uid

def autoGenerateDemoInstsAndStaffProfiles():

    institutions = []
    staff = []
    accounts = []
    fallbackInst = "";
    account_uid = 1
    for stateIdx, stateCode in enumerate((
            "AL", "AK", "AZ", "AR", "CA",
            "CO", "CT", "DC", "DE", "FL",
            "GA", "HI", "Id", "IL", "IN",
            "IA", "KS", "KY", "LA", "ME",
            "MD", "MA", "MI", "MN", "MS",
            "MO", "MT", "NE", "NV", "NH",
            "NJ", "NM", "NY", "NC", "ND",
            "OH", "OK", "OR", "PA", "RI",
            "SC", "SD", "TN", "TX", "UT",
            "VT", "VA", "WA", "WV", "WI",
            "WY")):

        newInstData = newInstObject(stateCode, account_uid)
        institutions.append(json.dumps(newInstData))
        accounts.append(newAccountJSON(stateCode, account_uid, newInstData))
        if stateCode == "CA":
            fallbackInst = newInstData
        staff.append(newStaffJSON(stateCode, newInstData, "", 2, 1, 0))
        # Standards Manager
        staff.append(newStaffJSON(stateCode, newInstData, "_SM", 2, 1, 1))
        # Another Standards Manager for same account
        staff.append(newStaffJSON(stateCode, newInstData, "_SM_B", 2, 1, 1))
        # Curriculum Manager
        staff.append(newStaffJSON(stateCode, newInstData, "_CM", 2, 1, 2))
        # Item Manager 
        staff.append(newStaffJSON(stateCode, newInstData, "_IM", 2, 2, 0))
        # Full Access
        staff.append(newStaffJSON(stateCode, newInstData, "_F", 1, 1, 1))
        # System Admin
        staff.append(newStaffJSON(stateCode, newInstData, "_SA", 0, 1, 1))
        account_uid += 1
        
        # Now create another set of users for a new inst account in the same state
        newInstData = newInstObject(stateCode, account_uid)
        institutions.append(json.dumps(newInstData))
        accounts.append(newAccountJSON(stateCode, account_uid, newInstData))
        staff.append(newStaffJSON(stateCode, newInstData, "2", 2, 1, 0))
        # Standards Manager
        staff.append(newStaffJSON(stateCode, newInstData, "2_SM", 2, 1, 1))
        # Curriculum Manager
        staff.append(newStaffJSON(stateCode, newInstData, "2_CM", 2, 1, 2))
        # Item Manager 
        staff.append(newStaffJSON(stateCode, newInstData, "2_IM", 2, 2, 0))
        # System Admin
        staff.append(newStaffJSON(stateCode, newInstData, "2_SA", 0, 1, 1))
        account_uid += 1
    

    # Keep demo1 and demo2 working, make them item & standards managers
    staff.append(newStaffJSON("", fallbackInst, "1", 0, 2, 1))
    staff.append(newStaffJSON("", fallbackInst, "2", 0, 2, 1))

    # Users for each of us
    staff.append(newStaffJSON("", fallbackInst, "Lisa", 0, 1, 0))
    staff.append(newStaffJSON("", fallbackInst, "Mark", 0, 1, 0))
    staff.append(newStaffJSON("", fallbackInst, "John", 0, 1, 0))
    staff.append(newStaffJSON("", fallbackInst, "Catherine", 0, 1, 0))
    staff.append(newStaffJSON("", fallbackInst, "David", 0, 1, 0))
    staff.append(newStaffJSON("", fallbackInst, "Jeremy", 0, 1, 0))
    staff.append(newStaffJSON("", fallbackInst, "Dan", 0, 1, 0))
    staff.append(newStaffJSON("", fallbackInst, "steve", 0, 1, 0))

    ## Continue here
    account_uid = genHierInstsAndUsers("CA", staff, account_uid, institutions, accounts)
    account_uid = genHierInstsAndUsers("NY", staff, account_uid, institutions, accounts)
    ## Up to here    

    account_uid = genHillsideElementary(account_uid, staff, institutions, accounts)


    open(fullPathTo('DemoInstitutions.txt'), 'w').write(joinedJSON(institutions))
    open(fullPathTo('DemoStaffProfiles.txt'), 'w').write(joinedJSON(staff))
    open(fullPathTo('DemoAccounts.txt'), 'w').write(joinedJSON(accounts))

if __name__ == '__main__':

    autoGenerateDemoInstsAndStaffProfiles()
