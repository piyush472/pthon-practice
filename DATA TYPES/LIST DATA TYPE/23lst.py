#Rotate list by k positions right.
n=int(input("how many elements u want to add in list:"))
l=[]
t=[]
s=[]


for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
k=int(input('enter the position:'))
for i in range(l[0],l[k+1]):
    t.append(i)
for i in range(l[k+1],l[-1]+1):
    s.append(i)
print(s+t)