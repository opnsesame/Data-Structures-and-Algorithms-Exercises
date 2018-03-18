#Write a pseudo-code description of a function that reverses a list of n
#integers,so that the numbers are listed in the opposite order than they 
#were before, and compare this method to an equivalent Pyton function for
#doing the same thing.

listNintegers = [1,4,5,8,2,7,0,11]
reverseList = []
n = len(listNintegers)
for i in range(0,n):
   reverseList.append(listNintegers[0-i-1])
print(listNintegers)
print(reverseList)
 #Call syetem methord to reverse a list     
listNintegers.reverse()
print(listNintegers)
