import math
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
delta = (b**2 - (4 * a * c))
print(delta)
if delta > 0:
    x1 = (-b - (delta**1/2)) / (2 * a)
    x2 = (-b - (delta**1/2)) / (2 * a)
    print("x1= " + str(x1) + ", " + "x2= " + str(x2))
elif delta == 0:
    x0 = -b - (2*a)
    print("x0= " + str(x0))
else:
    print("Nie ma miejsc zerowych")  