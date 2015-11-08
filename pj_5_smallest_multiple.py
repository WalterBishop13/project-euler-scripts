#returns smallest positive number that is evenly divisible
#by all numbers between 1 and 20

n = 1
flag=True
while flag:
    n+=1
    count=0
    for i in range(11,20):
        if 20*n%i==0:
            count+=1
        if count==9:
            print(20*n)
            flag=False
