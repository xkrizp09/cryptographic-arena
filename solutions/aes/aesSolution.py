#Imports the binascii module and the xor function from the operator module. The binascii function contains functions to convert strings to and from various formats, including hexadecimal representation.
import binascii
from operator import xor

#Opens the output2.txt file for reading, reads the first and second line of the file and converts the hexadecimal representation to a bytearray.
with open("output2.txt") as h:
    encrypted_test = bytearray.fromhex(h.readline().strip())
    encrypted_flag = bytearray.fromhex(h.readline().strip())
    
#Creates a bytearray named blob as the result of the XOR operation between encrypted_test and encrypted_flag.
blob = bytearray(a ^ b for a, b in zip(encrypted_test, encrypted_flag))

test = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."

#Creates a bytearray named "flag" as the result of an XOR operation between the blob and the first len(encrypted_flag) bytes of the test string.
flag = bytearray(a ^ b for a, b in zip(blob, test[: len(encrypted_flag)]))
print(f"{flag=}")
