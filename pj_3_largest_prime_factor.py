from math import *
#build list of primes from 2 up to and including integer x
def listPrimes(x):
    temp = [2]
    if x<=2:
        return temp
    else:
        for i in range(3,x+1,2):
            for j in range(3,i+1,2):
                if i%j==0:
                    break
            if i==j:
                temp.append(i)
        
        return temp

#bool declaring if integer x is a prime number     
def isPrime(x):
    n=1
    k=0
    if x==2 or x==3:
        return True
    elif x%2==0 or x<2:
        return False
    for j in str(x):
        k+=int(j)
    if k%3==0:
        return False
    else:
        while x%(3+2*n)!=0:
            n+=1
        return True if 3+2*n==x else False

                
#gives largest prime factor of integer x
def largestPF(x):
   n = 1
   while x-n!=0 and not(x%(x-n)==0 and isPrime(x-n)):
       n+=1
   return x-n if  x-n!=0 else None

def largestPF2(y):
    x = floor(sqrt(y))
    i = 1
    temp = []
    while i<=x:
        if y%i==0:
            temp.append(i)
            i+=1
        else:
            i+=1
    for j in range(len(temp)-1,-1,-1):
        temp.append(y/temp[j])
    for k in range(len(temp)-2,0,-1):
        if isPrime(temp[k]):
            return temp[k]
    return "No primes"
