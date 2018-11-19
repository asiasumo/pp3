limit = int(input("Podaj limit predkosci(km/h): "))
speed = int(input("Podaj predkosc pojazdu(km/h): "))
if speed>limit:
    over = speed - limit
    if over<=10:
        print("Mandat(zł): " + str(over*5))
    elif over>10:
        print("Mandat(zł): " + str((over*15)-100))
else:
    print("Jestes przykladnym kierowca")

        



