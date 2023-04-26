#!/usr/bin/env python3

#The binascii function is used to convert the decoded sequence of bytes into a text string.
import binascii
from pwn import xor

#Opening a file called "output2.txt". The coded text from which the given flag is obtained is stored here.
with open("output2.txt") as h:
#Complete the remaining code here.

#store the content into two binasciiarrays

#create an object blob for XOR operation between these two binasciiarrays

#Define a variable that contains a bytes object for testing.
test = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."

#Create an object as the result of an XOR operation between the blob and the first len(xxx) bytes of the test string.

#The flag listing.

FLAG = flag.decode('utf-8')[5:-1]
print(f"FLAG({FLAG})")
