#Convert a tuple into a list
n=int(input("how many elements u want to add in tuple:"))
l=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)

t=tuple(l)
print(type(t))