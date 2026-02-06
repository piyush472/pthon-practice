#Find sum of all elements (without sum())
l=[]
sum=0
n=int(input("how many elements u want to add in list:"))
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
for j in l:
    sum+=j
print(sum)