#Largest element in nested list
a=[]
nested_list = [[12, 7, 3], [4, 18], [6, 2, 9]]
for i in nested_list:
    for j in i:
        a.append(j)
print(max(a))