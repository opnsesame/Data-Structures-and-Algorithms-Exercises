'''
Implement the __mul__ method for the Vector class of Section 2.3.3, so
that the expression u v returns a scalar that represents the dot product of
the vectors, that is, Σ = ui · vi.
'''

	def __mul__(self,other):
		if isinstance(other,Vector):
			if len(self) != len(other):
				raise ValueError('dimensions must agree')
			result = Vector(len(self))
			for i in range(len(self)):
				result[i] = self[i]*other[i]
			return result
		else:
			result = Vector(len(self))
			for i in range(len(self)):
				result[i] = self[i]*other
			return result
