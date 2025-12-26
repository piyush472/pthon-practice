#Write a function that returns the largest of three numbers.
def find_lrg(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(find_lrg(5, 2, 3))
