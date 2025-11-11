#Find the index of an element in a tuple
n=int(input("how many elements u want to add in tuple:"))
l=[]

for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
idx=int(input("ener the element u want index:"))
t=tuple(l)
print("index of",idx,":",t.index(idx))