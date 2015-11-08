#build list of primes from 2 up to and including integer x and compute sum
def isPrime(x,prime_array):
    n=0
    if x%2==0:
        return False
    for j in str(x):
        n+=int(j)
    if n%3==0:
        return False
    else:
        for k in prime_array:
            if x%k==0:
                return False
        return True
#test using subpar algorithm, heavy on mem and time
prime_array = [2,3,5]
for i in range(6,2000000):
    if isPrime(i, prime_array):
        prime_array.append(i)

print sum(prime_array)

