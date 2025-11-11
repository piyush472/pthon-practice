#Copy one list into another list
n=int(input("how many elements u want to add in list:"))
l=[]
l2=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
for j in l:
    l2.append(j)
print(l2)