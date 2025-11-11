#Remove all digits from a string
s=input("enter an string:")
r="1234567890"
e=""
for ch in s:
    if ch not in r:
      e+=ch  
print(e)