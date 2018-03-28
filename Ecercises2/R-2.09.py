'''
Implement the sub method for the Vector class of Section 2.3.3, so
that the expression u−v returns a new vector instance representing the
difference between two vectors.
'''

class Vector:
	'''Represent a vector in a multidimensional space.'''

	def __init__(self, d):
		'''Create d-dimensional vector of zeros.'''
		self. coords = [0]*d

	def __len__(self):
		'''Return the dimension of the vector.'''
		return len(self. coords)

	def __getitem__(self, j):
		'''Return jth coordinate of vector.'''
		return self. coords[j]

	def __setitem__ (self, j, val):
		'''Set jth coordinate of vector to given value.'''
		self.coords[j] = val

	def __add__(self, other):
		'''Return sum of two vectors.'''
		if len(self) != len(other): # relies on len method
			raise ValueError('dimensions must agree')
		result = Vector(len(self)) # start with vector of zero
		for j in range(len(self)):
			#print('self[{}]+other[{}]='.format(j,j),self[j]+other[j])
			result[j] = self[j] + other[j]
			#print('result=',result)
		return  result
	__radd__ = __add__	
	'''sub method returns a new vector instance representing the
		difference between two vectors'''
	def __sub__ (self,other):
		if len(self) != len(other): # relies on len method
			raise ValueError('dimensions must agree')
		result = Vector(len(self)) # start with vector of zero
		for j in range(len(self)):
			print('self[{}]-other[{}]='.format(j,j),self[j]-other[j])
			result[j] = self[j] - other[j]
		#print('result=',self.coords)
		return  result
		
	def __eq__ (self, other):
		'''Return True if vector has same coordinates as other.'''
		return self. coords == other. coords

	def __ne__ (self, other):
		'''Return True if vector differs from other.'''
		return not self == other # rely on existing eq definition
	
	def __neg__(self):
		result = Vector(len(self))
		for i in range(len(self)):
			result[i] = - self[i]
		return result

	def __mul__(self,n):
		result = Vector(len(self))
		for i in range(len(self)):
			result[i] = self[i]*n
		return result
	__rmul__ = __mul__
	
	def __mul__(self,other):
		if len(self) != len(other):
			raise ValueError('dimensions must agree')
		result = Vector(len(self))
		for i in range(len(self)):
			result[i] = self[i]*other[i]
		return result

	def __str__ (self):
		'''Produce string representation of vector.'''
		return '<' + str(self. coords)[1:-1] + '>' # adapt list representation
v1 =Vector(4)
v2 =Vector(4)
v1[0]=44
v1[1]=10
v2[1]=22
print('v1=:   ',v1)
print('v2=:   ',v2)
v3=v1*v2
print(v3)
