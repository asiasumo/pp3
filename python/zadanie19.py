def silnia(n):
    if n>1:
        return n * silnia(n-1)
    elif n in (0,1):
        return 1 

for x in reversed(range(1, 11)):
    print("{}! = {}".format(x, silnia(x)))