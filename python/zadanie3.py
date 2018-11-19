dzielna = input("Podaj dzielna: ")
dzielnik = input("Podaj dzielnik: ")
try:
    x=int(dzielna)/int(dzielnik)
except ZeroDivisionError:
    print("Dzielenie przez 0 niedozwolone") 
print(str(dzielna) + "/" + str(dzielnik) + "=" + str(round(x,2)))