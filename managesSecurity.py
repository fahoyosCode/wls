groups = []
domainName = 'INVENTORY_WLS'

# Read file whit groups and load to array
def loadArchive(archiveName):
  archivo = open(archiveName, "r")
  for linea in archivo:
    groups.append(linea.rstrip())

## Create groups from array
def createGroups()
  loadArchive('groups.txt')
  for group in groups:
    newGroupName = group
    newGroupDescription = 'WO'
    createGroup(newGroupName, newGroupDescription, true)

## Crate group
def createGroup(newGroupName, newGroupDescription, deleteGroupFirstIfExists):
  try:
    cd('/SecurityConfiguration/'+domainName+'/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator')
    if (cmo.groupExists(newGroupName)):
      if (deleteGroupFirstIfExists):
        print 'Group '+newGroupName+' already exists - removing old group first !'
        cmo.removeGroup(newGroupName)
      else:
        # cannot create !!
        print 'Group '+newGroupName+' already exists - CANNOT create !'
        return
    # create group
    cmo.createGroup(newGroupName, newGroupDescription)

  except:
    dumpStack()

def addUsetToGroup(userName, groupName):
  try:
    cd('/SecurityConfiguration/'+domainName+'/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator')
      # check if user exists
      if (cmo.userExists(userName)==0):
        print 'User '+userName+' does not exist CANNOT add '+userName+' to group '+groupName+' !'
        return
      # check if group exists
      if (cmo.groupExists(groupName)==0):
        print 'Group '+groupName+' does not exist CANNOT add '+userName+' to group '+groupName+' !'
        return
      # check if already member
      if (cmo.isMember(groupName,userName,true)==1):
        print 'User '+userName+' is already member of group '+groupName+' !'
        return
     
      # finally  add user to group
      cmo.addMemberToGroup(groupName, userName)
  except:
    dumpStack()



connect("weblogic", "Welcome1", "t3://localhost:7100")
createGroups()
for group in groups:
  user = 'User1'
  addUsetToGroup(user,group)




