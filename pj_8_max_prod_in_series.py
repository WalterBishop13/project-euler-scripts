import string
#find max product of thirteen adjacent values in series of numbers
def maxProd(x):
    y = str(x)
    maxProd = 0
   
    for i in range(0,len(y)-12):
        accum = 1
        print i
        for j in range(i,i+13):
            accum*=int(y[j])
        if accum > maxProd:
            maxProd = accum
            print accum
    return maxProd
