from cbc import *
from Crypto.Util.strxor import strxor

def exploit():
	#Text ke kteremu chceme ziskat MAC
	target_string = "CBC-MAC is really interesting!!!"
	#Rozdeleni stringu na bloky o velikosti 16b a sifrovani
	first_slice = target_string[:16]
	MAC_first_slice = bytes.fromhex(MAC_generation(first_slice))
	#Vypocet druhe poloviny v zavislosti na prvnim sifrovanem bloku pomoci XOR
	second_slice = strxor(MAC_first_slice,target_string[16:32].encode())
	MAC = MAC_generation(second_slice)
	#Overeni vysledneho MAC tagu
	MAC_authentication(MAC)
if __name__ == '__main__':
	exploit()

