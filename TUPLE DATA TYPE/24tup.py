#Write a program to check whether all items in the tuple are the same.
t = (1,1,1,1,3)

if t.count(t[0]) == len(t):
    print("Yes, all elements are the same")
else:
    print("No, all elements are not the same")
