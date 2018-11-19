def wsp(x,y):
    if x>0 and y>0:
        print("Punkt w pierwszej cwiartce")
    elif x == 0 and y != 0: 
        print("punkt na osi x ")
    elif y == 0 and x != 0:
        print("punkt na osi y")
    elif x<0 and y>0:
        print("punkt w drugiej cwiartce")
    elif x>0 and y<0:
        print("punkt w czwartej cwiartce")
    elif x<0 and y<0:
        print("Punkt w trzeciej cwiartce")
    elif x == 0 and y == 0:
        print("Punkt w poczatku ukladu")
    
wsp(0,0)