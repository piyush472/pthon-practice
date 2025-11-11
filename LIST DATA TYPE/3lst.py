#Count how many times an item appears in list
n=int(input("how many elements u want to add in list:"))
l=[]

for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
im=int(input("enter the item want to count :"))
print(l.count(im))