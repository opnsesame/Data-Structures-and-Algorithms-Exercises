#Give a single command that computes the sum from Exercise R-1.4, relying
#on Python's comprehension syntax and the built-in sum function

n = int(input('Please input a positive integer'))
if n >= 0:
    result =sum(i**2   for i in range (n+1))
    print(result)
