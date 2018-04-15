'''
Show that if d(n) is O( f (n)) and e(n) is O(g(n)), then d(n)−e(n) is not
necessarily O( f (n)−g(n)).
'''
Let d(n)=2n  and e(n)=n
Then d(n)−e(n)=n.
Since d(n)=O(n)  and e(n)=O(n)
we have that f(n)=g(n)=n,
so
O(f(n)−g(n))=O(n−n)=O(1),
and clearly
n≠O(1).
