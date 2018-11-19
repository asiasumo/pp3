wiek = (int(input("Podaj swoj wiek: ")))
if wiek < 18:
    print("Jestes nieletni")
elif wiek >= 18 and wiek <= 120:
    print("Jestes dorosly")
else:
    print("Nie zyjesz, sorki")