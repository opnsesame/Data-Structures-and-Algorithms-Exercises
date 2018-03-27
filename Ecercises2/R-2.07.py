'''
The CreditCard class of Section 2.3 initializes the balance of a new account
to zero. Modify that class so that a new account can be given a
nonzero balance using an optional fifth parameter to the constructor. The
four-parameter constructor syntax should continue to produce an account
with zero balance.
'''
class CreditCard():
	def __init__(self,customer,bank,acnt,limit,balance=0):
		self._customer = customer
		self._bank = bank
		self._acnt = acnt
		self._balance = balance
		self._limit = limit