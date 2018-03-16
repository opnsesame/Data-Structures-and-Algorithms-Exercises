#Write a short Python function, minmax(data),that takes a sequence of
#one or more numbers, and returns the smallest and largest numbers, 
#in the form of a tuple of length two, Do no use the built-in functions
#min or max in implementing  your solution.
def minMax(data):
    print(data)
    Mi = data[0]
    Ma = data[0]
    for i in range(len(data)):
        if Mi>data[i]:
            Mi=data[i]
        if Ma<data[i]:
            Ma=data[i]
#    mMi = ()
#    mMa= ()
#    mM = ()
#    mMi = mM+(Mi,)
#    mMa = mM +(Ma,)
#    mM = mMi + mMa
#    print(mM)
#    return mM
    return Mi,Ma
d = (299,28,-1,-345,45,19,35,67,128,-26,9,0,1000,-18,199,200,-281,231,2,4,5,32,-299)
print(minMax(d))

