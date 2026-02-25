#Write a program to find the key with the maximum value in a dictionary.
dic={1:12,2:112,3:162,4:132,5:1,6:120,7:112,}
l=[]
for i in dic.values():
    l.append(i)
tar=max(l)
for key,val in dic.items():
    if val==tar:
        print(key)
