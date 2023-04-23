#!/usr/bin/env python3

#It opens the message.txt file for reading and reads the contents of the file and stores it in the contents.
with open("message.txt") as filp:
    contents = filp.read()

#It creates an empty "flag" list and runs a for loop that will step through the contents of the contents variable three characters at a time. Stores a three-character substring in the chunk variable.   
flag = []
for i in range(0, len(contents), 3):
    chunk = contents[i:i+3]
    
#If the length of the string in the chunk is less than 3, it adds spaces to make a string of length 3. Assigns single characters from the chunk string to the variables a, b, and c.
    if len(chunk) < 3:
        chunk += ' ' * (3 - len(chunk))
        
#Adds a new string to the flags list consisting of the third character, the first character, and the second character in sequence. This string is the result of encoding the secret string.
     a, b, c = chunk
    flag.append(c + a + b)
    
#Runs the join method on the "flag" list to create a single string. Splits the string into individual words and assigns the last word to the flag variable and prints the "flag" variable.
flag = "".join(flag).split()[-1]
print(flag)
