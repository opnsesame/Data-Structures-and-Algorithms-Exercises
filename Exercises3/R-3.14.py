'''
Show that O(max{ f (n),g(n)}) = O( f (n)+g(n)).
''
s(n) is O(f(n)+g(n)) if and only if there is an M such that
|s(n)| ≤ M(f(n) + g(n)) for large enough n, which is equivalent to:
|s(n)| ≤ M·max{f(n), g(n)} + M·min{f(n), g(n)} for large enough n.

For that same M the following would then also be true -- here we depend on the assumption that both f(n) and g(n) are positive for large n:

|s(n)| ≤ 2M·max{f(n), g(n)} for large enough n.

If we now choose P to be 2M, then we can say we have a P for which:

|s(n)| ≤ P·max{f(n), g(n)} for large enough n.

...which according to the definition of big-O means that

s(n) is O(max{f(n), g(n)})
