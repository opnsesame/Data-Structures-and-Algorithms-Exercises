#In our implementation of the scale function(page 25),the body of the loop
#executes the command data[j] *= factor. We have discussed that numeric
#types are immutable, and that use of the *= operator in this context causes
#the creation of a new instance (not the mutation of an existion instance).
#how is it still possible, then, that our implementation of scale changes the
#actual parameter sent by the caller?

#data and data1 are alias
data = [1,2,3,4,5,6]
data1 = data
def scale(data,factor):
    for j in range(len(data)):
          data[j]  *= factor
scale(data,0.5)
print(data)
print(data1)
data1 += [10]
print(data)
print(data1)
#data and data1 alias break
data1 = data1 + [7]
print(data)
print(data1)
