#Remove the element 30 from the tuple (10,20,30,40) without using tuple.remove().
t=(10,20,30,40)
l=[]
l2=[]
for i in t:
    if i!=30:
        l.append(i)
    else:
        l2.append(i)
tu=tuple(l)
print(tu)