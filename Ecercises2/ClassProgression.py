'''
The collections.Sequence abstract base class does not provide support for
comparing two sequences to each other. Modify our Sequence class from
Code Fragment 2.14 to include a definition for the __eq__ method, so
that expression seq1 == seq2 will return True precisely when the two
sequences are element by element equivalent.
'''
class Progression:
	'''Iterator producing a generic progression.
	Default iterator produces the whole numbers 0, 1, 2, ...
	'''
	
	def __init__(self, start=0):
		'''Initialize current to the first value of the progression.'''
		self._current = start

	def _advance(self):
		'''Update self. current to a new value.
		this should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
		end of a finite progression.
		'''
		self._current += 1

	def __next__ (self):
		'''Return the next element, or else raise StopIteration error.'''
		if self._current is None: # our convention to end a progression
			raise StopIteration()
		else:
			answer = self._current # record current value to return
			self._advance( ) # advance to prepare for next time
			return answer # return the answer

	def __iter__ (self):
		'''By convention, an iterator must return itself as an iterator.'''
		return self

	def print_progression(self, n):
		'''Print next n values of the progression.'''
		print( '  '.join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression): # inherit from Progression
	'''Iterator producing an arithmetic progression.'''

	def __init__(self, increment=1, start=0):
		'''Create a new arithmetic progression.
		increment the fixed constant to add to each term (default 1)
		start the first term of the progression (default 0)
		'''
		super().__init__(start) # initialize base class
		self._increment = increment

	def _advance(self): # override inherited version
		'''Update current value by adding the fixed increment.'''
		self._current += self._increment
		
class GeometricProgression(Progression):
	'''Create a new geometric progression'''
	def __init__(self,base = 2,start = 1):
		super().__init__(start)
		self._base = base
		
	def _advance(self):
		
		self._current *= self._base
		
class FibonacciProgression(Progression):
	
	def __init__(self,first = 0,second = 1):
		super().__init__(first)
		self._prev = second -first
	
	def _advance(self):
		self._prev,self._current = self._current, self._prev + self._current
