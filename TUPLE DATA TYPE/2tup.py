#2️⃣ Check if a given value exists in a tuple
n=int(input("how many elements u want to add in tuple:"))
l=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
t=tuple(l)
e=int(input("enter the element u want to check in tuple:"))
if e in t:
    print("element found in tuple!")
else:
    print("element not found in tuple!")