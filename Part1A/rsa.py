import sys
import os
import random
import time

sys.setrecursionlimit(5000)

# Extended Euclidean Algorithm from page 958 of textbook pdf
def EXTENDED_EUCLIDEAN(a, b):
    if (b == 0):
        return (a, 1, 0)

    else:
        (d_prime, x_prime, y_prime) = EXTENDED_EUCLIDEAN(b, a % b)
        (d, x, y) = (d_prime, y_prime, (x_prime - ((a // b) * y_prime)))
        
        return (d, x, y)

def MODULAR_INVERSE(a, m):
    if (EXTENDED_EUCLIDEAN(a, m)[0] != 1):
        return None

    return (EXTENDED_EUCLIDEAN(a, m)[1] % m)

# Witness Algorithm from page 990 of textbook pdf
def WITNESS(a, n):
    t = 0
    u = n - 1
    
    while ((u % 2) == 0):
        u = u // 2
        t = t + 1
    
    #((n - 1) == (pow(2, t) * u)) at this point
    x = [0 for _ in range(t + 1)]
    x[0] = pow(a, u, n)
    
    for i in range(1, t + 1):
        x[i] = pow(x[i - 1], 2, n)

        if ((x[i] == 1) and (x[i - 1] != 1) and (x[i - 1] != (n - 1))):
            return True
    
    if (x[t] != 1):
        return True
    
    return False

# Miller-Rabin Algorithm from page 991 of textbook pdf
def MILLER_RABIN(n, s):
    for _ in range(1, s):
        a = random.randint(1, n - 1)

        if (WITNESS(a, n) == True):
            return False

    return True

def CHECK_IF_PRIME(n):
    if (n < 2):
        return False
    
    for i in integerPrimes1000:
        if (n == i):
            return True

        if ((n % i) == 0):
            return False
        
    return MILLER_RABIN(n, 20)

def GENERATE_PRIME(modulusSize):
    n = random.randint(1, (pow(2, modulusSize) - 1))

    if ((n % 2) == 0):
        n = n + 1

    while (CHECK_IF_PRIME(n) == False):
        n = n + 2
    
    return n

def GENERATE_KEYS(modulusSize):
    p = GENERATE_PRIME(modulusSize)
    q = GENERATE_PRIME(modulusSize)
    N = (p * q)
    PHI_OF_N = ((p - 1) * (q - 1))
    e = (pow(2, 16) + 1)
    d = MODULAR_INVERSE(e, PHI_OF_N)
    publicKey = (e, N)
    privateKey = (d, N)

    fileZero = open("RSA_miscellaneous.txt", "w")
    fileZero.write(f"Modulus Size: {modulusSize}\n\np: {p}\n\nq: {q}\n\nN: {N}\n\nPHI(N): {PHI_OF_N}\n\ne: {e}\n\nd: {d}")
    fileZero.close()

    return (publicKey, privateKey)

def POPULATE_PRIMES1000():
    stringPrimes1000 = list()
    global integerPrimes1000
    integerPrimes1000 = list()

    with open("primes1000.txt") as inputFile:
        for everyLine in inputFile:
            stringPrimes1000.append(everyLine.split("\n"))

    for i in stringPrimes1000:
        del i[-1]

    integerPrimes1000 = [list(map(int, i)) for i in stringPrimes1000]
    integerPrimes1000 = [i for j in integerPrimes1000 for i in j]

def ENCODE(m):
    x = 0
    
    for c in m:
        x = x << 8
        x = x ^ ord(c)

    return x

if __name__ == "__main__":
    print("Final Project: Part 1A\n")

    if os.path.exists("RSA_miscellaneous.txt") or os.path.exists("RSA_public_key.txt") or os.path.exists("RSA_private_key.txt") or os.path.exists("RSA_signature.txt"):
        ans = input("Would you like to overwrite the pre-existing file(s)? (y/n): ")

        if (ans == "y"):
            os.remove("RSA_miscellaneous.txt")
            os.remove("RSA_public_key.txt")
            os.remove("RSA_private_key.txt")
            os.remove("RSA_signature.txt")
        
        else:
            sys.exit("ERROR - File(s) already exist, program has been terminated.\n")
    
    modulusSize = int(input("Enter your desired modulus size in bits (e.g. 1024, 2048): "))
    start_time = time.time()
    
    POPULATE_PRIMES1000()
    (publicKey, privateKey) = GENERATE_KEYS(modulusSize)
    
    fileOne = open("RSA_public_key.txt", "w")
    fileOne.write(f"{publicKey[0]},{publicKey[1]}")
    fileOne.close()
    
    fileTwo = open("RSA_private_key.txt", "w")
    fileTwo.write(f"{privateKey[0]},{privateKey[1]}")
    fileTwo.close()

    M = "I deserve an A"
    x = ENCODE(M)

    fileZero = open("RSA_miscellaneous.txt", "a")
    fileZero.write(f"\n\nMessage: {M}\n\nEncoded Message: {x}")
    fileZero.close()

    signature = pow(x, privateKey[0], privateKey[1])

    fileThree = open("RSA_signature.txt", "w")
    fileThree.write(str(signature))
    fileThree.close()

    print(f"\nRSA keys have been generated in {time.time() - start_time} seconds. Please check the text files!\n")