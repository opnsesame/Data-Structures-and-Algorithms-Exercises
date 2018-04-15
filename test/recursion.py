def Mideng(li):
  if(type(li)!=list):
    return
  if(len(li)==1):
    return [li]
  result=[]
  for i in range(0,len(li[:])):
    bak=li[:]
    head=bak.pop(i) #head of the recursive-produced value
    for j in Mideng(bak):
      j.insert(0,head)
      result.append(j)
  return result
def MM(n):
  if(type(n)!=int or n<2):
    return
  return Mideng(list(range(1,n)))
