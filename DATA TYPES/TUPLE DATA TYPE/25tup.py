#Given two tuples (1,2,3) and (4,5), create all possible pair combinations.
t1 = (1,2,3)
t2 = (4,5)

pairs = []

for i in t1:
    for j in t2:
        pairs.append((i, j))

print(pairs)
