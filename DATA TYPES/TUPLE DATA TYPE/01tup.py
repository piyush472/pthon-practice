#Create a tuple with 5 numbers. Print the first and last element
n=int(input("how many elements u want to add in tuple:"))
l=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)

t=tuple(l)
print(t)
print('first element:',t[0])
print('last element:',t[-1])
