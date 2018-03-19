#Write a Python function that takes a sequence of numbers and determines
#if all the numbers are different from each other(that is , they are
#distinct)
list = [2,4,3,6,8,12,5,9,11]
def distinctNumbers(list):
    n = len(list)
    for i in range(n-1):
        for j in range(1+i,n):
            if list[i] == list[j]:
                print("list[%d] and list[%d]are same numbers"%(i,j))
distinctNumbers(list)               
distinctNumbers([1,3,5,4,3])
