'''
Draw a class inheritance diagram for the following set of classes:
• Class Goat extends object and adds an instance variable tail and
methods milk( ) and jump().
• Class Pig extends object and adds an instance variable nose and
methods eat(food) and wallow( ).
• Class Horse extends object and adds instance variables height and
color, and methods run() and jump( ).
• Class Racer extends Horse and adds a method race( ).
• Class Equestrian extends Horse, adding an instance variable weight
and methods trot( ) and is_trained( ).
'''

class Goat:
	def __init__(self,tail):
		self.tail = tail
	
	def milk():
		pass
	
	def jump():
		pass

class Pig:
	def __init__(self,nose):
		self.nose = nose
		
	def eat(self, food):
		pass
	
	def wallow(self):
		pass
	
class Horse:
	def __init__(self,height,color):
		self.height=height
		self.color=color
		
	def run(self):
		pass
	
	def jump(self):
		pass
	
class Racer(Horse):
	def __init__(self):
		pass
	
	def race(self):
		pass
class Equestrian(Horse):
	def __init__(self,weight):
		pass
	def trot(self):
		pass
	def is_trained(self):
		pass
	
	
'''
      Horse               Goat      Pig
    |       |
  Racer  Equestrian
 

'''
		