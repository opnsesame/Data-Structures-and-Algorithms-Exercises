'''
The number of operations executed by algorithms A and B is 40n^2 and
2n^3, respectively. Determine n0 such that A is better than B for n ≥ n0.
n0 = 21

algorithm A is O(n^2)
algorithm B is O(n^3)

'''
n = 1
while 40*n**2 >= 2*n**3:
    n += 1

print('n0 =',n)
