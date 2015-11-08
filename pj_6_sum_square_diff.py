#difference between the sum of the
#squares of the first one hundred natural numbers and the square of the sum

x=[]
for i in range(1,101):
    x.append(i**2)
sum_of_squares = sum(x)
square_of_sum = (sum(list(range(1,101))))**2

diff = square_of_sum - sum_of_squares
