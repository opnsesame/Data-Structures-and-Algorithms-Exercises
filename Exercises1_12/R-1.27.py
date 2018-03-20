#In Section 1.8 we provided three different implementations of a generator
#that computes factors of a given integer.The third of those
#implementations,from page 41, was the most efficient, but we noted that 
#it did not yield the factors in increasing order. Modify the generator so
#that it reports factors in increasing order, while maintaining its general
#performance advantages.
import time
n = 100000000000
tst = time.time()
def factors(n):
    buf = []
    k = 1
    while k*k < n:
        if n%k == 0:
            yield k
            buf.append(n//k)
        k += 1
    if k*k == n:
        yield k
    for val in reversed(buf):
        yield val
t = time.time() - tst
print(t)

tst = time.time()
def factors(n):
    k = 1
    while k*k < n:
        if n%k == 0:
            yield k
            yield n//k
        k += 1
    if k*k == n:
        yield k
s = sorted(factors(n))
t = time.time() - tst
print(t)


