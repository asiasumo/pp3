import random 
rzut = 0 
suma = 0
while True:
    rzut = rzut + 1
    if rzut>6:
        break
    y = random.randint(1,7) 
    suma = suma + y
print(str(suma))



