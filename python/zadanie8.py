pesel = input("Podaj pesel: ")
print(str("Data urodzenia: " + pesel[0:2])+ "/" + str(pesel[2:4]) + "/" + (pesel[4:6]))
if int(pesel[-2])%2 == 0:
    print("Plec: kobieta")
else: 
    print("Plec: mezczyzna")