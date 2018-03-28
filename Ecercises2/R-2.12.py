'''
Implement the __mul__ method for the Vector class of Section 2.3.3, so
that the expression v*3 returns a new vector with coordinates that are 3
times the respective coordinates of v.
'''
def __mul__(self,n):
	result = Vector(len(self))
	for i in range(len(self)):
		result[i] = self.[i]*n
	return result