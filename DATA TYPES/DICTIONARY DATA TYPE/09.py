#Check if a key "age" exists in:
person = {"name": "Piyush", "age": "Gurgaon"}
l=[]
for k in person.keys():
    l.append(k)
if "age" in l:
    print("key exists!")
else:
    print("keys not exists!")