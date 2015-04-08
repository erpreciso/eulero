import math
import time
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
def timing(x):
    startTime = time.time()
    print findMaxPrime(x)
    endTime = time.time()
    return endTime - startTime

def isprime_simple(num):
    k = 1
    prime = True
    while k < num - 1:
        k += 1
        if num % k == 0:
            prime = False
            break
    return prime

def isprime_complex(num):
    if num < 4:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    x = 3
    while x < math.sqrt(num):
        if num % x == 0:
            return False
        x += 2
    return True

    
#print isprime_complex(28)

n = 13195
n = 10000033

def findMaxPrime_simple(n):
    counter = n - 1
    res = 1
    divis = []
    while counter > 1:
        if n % counter == 0:
            if isprime_simple(counter):
                return counter
        counter -= 1
    return "Not found"

def findMaxPrime_complex(n):
    counter = n - 1
    res = 1
    divis = []
    while counter > 1:
        if n % counter == 0:
            if isprime_complex(counter):
                return counter
        counter -= 1
    return "Not found"

#print timing(n)


