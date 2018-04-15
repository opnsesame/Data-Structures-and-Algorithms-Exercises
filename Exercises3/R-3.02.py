'''
The number of operations executed by algorithms A and B is 8nlog n and
2n^2, respectively. Determine n0 such that A is better than B for n >= n0.

n0 = 16

algorithm A  is O(nlogn)

algorithm B  is O(n^2)


'''
import numpy
n = 2
while 8*n*(numpy.log2(n)) > 2*n**2:
    print(str(8*n*(numpy.log2(n))),'-----------',str(2*n**2))
    n += 1

print('n0 = ',n)

