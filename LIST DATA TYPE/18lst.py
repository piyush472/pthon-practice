#Swap first and last element
n=int(input("how many elements u want to add in list:"))
l=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
a=len(l)
l[0],l[a-1]=l[a-1],l[0]
print(l)