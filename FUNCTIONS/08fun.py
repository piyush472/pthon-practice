#Given list from 1 to n with one missing:
def find_missing(arr):
    l2=[]
    l3=[]
    a=max(arr)
    b=min(arr)
    
    for i in range(b,a+1):
        l2.append(i)
    for j in l2:
        if j not in arr:
            l3.append(j)
    print("missing element:",l3)


find_missing(arr=[1,2,4,5,6])