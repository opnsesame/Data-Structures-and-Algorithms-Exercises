'''
Show that if p(n) is a polynomial in n, then log p(n) is O(logn).
'''
Let p(n) = amn^m + (am-1)n^(m-1) + … + a1n + a0
p(n) < max{|am|, |am-1|, …, |a0|} (m+1)*n^m
log p(n) < log(max{|am|, |am-1|, …, |a0|} (m+1) + m*logn
Since m and ai (i=0, 1, …, m) are constants, we have O(logp(n)) = O(log(max{|am|, |am-1|, …,
|a0|}) (m+1)+O(m log n) = O(log n).
