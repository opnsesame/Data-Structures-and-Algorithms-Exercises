#Write a short program that takes as input three integers,a,b,and c,from
#the console and determines if they can be used in a correct arithmetic
#formula (in the given order),like"a+b=c," "a=b-c,"v "a*b=c."
takeIn = input("Please input 3 numbers ,separate by ','")
s = takeIn.split(',')
a = int(s[0])
b = int(s[1])
c = int(s[2])
if a + b == c:
    print("a + b = c")
if a == b - c:
    print("a = b - c")
if a * b == c:
    print("a * b == c")
