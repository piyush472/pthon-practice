#Return number of vowels in string.
def count_vowels(s):
    count=0
    for i in s:
        if i in "aeiou":
            count+=1
    print("no of vowel:",count)



str=input("enter an string:")

count_vowels(str)