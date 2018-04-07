'''
The collections.Sequence abstract base class does not provide support for
comparing two sequences to each other. Modify our Sequence class from
Code Fragment 2.14 to include a definition for the __eq__ method, so
that expression seq1 == seq2 will return True precisely when the two
sequences are element by element equivalent.
'''
from abc import ABCMeta,abstractmethod

class Sequence(metaclass = ABCMeta):

    @abstractmethod
    def __len__(self):
        ''''''
    @abstractmethod
    def __getitem__(self,j):
        ''''''
    def __contains__(self,val):
        for j in range(len(self)):
            if self[j] == val:
                return True
            return False

    def __eq__(self,other):
        if len(self) == len(other):
            for i in range(len(self)):
                if self[i] != other[i]:
                    return False
            return True
        else:
            return False

    def __lt__(self,other):
        for i in range(len(self)):
            if self[i] < other[i]:
                return True
        return False


    def index(self,val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self,val):
        k = 0
        for j in range(len(self)):
            
            if self[j] == val:
                k += 1
        return k

class Seq(Sequence):
    def __init__(self,s):
        self._s  = s

    def __len__(self):
        return len(self._s)

    def __getitem__(self,n):
        return self._s[n]
