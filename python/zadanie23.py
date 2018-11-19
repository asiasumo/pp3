for x in range(1,51):
    if x % 3 == 0 and x % 5 == 0:
        print("BINGO")
    elif x % 5 == 0 or x % 3 == 0:
        if x % 5 == 0:
            print("BAM")
        elif x % 3 == 0 :
            print("BIM")
    else: 
        print(x)
    
