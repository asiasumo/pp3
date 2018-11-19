def liczba(n):
    reszta = 0   
    wynik = n 
    lista = []
    while True:
        reszta = wynik % 2
        wynik = wynik // 2
        lista.append(reszta)
        if wynik == 1:
            lista.append(1)
            break
    print(str(n) + "(10) = ", end = " "  )
    print(*lista, sep = "", end = "(2)")
    print()
    
liczba(230)
        
   