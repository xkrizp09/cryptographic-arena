#Importing algorithm AES and Counter mode from Crypto library.
from Crypto.Cipher import AES
from Crypto.Util import Counter
#Imports the os module to use the os.urandom() function, which generates the required bytes.
import os

#Generates a 128-bit random key used to encrypt and decrypt messages.
KEY = os.urandom(16)

#Defines an encrypt(plaintext) function that takes a plaintext byte string as input, encrypts it using the AES algorithm in CTR mode with a random key, and returns the hexadecimal representation of the encrypted message. To initialize the algorithm, the function Counter.new(128) is used, which creates a counter with a width of 128 bits.
def encrypt(plaintext):
    cipher = AES.new(KEY, AES.MODE_CTR, counter=Counter.new(128))
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext.hex()

#Defines a test string "test" that calls the encrypt function with this test string as input and outputs the ciphertext as a hexadecimal representation.    
test = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."
print(encrypt(test))   

#It opens the flag.txt file to read the binary contents, reads the contents of the file into the flag variable, and removes whitespace at the beginning and end of the string using the strip() method.
with open('flag.txt', 'rb') as f:
    flag = f.read().strip()
    print(encrypt(flag)) #It calls the encrypt function with the contents of the flag.txt file as input and outputs the encrypted text as a hexadecimal representation.
