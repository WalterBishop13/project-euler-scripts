def sum35(x):
    count = 0
    for i in range(x):
        if i%3==0 and i%5==0:
            count+=i
        elif i%3==0 or i%5==0:
            count+=i
    return count
