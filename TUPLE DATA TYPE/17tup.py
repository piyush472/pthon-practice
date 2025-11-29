#Find elements that appear in both tuples: (1,2,3,4) & (3,4,5,6).
t=(1,2,3,4)
t2=(3,4,5,6)
for i in t:
    if i in t2:
        print(i)