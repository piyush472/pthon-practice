#Count vowels (a, e, i, o, u) in a string
s=input("enter an string:")
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
for i in s:
    if i=="a":
        count_a+=1
    elif i=="e":
        count_e+=1
    elif i=="i":
        count_i+=1
    elif i=="o":
        count_o+=1
    elif i=="u":
        count_u+=1
print("count of vowel a:",count_a)
print("count of vowel e:",count_e)
print("count of vowel i:",count_i)
print("count of vowel o:",count_o)
print("count of vowel u:",count_u)