#Check if a number exists in list or not.
n=int(input("how many elements u want to add in list:"))
l=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
no=int(input("enter the no u want to search in list"))
if no in l:
    print("yes",no,"is in list")
else:
    print("no no is not in list")