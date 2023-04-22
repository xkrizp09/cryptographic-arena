#!/usr/bin/env python3

#It opens the message.txt file for reading and reads the contents of the file and stores it in the contents variable.
with open("message.txt") as filp:
    contents = filp.read()

#Complete the remaining part of the code.

#Initialize an empty list to store the results and iterate through the string three characters at a time.
#Get a three-character substring

#Add spaces to make a string of length 3.

#Create a new string by reordering the characters in the chunk and adds it to the "flag" list. The resulting string is the encoded secret.

#run method on the "flag" list to create a single string. Splits the string into individual words and assigns the last word to the flag variable.  

#Prints the flag variable.
print(flag)
