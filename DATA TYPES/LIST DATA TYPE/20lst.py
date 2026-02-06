#Create a new list from squares of only even numbers
n=int(input("how many elements u want to add in list:"))
l=[]
t=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
for j in l:
    if j%2==0:
        t.append(j*j)
print(t)