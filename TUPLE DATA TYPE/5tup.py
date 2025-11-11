#Count occurrences of an element in a tuple
n=int(input("how many elements u want to add in tuple:"))
l=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)

t=tuple(l)
c=int(input("enter an elemnt u want to count occourence of:"))
print(t.count(c))