x = input("Podaj pierwsza liczba: ")
y = input("Podaj druga liczba: ")
z = input("Podaj trzecia liczba: ")
if x>y and x<z or x<y and x>z:
    print("Mediana wynosi: " + str(x))
elif y>x and y<z or y<x and y>z:
    print("Mediana wynosi: " + str(y))
else: 
    print("Mediana wynosi: " + str(z))
