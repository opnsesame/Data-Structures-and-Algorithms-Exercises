'''
Show that f(n) is O(g(n)) if and only if g(n) is Ω(f(n)).
'''

Let f(n) and g(n) be positive functions, Prove that if f(n) is O(g(n)) then g(n) is Ω(f(n)).
    If f(n) is O(g(n)) then
       there exist a constant c > 0, and a constant n0 such that for all n ≥ n0: f(n) ≤ c*g(n)
    hence:
       there exist a constant c > 0, and a constant n0 such that for all n ≥ n0: g(n) ≥ (1/c)*f(n)
         note that since c > 0, then the constant (1/c) > 0
    hence:
       there exist a constant k > 0, namely k = (1/c), and a constant n0 such that for all n ≥ n0: g(n) ≥ k*f(n)
    which is the definition of g(n) = Ω (f(n)).

Let f(n) and g(n) be positive functions, Prove that if g(n) is Ω(f(n)) then f(n) is O(g(n)).
    If g(n) = Ω (f(n)) then
        there exist a constant k > 0, and a constant n0 such that for all n ≥ n0: g(n) ≥ k*f(n)
    hence:
        there exist a constant k > 0, and a constant n0 such that for all n ≥ n0: f(n) ≤ (1/k)*g(n)
           note that since k > 0, then the constant (1/k) > 0
    hence:
        there exist a constant c > 0, namely c = (1/k), and a constant n0 such that for all n ≥ n0: f(n) ≤ c*g(n)
    which is the definition of f(n) = O(g(n)).
