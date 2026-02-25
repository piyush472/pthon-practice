'''Create a dictionary from two lists:

keys = ["name", "age", "city"]
values = ["Piyush", 21, "Delhi"]'''
idx=0
s={}
keys = ["name", "age", "city"]
values = ["Piyush", 21, "Delhi"]
for i in keys:
    
    s[i]=values[idx]
    idx+=1

    
print(s)
