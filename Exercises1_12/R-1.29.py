#Write a Python program that outputs all possible strings formed by
#using the characters 'c','a','t','d','o','g' exactly once.

import time
ts = time.time()
s= ['c','a','t','d','o','g']
pr = []
COUNT = 0

def perm(s,first,last):
    global COUNT
    global pr
    if first>=last:
        st = ''
        for ch in s:
            st = st + ch
        pr.append(st)
        COUNT +=1  
    else:  
        i=first
        for num in range(first,last):  
            s[num],s[i]=s[i],s[num]
            perm(s,first+1,last)
            s[num],s[i]=s[i],s[num]   # switch to original order
perm(s,0,len(s))
te = time.time() - ts
print(te)
print(COUNT)
