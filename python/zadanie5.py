login = (str(input("Podaj login: ")))
haslo = (str(input("podaj haslo: ")))
while login != "marek" and haslo != "m-123":
   print("Podales zle dane")
   break
else:
    print("Zostales zalogowany")
