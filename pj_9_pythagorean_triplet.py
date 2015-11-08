#find product abc of pythagorean triplet such that a^2+b^2=c^2, a<b<c, and a+b+c=1000
for i in range(0,1001):
    for j in range(0,1001):
        for k in range(0,1001):
            if a**2+b**2==c**2 and a+b+c==1000: #only 1 solution under 1000, so a<b<c guaranteed
                print a,b,c,a*b*c

