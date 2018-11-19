proba = 0
while True:
    pytaj = input("Podaj PIN: ")
    proba = proba + 1
    if proba == 3 and pytaj!= "0507":
        print("Karta platnicza zostaje zablokowana.")
        break
    elif pytaj == "0507":
        print("Transakcja zaakceptowana")


    
