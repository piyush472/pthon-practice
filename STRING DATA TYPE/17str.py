#Remove special characters like @, #, $, %, !
s=input("enter an string:")
r="@!#$%"
e=""
for i in s:
    if i not in r:
        e+=i
print(e)
