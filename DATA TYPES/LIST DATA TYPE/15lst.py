#Identify even and odd numbers separately
n=int(input("how many elements u want to add in list:"))
e=[]
o=[]
l=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
for j in l:
    if j%2==0:
        e.append(j)
    else:
        o.append(j)
print('even lsit',e)
print('odd lsit',o)