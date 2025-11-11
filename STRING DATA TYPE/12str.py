#Check if a string is palindrome (same forward/backward
s=input("enter an string:")
if s==s[-1::-1]:
    print("yes str is palindrome")
else:
    print("str is not palindrome")