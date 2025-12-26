#Write a function that checks if a string is palindrome.
def palin(a):
    if a==a[-1::-1]:
        return "given str is palindrome!"
    else:
        return "the given string is not palindrome!"
print(palin("hhhh"))