'''
Show that if d(n) is O( f (n)) and e(n) is O(g(n)), then d(n) +e(n) is
O( f (n)+g(n)).
'''
set d(n) <= f(n) for all n>n0 , e(n) <= g(n) for all n>m0
d(n) + e(n) <= f(n)+g(n) for all n>max(n0,m0)
so d(n)+e(n) is O(f(n)+g(n))


The functions f(n) and g(n) are asymptotically non negative, there exists
n0 such that f(n) ≥ 0 and g(n) ≥ 0 for all n ≥ n0.

Thus, we have that for all n ≥ n0, f(n) + g(n) ≥ f(n) ≥ 0 and f(n) + g(n) ≥
g(n) ≥ 0. Adding both inequalities (since the functions are nonnegative),
we get f(n) + g(n) ≥ max(f(n); g(n)) for all n ≥ n0.

This proves that
max(f(n); g(n)) ≤ c(f(n) + g(n)) for all n ≥ n0 with c = 1, in other
words, max(f(n); g(n)) = O(f(n) + g(n)).

Similarly, we can see that max(f(n); g(n)) ≥ f(n) and max(f(n); g(n)) ≥
g(n) for all n ≥ n0. Adding these two inequalities, we can see that
2max(f(n); g(n)) ≥ (g(n) + f(n))
, or
max(f(n); g(n)) ≥ 1/2(g(n) + f(n))
for all n ≥ n0.
