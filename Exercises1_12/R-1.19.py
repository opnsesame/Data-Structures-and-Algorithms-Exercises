#Demonstrate how to use Python's list comprehension syntax to produce
#the list ['a','b','c',...'z'],but without having to type all 26 such
#chaaracters literally.

list = [chr(n) for n in range(97,122)]
print(list)
