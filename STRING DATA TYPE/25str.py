#Count uppercase, lowercase, digits, and special characters separately
s=input("enter an string:")
import string
counta=0
countb=0
countc=0
countd=0

a=list(string.ascii_uppercase)
b=list(string.ascii_lowercase)
c=list(string.digits)
d=list(string.punctuation)
for i in s:
    if i in a:
        counta+=1
    elif i in b:
        countb+=1
    elif i in c:
        countc+=1
    elif i in d:
        countd+=1
print("uppercase :",counta)
print("lowercasecase :",countb)
print("digit:",countc)
print("special char :",countd)
