#Return a New List with Distinct Elements from a List
def dis_ele(element):
    l2=[]
    for i in element:
        if i not in l2:
            l2.append(i)
    return l2

no=[1,1,1,1,1,1]
print(dis_ele(no))