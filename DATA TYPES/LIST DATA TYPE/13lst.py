#Merge two lists into one (no + operator
n=int(input("how many elements u want to add in list1:"))
l=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
n=int(input("how many elements u want to add in list2:"))
l2=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l2.append(element)
print('list1',l)
print('list2',l2)
for j in l2:
    l.append(j)
print('combined list',l)