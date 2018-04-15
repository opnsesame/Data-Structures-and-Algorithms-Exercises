'''
Show that if d(n) is O(f(n)), then ad(n) is O( f (n)), for any constant
a > 0.
'''
Since d(n) is O(f(n)), there are constants a and n0
 set d(n) <= a*d(n) < a*f(n) for all n >=n0
so a*d(n) is O(f(n))
