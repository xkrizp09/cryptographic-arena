import hashlib

#implement a funtion which will read the password file and will parse the code into sigle list elements.
def readPasswords():
   #todo implement
   return passwords


#creates hashes of the passwords and returns the resulting hashes
def getHashes(passwords):
    result = []
    for i in passwords:
        hash = hashlib.md5(i.encode())
        result.append(hash.hexdigest())
    return result

#implement a function which will find the collision and will return the index of the position where to collision was found
def findCollision(hashes, passhash):
    #todo implement
    return index
        

passwords = readPasswords() #implement
hashes = getHashes(passwords)


number = findCollision(hashes, "input hash")#implement
print("Password is :" , passwords[number])
