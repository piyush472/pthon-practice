#Take 5 elements from user and store in a list
n=int(input("how many elements u want to add in list:"))
l=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
print(l)