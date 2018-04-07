'''
Write a Python program to simulate an ecosystem containing two types
of creatures, bears and fish. The ecosystem consists of a river, which is
modeled as a relatively large list. Each element of the list should be a
Bear object, a Fish object, or None. In each time step, based on a random
process, each animal either attempts to move into an adjacent list location
or stay where it is. If two animals of the same type are about to collide in
the same cell, then they stay where they are, but they create a new instance
of that type of animal, which is placed in a random empty (i.e., previously
None) location in the list. If a bear and a fish collide, however, then the
fish dies (i.e., it disappears).
'''
import random
import time
START = 0
RIVERSIZE = 50

class River():
    def __init__(self,river):
        self.__riverSize__ = river
        self.__river__ = []
        self.__riverNew__ = [None]*river
        self.__riverEmpty__ = []
        self.poisiton = 0
        self.__bear__ = 0
        self.__fish__ =0
        for i in range(river):
            if i%5 == 0:
                r = random.randint(0, 2)
                if  r==0:
                    self.__river__.append(None)
                    self.__riverEmpty__.append(i)
#                    print('River')
                if  r == 1:
                    self.__river__.append(Fish())
                    self.__fish__ += 1
#                    print('Fish created')
                if  r ==2:
                    self.__river__.append(Bear())
                    self.__bear__ += 1
#                    print('Bear created')
            else:
                    self.__river__.append(None)
                    self.__riverEmpty__.append(i)
#                    print('River')
#            self.__riverNew__ =   self.__river__
        print('{}Bear created and {}Fish created'.format(self.__bear__,self.__fish__))
    def getContent(self,poisition):
        self.poisition = poisition
        '''
        if type(self.__river__[self.poisition]) == None:
            print('Nothing there')
        if type(self.__river__[self.poisition]) == Fish:
            print('There is a Fish')
        if type(self.__river__[self.poisition]) == Bear:
            print('There is a Bear')
        '''
        return self.__river__[self.poisition]

    def updateRiver(self,originalP,newP):
        '''
        if self.__bear__ == len(self.__river__):
            print('River full of  bear , Game Over, Exit 1')
            exit()
        '''
        #print('The river has {} Bears and {} Fishs'.format(self.__bear__,self.__fish__))
        if self.__bear__ == len(self.__river__):
            print('River full of  bear , Game Over, Exit 2')
            print(self.__str__())
            exit()
        if self.__fish__ == len(self.__river__):
            print('River full of  fish , Game Over, Exit 3')
            print(self.__str__())
            exit()
        if self.__fish__ == 1 and self.__bear__ == 0:
            print('There is only 1 fish in the river , unable to reproduce , Game Over, Exit 3')
            print(self.__str__())
            exit()
            exit()
        if self.__bear__ == 1 and self.__fish__ == 0:
            print('There is only 1 bear in the river , unable to reproduce , Game Over, Exit 4')
            print(self.__str__())
            exit()            
        #print('old poisition{};new poisition{}'.format(originalP,newP))
        #print(type(self.__river__[newP]),'---------',type(self.__river__[originalP]))
        #print('---------------------------------------------------------------')
        if  originalP > newP:
            if self.__river__[newP] == None:
                self.__river__[newP],self.__river__[originalP] = self.__river__[originalP],self.__river__[newP]
                print(self.__str__(),type(self.__river__[newP]),'{} Moved <--------to Left {}'.format(originalP,newP))

            if  type(self.__river__[newP]) == type(self.__river__[originalP]):#

                l =[]
                for i in range(len(self.__river__)):
                    '''
                    f,b=0,0
                    if type(self.__river__[i]) == Fish:
                        f += 1
                    if type(self.__river__[i]) == Bear:
                        b += 1
                        if b == len(self.__river__):
                            print('River full of Bear , Game Over!',str(b))
                            exit()
                    '''
                    if self.__river__[i] == None:
                        l.append(i)
                print(l)
                '''
                if len(l) == 0:
                    print('There is no space for  Bear to reproduce, Game Over!',str(self.__bear__),'---------------',str(self.__fish__))
                '''
                if len(l) != 0:
                    r = random.randint(0,len(l)-1)
                    if type(self.__river__[newP])  == Fish:
                        self.__river__[l[r]] = Fish()
                        self.__fish__ += 1
                        print(self.__str__(),'Fish meet Fish,New Fish born @',l[r])
                    if type(self.__river__[newP])  == Bear:
                        self.__river__[l[r]] = Bear()
                        self.__bear__ += 1
                        print(self.__str__(),'Bear meet Bear,New Bear born @',l[r])

            if  (type(self.__river__[newP]) == Fish and type(self.__river__[originalP]) == Bear):
                self.__river__[newP] = self.__river__[originalP]
                self.__river__[originalP] = None
                self.__fish__ -= 1
                print(self.__str__(),'Bear Catch Fish,Fish Die! There is {} fish left'.format(self.__fish__))
            if type(self.__river__[newP]) == Bear and type(self.__river__[originalP]) == Fish:
                #print('Fish Goto Bear and Die! There is {} fish left'.format(self.__fish__))
                #self.__river__[newP] = self.__river__[newP]
                self.__river__[originalP] = None
                self.__fish__ -= 1
                print(self.__str__(),'Fish Goto Bear and Die! There is {} fish left'.format(self.__fish__))

        if  originalP < newP:
            if self.__river__[newP] == None:
                self.__river__[newP],self.__river__[originalP] = self.__river__[originalP],self.__river__[newP]
                print(self.__str__(),type(self.__river__[newP]),'{} Moved --------> to Right {}'.format(originalP,newP))                
            if type(self.__river__[newP]) == type(self.__river__[originalP]):
                l =[]
                for i in range(len(self.__river__)):
                    if self.__river__[i] == None:
                        l.append(i)
                print(l)
                if len(l) != 0:
                    r = random.randint(0,len(l)-1)
                    if type(self.__river__[newP])  == Fish:
                        self.__river__[l[r]] = Fish()
                        self.__fish__ += 1
                        print(self.__str__(),'Fish meet Fish,New Fish born @',l[r])
                    if type(self.__river__[newP])  == Bear:
                        self.__river__[l[r]] = Bear()
                        self.__bear__ += 1
                        print(self.__str__(),'Bear meet Bear,New Bear born @',l[r])

            if type(self.__river__[newP]) == Fish and  type(self.__river__[originalP]) == Bear:
                #print('Bear Catch Fish,Fish Die!')
                self.__river__[newP] = self.__river__[originalP]
                self.__river__[originalP] = None
                self.__fish__ -= 1
                print(self.__str__(),'Fish Goto Bear and Die! There is {} fish left'.format(self.__fish__))
            if type(self.__river__[newP]) == Bear and  type(self.__river__[originalP]) == Fish:
                #print('Fish Goto Bear and Die!')
                #self.__river__[newP] = self.__river__[newP]
                self.__river__[originalP] = None
                self.__fish__ -= 1
                print(self.__str__(),'Fish Goto Bear and Die! There is {} fish left'.format(self.__fish__))

        if originalP == newP:
            pass

        #self.__riverNew__[newP] = self.__river__[originalP]
        #if self.__river__[originalP+1] == None:
            #self.__river__[newP],self.__river__[originalP] = self.__river__[originalP],self.__river__[newP]
        #print('River updated')

        #print(self.__river__)

    def __str__(self):
        s = ''
        s1=''
        for i in range(len(self.__river__)):
            if self.__riverNew__[i] == None:
                s1 += '0'
            if type(self.__riverNew__[i]) == Fish:
                s1 +='F'
            if type(self.__riverNew__[i]) ==Bear:
                s1 +='B'
        for i in range(len(self.__river__)):
            if self.__river__[i] == None:
                s += '0'
            if type(self.__river__[i]) == Fish:
                s +='F'
            if type(self.__river__[i]) ==Bear:
                s +='B'
        return '['+s+']'

