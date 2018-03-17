#Demonstrate how to use Python's list comprehension syntax to produce
#the list[1,2,4,8,16,32,64,126,256]
list = (2**i for i in range(0,9))
print(list)
