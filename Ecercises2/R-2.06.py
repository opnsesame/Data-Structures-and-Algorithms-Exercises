'''
If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent.
'''
def make_payment(self,amount):
		if amount < 0:
			raise ValueError("Payment amount can not be negative")
		else:
			try:
				self._balance -= amount
				msg = '$' + str(amount) +' Payment received' + 'New balance is '+'$'+str(self._balance)
				return msg
			except (ValueError,NameError,SyntaxError) as e:
				print('Please input correct number')
				print(e)