class Bear():
    def __init__(self):
        self.__poisition__ = 0
        self.__newP__ = 0
#        print('Bear Created at :' +str(self.__poisition__))

    def move(self,poisition):
        self.__poisition__ = poisition
        r = random.randint(0, 2)
        if r == 1:
            #print('Bear didnt move')
            river.updateRiver(self.__poisition__,self.__poisition__)
        if r ==0:
            if self.__poisition__>=1:
                self.__newP__ =  self.__poisition__-1
                #print('Bear Moved <--------Left')
                river.updateRiver(self.__poisition__,self.__newP__)
        if r ==2:
            if self.__poisition__ <= RIVERSIZE-2:
                self.__newP__ =  self.__poisition__+1
                #print('Bear Moved -------->Right')
            #print('old poisition{};new poisition{}'.format(self.__poisition__,self.__newP__))
                river.updateRiver(self.__poisition__,self.__newP__)

class Fish():
    def __init__(self):
        self.__poisition__ = 0
        self.__newP__ = 0
#        print('Fish Created at :' +str(self.__poisition__))

    def move(self,poisition):
        self.__poisition__ = poisition
        r = random.randint(0, 2)
        if r ==1:
            pass
            #print('Fish didnt move')
            #river.updateRiver(self.__poisition__,self.__poisition__)
        if r == 0:
            if self.__poisition__>=1:
                    self.__newP__ =  self.__poisition__-1
                    #print('Fish Moved <--------Left')
                    river.updateRiver(self.__poisition__,self.__newP__)
        if r ==2:
            if self.__poisition__ <= RIVERSIZE-2:
                self.__newP__ =  self.__poisition__+1
                #print('Fish Moved -------->Right')
        #print('old poisition{};new poisition{}'.format(self.__poisition__,self.__newP__))
                river.updateRiver(self.__poisition__,self.__newP__)


river = River(RIVERSIZE)

print(river)
while 1:
    for i in range(RIVERSIZE):
        #print(river.getContent(i))
        if type(river.getContent(i))==Fish:
            #print('Fish @{}'.format(i))
            river.getContent(i).move(i)
        if type(river.getContent(i))==Bear:
            #print('Bear @{}'.format(i))
            river.getContent(i).move(i)

    print(river)
