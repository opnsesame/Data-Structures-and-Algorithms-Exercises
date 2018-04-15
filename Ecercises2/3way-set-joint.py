a = [1,2,3,4,5,6,7,8,9,10]
b = [4,9,10,15,8,12,19,18,17,16,1,1]
c = [7,19,32,9,6,4,12]

def findJoints(a,b,c):
    i,j,k= 0,0,0
    tmp =[]
    for num in a:
        for num1 in b:
            if num == num1:
#            print('find joint number!',str(num))
                tmp.append(num)
    print(tmp)
    for num in c:
        for num1 in tmp:
            if num == num1:
                print('find joint number!',str(num))

findJoints(a,b,c)
#time complexility O(n^2)

b.sort()
print(b)
