#Program to check list is palindrome
n=int(input("how many elements u want to add in list:"))
l=[]
for i in range(1,n+1):
    element=int(input("enter the element:"))
    l.append(element)
if l==l[-1::-1]:
    print('list is palindrome')
else:
    print('list is not palindrome')
