from Crypto.Util.number import *
from Crypto.Cipher import AES


AES_key = "a9c3ffe462a9948c3e36b08d83a83e45"
MAC_flag = "b5ee2383ade763c03b5a61b393af868c"

AES_key = bytes.fromhex(AES_key)
iv = "\x00" * 16
BLOCKSIZE = 16

def MAC_generation(plaintext):
	try:
		#Checks if the input is a multiple of 16
		assert len(plaintext) % 16 == 0
		
		#Forbids user from using whole text
		if plaintext == "CBC-MAC is really interesting!!!":
			print("It's not that easy, try again")
			exit()
		
		#Creating a ciphertext
		obj1 = AES.new(AES_key, AES.MODE_CBC, iv)
		ciphertext = obj1.encrypt(plaintext)
		ciphertext = ciphertext[len(ciphertext) - 16:]

		return ciphertext.hex()
	except:
		print ("Input error")

def MAC_authentication(tag):
	#if user chose the correct approach tag will be displayed
	if tag == MAC_flag:
		print ("FLAG{cbc_m4c}")
	else:
		print ("That's not it, try again")
