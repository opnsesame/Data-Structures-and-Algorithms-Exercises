#Write a short Pyton function that takes a positive integer n and returns
#the sum of the squares of all the positive integers smaller than n.
def sigmaSquareN(n):
    list =[]
    sum = 0
    for i in range(1,n):
        sum += i**2
        if sum < n:
           print ('Sigma of  squrae %d=%d'%(i,sum))
           list.append(sum)
        else:
            break
    return list
n = int(input('Please input a positive integer'))
if n >= 0:
    print(sigmaSquareN(n))
