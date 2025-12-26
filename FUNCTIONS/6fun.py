#Write a function that counts the number of vowels in a string.

def count_vowel(str):
    ct_a=0
    ct_e=0
    ct_i=0
    ct_o=0
    ct_u=0
    for i in str:
        if i=="a":
            ct_a+=1
        elif i=="e":
            ct_e+=1
        elif i=="i":
            ct_i+=1
        elif i=="o":
            ct_o+=1
        elif i=="u":
            ct_u+=1
    print("a:",ct_a)
    print("e:",ct_e)
    print("i:",ct_i)
    print("o:",ct_o)
    print("u:",ct_u)
count_vowel("hello")