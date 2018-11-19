count = 0
suma = 0
average = 0 
while True:             
    l = int(input("Podaj liczbe: "))
    if l == 0:      
        break 
    suma = suma + l
    count = count + 1
    average = suma / count
print("Suma: " + str(suma) + " Liczb: " + str(count) + " Srednia: " + str(average))
