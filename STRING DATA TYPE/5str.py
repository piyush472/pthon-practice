#Count how many times "a" appears in a string
ct_a=0
s=input("enter an string:")
for i in s:
    if i=="a":
        ct_a+=1
print(ct_a)