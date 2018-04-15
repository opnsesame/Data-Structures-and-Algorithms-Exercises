'''
Explain why the plot of the function n^c is a straight line with slope c on a
log-log scale.

y = n^c
log(y) = c*log(n)
set X = log(n) , Y = log(y)
Y = cX
c is the slope of Y=cX
'''

import numpy
import matplotlib.pyplot
c = 5
x = [numpy.log2(i) for i in range(1,20)]
y = [c*x for x in x]

matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.show()
