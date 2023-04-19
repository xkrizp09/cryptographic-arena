from mysterious import key, flag
from keyGeneration import p, h, g

f = open('ciphertext2.txt', 'w')

y = key
m = int(flag.encode('utf-8').hex(), 16) % p

c1 = pow(g, y, p)
k = pow(h, y, p)
c2 = k * m % p

f.write(str(c1) + '\n')
f.write(str(c2) + '\n')

f.close()