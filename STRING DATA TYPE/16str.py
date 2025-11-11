#Check if all characters are alphabetic
import string
l=[]
t=[]
s=input("enter an string:")
a=list(string.ascii_lowercase)
b=list(string.ascii_uppercase)
c=a+b
for i in s:
    if i not in c:
      t.append(i)
    else:
       l.append(i)
if len(t)>0:
   print("str all char are not alphabetic")
else:
   print("all cahr are aplha")