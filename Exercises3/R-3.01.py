'''
Graph the functions 8n, 4nlogn, 2n^2, n^3, and 2^n using a logarithmic scale
for the x- and y-axes; that is, if the function value f (n) is y, plot this as a
point with x-coordinate at logn and y-coordinate at logy.
'''
import numpy
import matplotlib.pyplot
x , y, y1,y2,y3,y4 = [],[],[],[],[],[]
for i in range(2,20):
    x.append(numpy.log(i))
    y.append(3+x[i-2]) #log (8n)
    y1.append(2+x[i-2]+numpy.log(x[i-2])) #log (4nlogn)
    y2.append(1+2*x[i-2]) # log (2n^2)
    y3.append(3*x[i-2]) #log(n^3)
    y4.append(numpy.log2(x[i-2])) #log(2^n)
print(x)

#matplotlib.pyplot.plot(x,y,'ro',x,y1,'b*',x,y2,'g^',x,y3,'ks',x,y4,'m+')
matplotlib.pyplot.plot(x,y,'r',x,y1,'b',x,y2,'g',x,y3,'k',x,y4,'m')
matplotlib.pyplot.show()
