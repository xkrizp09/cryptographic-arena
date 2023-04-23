#Imports the binascii module and the xor function from the pwn tools. The binascii function contains functions to convert strings to and from various formats, including hexadecimal representation.
import binascii
from pwn import xor

#Opens the output2.txt file for reading, reads the first and second line of the file and convert the hexadecimal-encoded strings to their corresponding bytes representation.
with open("output2.txt") as h:
    encrypted_test = binascii.unhexlify(h.readline().strip())
    encrypted_flag = binascii.unhexlify(h.readline().strip())
    
#Creates an object named blob as the result of the XOR operation between encrypted_test and encrypted_flag.
blob = xor(encrypted_test, encrypted_flag)

test = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."

#Creates an object named "flag" as the result of an XOR operation between the blob and the first len(encrypted_flag) bytes of the test string.
flag = xor(blob, test[: len(encrypted_flag)]) [: len(encrypted_flag)]
FLAG = flag.decode('utf-8')[5:-1]
print(f"FLAG({FLAG})")
