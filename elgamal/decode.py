#Import the necessary modules
from keyGeneration import p, h, g

#Helper function to decode integer to string
def decode_int_to_str(encoded_int):
    # Convert integer to hex string
    hex_str = hex(encoded_int)[2:]
    
    # Convert hex string to byte string
    byte_str = bytes.fromhex(hex_str).decode('utf-8')
    return byte_str

#Function to decrypt the Elgamal ciphertext
def decode():
    
    # Open a file to read ciphertext
    f = open("ciphertext.txt", "r")
    
    # Read the ciphertext from the file
    c1 = int(f.readline())
    c2 = int(f.readline())

    # Calculate the private key, your task is to complete this line using all available files in this folder
    x = (p - 1) // 2

    # Decrypt the ciphertext
    s = pow(c1, x, p)
    m = (c2* pow(s, -1, p)) % p

    # Convert the decrypted message from integer to string
    m_decoded = decode_int_to_str(m)
    
    # Print the decrypted message
    print(m_decoded)

if __name__ == "__main__":
    decode()
