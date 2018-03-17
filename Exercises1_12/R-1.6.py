#Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all odd positive integers smaller than n.
def sumOfSquareN(n):
    sum=0
    for i in range(1,n):
        if i&1 != 0:
            sum += i**2
    return sum
n = int(input('please input an positive integer:'))
print(sumOfSquareN(n))
