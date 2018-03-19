#Python's random moduel includes a function shuffle(data) that accepts a
#list of element and randomly reorders the elements so that each possible
#order occurs with equal probability.The random module includes a more
#basic function randint(a,b) that returns a uniformly random integer from
#a to b (including both endpoints). Using only the radint function.implement
#your own version of the shuffle function.

import random
#built-in random shuffle function
list = [chr(n) for n in range(97,123)]
print(list)
random.shuffle(list)
print(list)

#User defined shuffle
list = [chr(n) for n in range(97,123)]
def myShuffle(list):
    mShuffle = []
    n = len(list)
    for i in range(n):
        a = random.randint(0,n-i-1)
        mShuffle.append(list[a])
        list.pop(a)
    return(mShuffle)
list = myShuffle(list)
print(list)
