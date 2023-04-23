import random
from numpy import sqrt


def gcd(a, b):
    return a if (b==0) else gcd(b, a % b)

#a^n mod c
def PowMod(a, n, c):
    ans = 1
    base = a % c
    while n:
        if n & 1:
            ans = (ans * base) % c
        base = (base * base) % c
        n //= 2
    return ans



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


#P + P definition
def pointAddition(point, curve):
    result = Point

    #lambda
    s = (3 * point.x * point.x + curve.a) * (int)(PowMod(((int)(point.y) << 1), (int)(curve.modulo - 2), (int)(curve.modulo)))

    #addition itself
    result.x = (s * s - point.x - point.x) % curve.modulo
    result.y = (s * (2 * point.x + result.x) - s * s) % curve.modulo

    return result

class EllipticCurve:
    def __init__(self, a, b, modulo):
        self.a = a
        self.b = b
        self.modulo = modulo

def LenstraEllipticCurveFactorization(modulus):
    if modulus % 2 == 0:
        return 2
    elif modulus % 3 == 0:
        return 3
    elif modulus % 5 == 0:
        return 5
    elif modulus % 7 == 0:
        return 7
    elif modulus % 11 == 0:
        return 11
    #Elementary divisor elimination

    
    P0 = Point
    P0.x = random.randint(1, modulus - 1)
    P0.y = random.randint(1, modulus - 1)
    #random point generation
    
    E = EllipticCurve
    E.a = random.randint(1, modulus - 1)
    E.b = random.randint(1, modulus - 1)
    E.modulo = modulus
    #random curve


    points = [P0]
    d = 0

    for i in range(1, (int)(sqrt(modulus))):
        points.append(pointAddition(points[i-1], E))


        d = (int)(gcd((int)(modulus), (int)(points[i-1].y)))

        #test if the divisor has been found
        if(d > 1 & d < modulus):
            return d


    return -1

#executes the Factorization and prints out the found divisors and returns a list with the found divisors
def LECF(modulus):
    results = []
    while (modulus != 1):
        results.append(LenstraEllipticCurveFactorization(modulus))
        if(results[-1] == -1):
            results[-1] = (int)(modulus)
            print(results[-1])
            return results

        modulus/= results[-1]
        print(results[-1])

LECF(10590456016)  