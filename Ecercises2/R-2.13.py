'''
Exercise R-2.12 asks for an implementation of __mul__ , for the Vector
class of Section 2.3.3, to provide support for the syntax v*3. Implement
the rmul method, to provide additional support for syntax 3*v.
'''
def __mul__(self,n):
	result = Vector(len(self))
	for i in range(len(self)):
		result[i] = self.[i]*n
	return result
__rmul__ = __mul__