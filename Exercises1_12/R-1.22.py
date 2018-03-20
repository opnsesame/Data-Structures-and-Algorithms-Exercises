#Write a short Python program that takes two arrays a and b of lengh n
#storing int values, and returns the dot product of a and b. That is , 
#returns an array c of length n such that c[i] = a[i].b[i], 
#for i =0....n-1

#return [a[i]*b[i] for i in range(n)]

a = [2,5,3,-12]
b = [7,2,-9,9]
def dotProduct(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return c
print(dotProduct(a,b))


