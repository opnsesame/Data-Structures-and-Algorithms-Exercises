'''
Give an example of a function that is plotted the same on a log-log scale
as it is on a standard scale

y = x

'''
import numpy
import matplotlib.pyplot

x = [i for i in range(1,20)] #standard scale
y = x
x1 = [numpy.log2(x) for x in x] #log-log scale
y1 = [numpy.log2(y) for y in y]

matplotlib.pyplot.plot(x,y,'ro',x1,y1,'b*')
matplotlib.pyplot.show()
