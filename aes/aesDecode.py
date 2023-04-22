#!/usr/bin/env python3

#The binascii function is used to convert the decoded sequence of bytes into a text string.
import binascii
from operator import xor

#Opening a file called "output2.txt". The coded text from which the given flag is obtained is stored here.
with open("output2.txt") as h:
#Complete the remaining code here.

#store the content into two bytearrays

#create blob bytearray for XOR operation between these two bytearrays

test = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."

#Create a bytearray as the result of an XOR operation between the blob and the first len(xxx) bytes of the test string.

#The flag listing.
print(f"{flag=}")
