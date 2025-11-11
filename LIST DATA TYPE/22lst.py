#Find unique elements (appear only once).
n=int(input("how many elements u want to add in list:"))
new=[]
l=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
for i in l:
    if i not in new:
        new.append(i)
print(new)