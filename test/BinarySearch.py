import random
import time
import functools
x = [random.randint(1,1000000) for i in range(1000000)]
x.sort()
#print(x)
def timer(func):
    functools.wraps(func)
    def wr(*a):
        start = time.time()
        rv = func(*a)
        end = time.time()
        #print('elapsed: ',end-start)
        return rv
    return wr

#@timer
def findThis(x,n):
#    print('-----------------------------------------------------------------------------------------')
    l = len(x)
    if l == 0:
#        print('N not found in the list')
        return False
    if l==1:
        if x[0] != n:
#            print('N not found in the list')
            return False
        else:
#            print('Found N')
            return True
    mid = x[l//2]
#    print('mid = : ',mid,'x[{}]'.format(l//2))
    if mid == n:
#        print('find :',n)
        return True
    if mid < n:
#        print('mid < n ,original x = :',x)
#        print('l =:', l//2)
        x = x[l//2:]   #slice original list x . leave the half part that includes n.
#        print('new x =: ',x)        
        return findThis(x,n)
    if mid > n:
#        print('mid >n, original x = :',x)        
#        print('l =:', l//2)        
        x = x[:l//2]  #slice original list x . leave the half part that includes n.
#        print('new x = :',x)
        return findThis(x,n)
start = time.time()
print(findThis(x,25))
end = time.time()
print(end - start)
print('+++++++++++++++++++++++++++++++')

#@timer
def bSearch(x,n,low,high):
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if n == x[mid]:
            return True
        elif n < x[mid]:
            return bSearch(x,n,low,mid-1)
        else:
            return bSearch(x,n,mid+1,high)
start = time.time()        
print(bSearch(x,25,0,len(x)))
end = time.time()
print(end - start)
