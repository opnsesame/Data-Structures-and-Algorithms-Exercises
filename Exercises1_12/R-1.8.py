#Python allows negative integers to be used as indices into a sequence,
#Such as a string. If string s has length n, and expression s[k] is 
#used for index -n<=k<0, what is the equivalent index j>=0 such that
#s[j]  references the same element?

# -n   -n+1 .........k..........  -3      -2      -1
#-------------------------------------------------------
#|   |    |   |   | | | | | | | |      |      |       |
#--------------------------------------------------------
#  0    1   .........j..........   n-3   n-2      n-1      

#j-k = n
#s[j] = s[j-n]