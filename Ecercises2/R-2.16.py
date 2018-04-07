'''
Our Range class, from Section 2.3.5, relies on the formula
max(0, (stop − start + step − 1) // step)
to compute the number of elements in the range. It is not immediately evident
why this formula provides the correct calculation, even if assuming
a positive step size. Justify this formula, in your own words.
'''
'''

      L-A 
n = ------- + 1
       d
	   	   
	   
Divide the common difference (d) into the difference between the last term (L) and the first term (A), and then add 1.

'''