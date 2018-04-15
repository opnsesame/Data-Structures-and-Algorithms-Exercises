'''
Show that if d(n) is O( f (n)) and f (n) is O(g(n)), then d(n) is O(g(n)).
'''
d(n) is O(f(n)) so there is a c and n0 when d(n) <= cf(n) for all n>n0
f(n) is O(g(n)) so there is a k and m0 when f(n) <= kg(n) for all n>n0
d(n) <= cf(n) <= c(k(g(n)))= c*k(g(n))
so d(n) is O(g(n))
