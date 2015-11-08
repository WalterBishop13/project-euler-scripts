#recursively find nth fibonacci sequence term
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fib(n-1)+fib(n-2)

#find nth fibonacci term that does not exceed input integer
#upper-limited by constraints of int type
def findFibN(x):
    n = 1
    while fib(n) <= x:
        n+=1
    return n-1


#summing even fibonacci numbers under input integer x
def sumEvenFibUnder(x):
    count = 0
    nLimit = findFibN(x)
    for i in range(nLimit):
        f = fib(i+1)
        if f%2==0:
            count+=f
    return count
