def find_NOD(a, b):
    while a!=b:
        if a>b:
            a -= b
        else:
            b -= a
    return a
            


a, b = 18, 24

print(find_NOD(a, b))

