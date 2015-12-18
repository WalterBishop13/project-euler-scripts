#find first triangular number with over 500 divisors
import math

#produces nth triangle number
def triangleNum(n):
    return sum(range(1,n+1))

#counts number of factors of number x, assuming x positive
def factorTally(x):
    if x==1:
        return 1
    elif x<=3:
        return 2
    tally = 2
    temp = int(math.sqrt(x))
    for i in range(2,temp):
        if x%i==0:
            tally+=2
    if x%temp==0:
        tally+=1
    return tally

n=1
x = triangleNum(n)
while factorTally(x)<501:
    n+=1
    x = triangleNum(n)
print(x)               
               

