#Count positive, negative numbers in list
n=int(input("how many elements u want to add in list:"))
l=[]
posicount=0
negacount=0
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
for j in l:
    if j<0:
        negacount+=1
    elif j>0:
        posicount+=1
print('positive co in list:',posicount)
print('negative co in list:',negacount)