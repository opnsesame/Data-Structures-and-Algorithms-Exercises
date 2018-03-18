#Write a short Python function that takes a sequence of integer values
#and determines if there is a distinct pair of numbers in the sequence
#whose product is odd
list = [2,4,3,6,8,12,5,9,11]
def oddProduct(list):
    n = len(list)
    for i in range(n-1):
        for j in range(1+i,n):
            if (list[i]*list[j])&1 == 1 and list[i] != list[j]:
                print("list[%d]*list[%d]is odd number"%(i,j))
oddProduct(list)               
oddProduct([1,3,5,4,3])
