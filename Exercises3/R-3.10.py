'''
Show that if d(n) is O( f (n)) and e(n) is O(g(n)), then the product d(n)e(n)
is O( f (n)g(n)).
'''
set a , b are constants .
set d(n) <= a*f(n) for all n >= n0
set e(n) <= b*g(n) for all n >= m0
e(n)*d(n) <= a*b*f(n)*g(n) for all n>max(n0,m0)

so d(n)e(n) is O(f(n)g(n)).
