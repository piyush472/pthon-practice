#write a python function called calculate_avg that takes a list of no as input and returns the average of those numbers
def calculate_avg(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers)/len(numbers)
num=[1,2,3,4]
avg=(calculate_avg(num))
print(avg)