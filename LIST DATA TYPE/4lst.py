#Reverse the list without using reverse()
l=[]
n=int(input("how many elements u want to add in list:"))
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
l.reverse()
print(l)