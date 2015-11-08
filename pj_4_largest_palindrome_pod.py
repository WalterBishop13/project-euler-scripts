#returns largest palindrome product of two three-digit numbers (ijk*xyz)=form abccba
def palinProd():
    num=[0,0,0]
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            x = str(i*j)
            if i*j>99999 and x[0]==x[5] and x[1]==x[4] and x[2]==x[3] and i*j>num[2]:
                num = [i,j,i*j]
    return num
