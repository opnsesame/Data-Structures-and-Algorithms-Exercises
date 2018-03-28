'''
In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector.
'''
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