import los
from collections import Counter
Odd = 0
Even = 0
for y in range(1,1001):
    s = los.Losuj()
    if s % 2 == 0:
        Even += 1
    else:
        Odd += 1

O = (Odd/1000)*100
E = (Even/1000)*100

print("Liczby parzyste: " + str(E) + "%")
print("Liczby nieparzyste: " + str(O) + "%")

