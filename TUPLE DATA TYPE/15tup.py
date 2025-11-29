#Convert a nested tuple ((1,2),(3,4)) into a flat tuple (1,2,3,4).
t=((1,2),(3,4))
l=[]
for i in t:
    for j in i:
        l.append(j)
tu=tuple(l)
print(tu)