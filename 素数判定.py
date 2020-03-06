def  isPrime(k):
    for i in range(2,k):
        if k % i == 0:
            return False
    return True

def getPrime(n):
    primes = []
    for i in range(1,n+1):
        if isPrime(i):
            primes.append(i)
    return primes

n = 100
print(getPrime(n))