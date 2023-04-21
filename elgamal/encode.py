# Import necessary modules and functions
from mysterious import key, flag
from keyGeneration import p, h, g

#Function to ecrypt the user message
def encode():
    # Open a file to write ciphertext
    f = open('ciphertext.txt', 'w')

    # Convert unknown plaintext to integer using hexadecimal encoding
    m = int(flag.encode('utf-8').hex(), 16) % p

    # Generate the public key component
    c1 = pow(g, key, p)

    # Generate the shared secret component
    s = pow(h, key, p)

    # Encrypt the plaintext using ElGamal encryption
    c2 = m * s % p

    # Write the ciphertext components to file
    f.write(str(c1) + '\n')
    f.write(str(c2) + '\n')

    # Close the file
    f.close()

if __name__ == "__main__":
    encode()