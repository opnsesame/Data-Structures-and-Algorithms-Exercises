def is_multiple(n,m):
    x,y = divmod(n,m)
    if x >=1 and y ==0:
        print('n is %d time of m'%x)
    else:
        print('n is not multiple of m')
n = int(input('please input first number'))
m = int(input('please input second number'))
is_multiple(n,m)
