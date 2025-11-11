#Find common elements of two lists
n=int(input("how many elements u want to add in list:"))
l=[]
t=[]
e=[]
new=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
n=int(input("how many elements u want to add in list2:"))
for i in range(1,n+1):
    element=int(input("enter the element:"))
    t.append(element)
for i in l:
    if i in t:
        new.append(i)
for i in new:
    if i not in e:
        e.append(i)
print(e)