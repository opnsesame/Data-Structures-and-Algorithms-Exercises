'''
Use the techniques of Section 1.7 to revise the charge and make_payment
methods of the CreditCard class to ensure that the caller sends a 
number as a parameter.
'''
class CreditCard():
	def __init__(self,customer,bank,acnt,limit,balance=0):
		self._customer = customer
		self._bank = bank
		self._acnt = acnt
		self._balance = balance
		self._limit = limit
	
	def __str__(self):
		msg = "Customer: "+self._customer+"\n"+"Bank : "+self._bank+"\n"+"Account number : " + self._acnt+"\n"+"Credit limit : "+str(self._limit)+"\n"+"New balance : "+ str(self._balance)
		return msg
	def get_customer(self):
		return self._customer
	
	def get_bank(self):
		return self._bank
	
	def get_account(self):
		return self._account
	
	def get_limit(self):
		return self._limit
	
	def get_balance(self):
		return self._balance
	
	def charge(self,price):
		try:
			if price + self._balance > self._limit:
				print("Your charge is over the limit!")
				return False
			else:
				self._balance += price
				msg = '$' + str(price) +' Charged' + 'New balance is '+'$'+str(self._balance)
				return msg
		except (ValueError,NameError,SyntaxError) as e:
			print('Please input correct number')
			print(e)
			
	def make_payment(self,amount):
		if amount < 0:
			print("amount<0")
			raise ValueError("Payment amount can not be negative")
		else:
			try:
				self._balance -= amount
				msg = '$' + str(amount) +' Payment received' + 'New balance is '+'$'+str(self._balance)
				return msg
			except (ValueError,NameError,SyntaxError) as e:
				print('Please input correct number')
				print(e)


peter = CreditCard('peter','cibc','1234 5678 9012 3456',1500)
try:
	peter.charge(123)
	peter.charge(d)
except (ValueError,NameError,SyntaxError) as e:
	print('Please input correct number')
peter.make_payment(-19)
