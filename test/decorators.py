from time import time
import functools
def timer(func):
    functools.wraps(func)
    def f(*a,**kw):
        before = time()
        rv = func(*a,**kw)
        after = time()
        print('elasped',after-before)
        return rv
    return f
@timer
def add(x,y=1):
    return x + y
@timer
def sub(x,y=10):
    return x - y
print('add(10)',add(10))
print('add(20,30)',add(20,30))
print('add("a","b")',add("a","b"))
