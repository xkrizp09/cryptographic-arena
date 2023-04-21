from Crypto.Util.number import *
from Crypto.Cipher import AES


AES_key = "a9c3ffe462a9948c3e36b08d83a83e45"
MAC_flag = "b5ee2383ade763c03b5a61b393af868c"

AES_key = bytes.fromhex(AES_key)
iv = "\x00" * 16
BLOCKSIZE = 16

def MAC_generation(plaintext):
	try:
		#Zkontroluje delku velikost vstupu, aby odpovidala nasobkum 16 (velikosti bloku)
		assert len(plaintext) % 16 == 0
		
		#Zabrani uzivateli pouzit cely text
		if plaintext == "CBC-MAC is really interesting!!!":
			print("Takto jednoduche to nebude, zkus to jinak")
			exit()
		
		#Vytvoreni MAC tagu
		obj1 = AES.new(AES_key, AES.MODE_CBC, iv)
		ciphertext = obj1.encrypt(plaintext)
		ciphertext = ciphertext[len(ciphertext) - 16:]

		return ciphertext.hex()
	except:
		print ("Chyba vstupu")

def MAC_authentication(tag):
	#Pokud uzivatel uspesne zvolil postup reseni, ziska flag
	if tag == MAC_flag:
		print ("FLAG{cbc_m4c}")
	else:
		print ("To neni ono, zkus to znovu")
