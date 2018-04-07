'''
Write a Python program that inputs a polynomial in standard algebraic
notation and outputs the first derivative of that polynomial.
'''
import re
polynomial = input('Please input a polynomial notation:')

class DePoly():
    def __init__(self,poylnomal):
        self._poylnomal = poylnomal
        self._coeffi = []
        self._power = []
        self._newConst = []
    def getCoeff(self):
        self._coeffi = re.findall('[-]?[\d]*[x][\^$]',self._poylnomal)
        self._coeffi = [re.compile(r"x\^").sub("", m) for m in self._coeffi]
        for i in range(len(self._coeffi)):
            if self._coeffi[i] == '':
                self._coeffi[i] = '1'
            if self._coeffi[i] == "-":
                self._coeffi[i] = "-1"
        return self._coeffi

    def getPower(self):
        x1 = re.findall('[-]?[\d]*[x](?!\^)',self._poylnomal)
        self._newConst = [re.compile(r"x").sub("",m) for m in x1]

        for i in range(len(self._newConst)):
            if self._newConst[i] == '':
                self._newConst[i] = '1'
            if self._newConst[i] == "-":
                self._newConst[i] = "-1"

        for i in range(len(self._newConst)):
            if int(self._newConst[i]) > 0:
                self._newConst[i] = '+'+str(self._newConst[i])
        self._power = re.findall('[\^][-]?[\d$]+',self._poylnomal)
        self._power = [re.compile(r"\^").sub("", m) for m in self._power]
        return self._power

    def derivativePolynomial(self,n=1):
        print('f(x)=',self._poylnomal)
        self.getCoeff()
        self.getPower()
        newPolynomial = []
        newPower = [int(self._power[i])-1 for i in range(len(self._power))]
        newCo = [int(self._coeffi[i])*int(self._power[i]) for i in range(len(self._power))]

        for i in range(1,len(newCo)):
            if newCo[i] > 0:
                newCo[i] = '+'+str(newCo[i])

        for i in range(len(newPower)):
            if newPower[i] == 1:
                newPolynomial.append(str(newCo[i])+'x')
            else:
                newPolynomial.append(str(newCo[i])+'x^'+str(newPower[i]))

        for i in range(len(self._newConst)):
            newPolynomial.append(self._newConst[i])

        if len(newPolynomial) == 0:
            newPolynomial.append('0')
        s = 'f(x)\'='+''.join(newPolynomial)
        return s
de= DePoly(polynomial)
print(de.derivativePolynomial())

#de.getPower()
#de.getCoeff()


'''
import re

def derivative(polynomial):

	coefficient = re.findall(r'-?[\d]*[x$]', polynomial)

	power = re.findall(r'[\^][-]?[\d$]+', polynomial)

	derivative_polynomial = []

	# print coefficient
	# print power

	for i in range(len(coefficient)):
		coef = re.findall(r'[-\d]+',coefficient[i])
		if len(coef) != 0:
			if coef[0]=='-':
				coef[0] = '-1'
			a = int(coef[0])
		else: a=1
		b = 1
		if i < len(power):
			b = int(power[i][1:])
		derivative = a*b

		if b>2:
			end = '^'+str(b-1)
		elif b<0: end = '^' + str(b-1)
		else: end=''

		# print "a: " + str(a)
		# print "b: " + str(b)
		# sys.stdout.softspace=0

		# print("+"*(derivative>0 and i!=0) +str(derivative)+ 'x'*(abs(b-1)>0)+end),
		derivative_polynomial.append("+"*(derivative>0 and i!=0) + str(derivative)+ 'x'*(abs(b-1)>0)+end)
	if len(derivative_polynomial)==0: derivative_polynomial.append('0')
	return "".join(derivative_polynomial)

assert getDerivative("4x+1"),"4"
assert getDerivative("-4x-1"),"-4"
assert getDerivative("x^2+2x+1"),"2x+2"
assert getDerivative("0"),"0"
assert getDerivative("-100"),"0"
assert getDerivative("-x^2+3x+4"),"-2x+3"
assert getDerivative("-x^5-x^4-x^3"),"-5x^4-4x^3-3x^2"
assert getDerivative("10x^9+10x^3+10x"),"90x^8+30x^2+10"
assert getDerivative("100x^5+12x^3-3x-3"),"500x^4+36x^2-3"
assert getDerivative("-1000x^7+200x^4+6x^2+x+1000"),"-7000x^6+800x^3+12x+1"
'''
