'''Write a program to count how many times each character appears in a string.
Example: "apple"
Output: {'a':1, 'p':2, 'l':1, 'e':1}'''
s="apple"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)