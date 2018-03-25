'''
Write a Python class, Flower,that has three instance variables of
type str, int, and float, that respectively represent the name of
the flower, its number of petals,and its price. Your cass must
include a constrctor method that initializes each variable to an
appropriate value, and your class should include methods for setting 
the value of each type,and retrieving the value of each type.
'''

class Flower():
	def __init__(self,flowerName,petals,price):
		self._flowerName = ''
		self._petals = 0
		self._price = 0.0
		self._setFlowerName(flowerName)
		self._setPetals(petals)
		self._setPrice(price)
	def _setFlowerName(self,flowerName):
		self._flowerName = flowerName
		
	def getFlowerName(self):
		return self._flowerName
	
	def _setPetals(self,petals):
		self._petals = petals
		
	def getPetals(self):
		return self._petals
		
	def _setPrice(self,price):
		self._price = price
		
	def getPrice(self):
		return self._price
	
	def __str__(self):
		msg = "Flower name ="+self._flowerName+'\n'+"Price ="+str(self._price)+'\n'+"Petals ="+str(self._petals)
		return msg
