#Replace vowels with *
s=input("enter an string:")
r="aeiouAEIOU"
e=""
for i in s:
   if i not in r:
      e+=i
   else:
      e+="*"
print(e )