from keyGeneration import p, h, g

def decode_int_to_str(encoded_int):
    hex_str = hex(encoded_int)[2:]
    byte_str = bytes.fromhex(hex_str).decode('utf-8')
    return byte_str

def decode():
    f = open("ciphertext.txt", "r")

    c1 = int(f.readline())
    c2 = int(f.readline())

    y = (p - 1) // 2

    s = pow(h, y, p)
    m = (c2* pow(s, -1, p)) % p

    m_decoded = decode_int_to_str(m)

    print(m_decoded)

decode()
