#Given a tuple (10,20,30,20,40,20), print all indices where 20 appears.
t=(10,20,30,20,40,20)
s=0
for i in t:
    s+=1

    if i==20:
        print(s-1)