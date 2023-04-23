from Crypto.Util.strxor import strxor
import importlib.util
spec = importlib.util.spec_from_file_location("cbc", ".cbc.py")
cbc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cbc)

"""
To communicate with server use the following functions:
	
cbc.MAC_generation(text) - used to cipher block of the message
	
cbc.MAC_authentication(tag) - used for checking if generated tag is correct
	
"""
def exploit():
	#Text we want to create MAC from
	plaintext = "CBC-MAC is really interesting!!!"
	
	#Create ciphertext from first block of string
	
	#Calculate second part of the tag
	
	#Check if the tag is correct
	
if __name__ == '__main__':
	exploit()
