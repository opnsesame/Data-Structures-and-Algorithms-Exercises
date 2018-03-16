#Write a short Python function, is_even(k),that taks an integervalue
#and returns True if k i even, and False outherwise, However,your
#function cannot use the multiplication, modulo,or division operators.
def is_even(k):
    if k&1 == 0:
        print('k is even number')
    else:
        print('k is not even number')
        
        
k = int(input('please input a number:'))
is_even(k)