#Write a short Pyton function that takes a positive integer n and returns
#the sum of the squares of all the positive integers smaller than n.
def sigmaSquareN(n):
    list =[]
    sum = 0
    for i in range(n):
        sum += i**2
        print ('i=%d,Sigma of  squrae i=%d'%(i,sum))
        if sum < n:
           list.append(sum)
        else:
            break
    return list
n = int(input('Please input a positive integer'))
if n >= 0:
    print(sigmaSquareN(n))
