#bool declaring if integer x is a prime number
#using conditions and array of prime #s for determination of primeness
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
        
#determines nth prime number
def nthPrime(x):
    if x<1:
        print("YOU STUPID")
        return None
    elif x<3:
        return x+1
    primes = [2,3]
    val = 4
    while len(primes)!=x:
        if isPrime(val,primes):
            primes.append(val)
            val+=1
        else:
            val+=1
    return primes[-1]
