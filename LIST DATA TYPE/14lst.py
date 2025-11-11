#Remove duplicates from a list
n=int(input("how many elements u want to add in list:"))
a=[]
l=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
for j in l:
    if j not in a:
        a.append(j)
print(a)
