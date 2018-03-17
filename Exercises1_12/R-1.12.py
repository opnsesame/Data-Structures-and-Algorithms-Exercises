#Python's random module includes a function choice(data) that returns a 
#random element from a non-empty sequence. The random modul includes a 
#more basic function randrange,with parameterization similar to the 
#built-in range function , that return a random choice from the given
#range.Using only the randrange funciton,implement your own version of 
#the choice function.
import random
lottoMax = list()
lottoMax = [random.randrange(1,50,1) for i in range(1,8)]
print(lottoMax)