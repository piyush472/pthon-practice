#Multiply All Numbers in a List
def mul_lst(list):
    no=1
    if len(list)==0:
        return 0
    else:
        for i in list:
            no*=i
    return no
num=[1,2,3]
multiply=(mul_lst(num))   
print(multiply)         