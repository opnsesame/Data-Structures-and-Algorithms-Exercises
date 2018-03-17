#Give a single command that computes the sum from Exercise R-1.6,relying
#on Python's comprehension syntax and the built-in sum function
n = int(input('please input an positive integer:'))
result = sum(i**2 for i in range(1,n) if i&1!=0)
print(result)