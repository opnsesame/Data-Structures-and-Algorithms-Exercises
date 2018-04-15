import functools
import time

def timer(func):
    functools.wraps(func)
    def wr(*a):
        start = time.time()
        rv = func(*a)
        end = time.time()
        #print('elapsed: ',end-start)
        return rv
    return wr

@timer
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

f = factorial(5)  
