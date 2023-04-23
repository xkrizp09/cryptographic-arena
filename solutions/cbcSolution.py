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
	target_string = "CBC-MAC is really interesting!!!"
	#Create ciphertext from first block of string
	first_slice = target_string[:16]
	MAC_first_slice = bytes.fromhex(cbc.MAC_generation(first_slice))
	#Calculate second part of the tag
	second_slice = strxor(MAC_first_slice,target_string[16:32].encode())
	MAC = cbc.MAC_generation(second_slice)
	#Check if the tag is correct
	cbc.MAC_authentication(MAC)
if __name__ == '__main__':
	exploit()

