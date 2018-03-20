#Give an implementation of a funtion named norm such that norm(v,p)
#returns the p-norm vlaue of v and norm(v) returns the Eucliden norm
#of v. You may ssume that v is a list of numbers.
import math
v = (3,4,5,6)
def norm(v,p = 2):
        a =0
#comprehension
        return ((sum(i**p for i in v))**(1/p))
#        for i in v:
#                a +=  i**p
#       return a**(1/p)
print(norm(v))
print(norm(v,3))
print(norm(v,4))
