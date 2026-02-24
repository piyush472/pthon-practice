#Create a dictionary to store a student's name, age, and course. Print the dictionary.
d={}
for i in range(1,4):
    key=input("enter key:")
    val=input("enter value:")
    d[key]=val
print(d)