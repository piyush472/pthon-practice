#Given a tuple of tuples ((1,2,3),(4,5,6),(7,8,9)), print the sum of each inner tuple.
t=((1,2,3),(4,5,6),(7,8,9))
for i in t:
    print(sum(i))