'''
What is the sum of all the even numbers from 0 to 2n, for any positive
integer n?
'''
sum = 0
n = 100
for i in range(0,2*n+2,2):
    sum = sum +i
print(str(sum))
