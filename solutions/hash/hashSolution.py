import hashlib

#reads passwords from a file and separates them into single list elements
def readPasswords():
    with open("passwords.txt") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines

#creates hashes of the passwords and returns the resulting hashes
def getHashes(passwords):
    result = []
    for i in passwords:
        hash = hashlib.md5(i.encode())
        result.append(hash.hexdigest())
    return result

#finds collision between given list of hashes and found hash we need to find the collision to. Returns index of the collision thus giving us the result
def findCollision(hashes, passhash):
    for i in hashes:
        if(i == passhash):
            return hashes.index(i)
        
passwords = readPasswords()
hashes = getHashes(passwords)

number = findCollision(hashes, "input hash")
print("Password is :" , passwords[number])