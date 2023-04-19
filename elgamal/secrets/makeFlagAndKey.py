import random

def makeKey():
    key = random.randint(1, 10**100) # vygeneruje náhodné číslo s alespoň 100 ciframi
    with open('key.txt', 'w') as f:
        f.write(str(key))

def makeFlag():
    flag = "Tajemstvi!"
    with open('flag.txt', 'w') as f:
        f.write(flag)

def main():
    makeKey()
    makeFlag()

if __name__ == "__main__":
    main()