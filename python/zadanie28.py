x = 7 
prawda = True
while True:
    prawda = True
    for y in range(2,7):
        if x % y != 1:
            prawda = False
            x += 7
            break
     #if x % 2 == 1 and x % 3 == 1 and x % 4 == 1 and x % 5 == 1 and x % 6 == 1:
        #print(x) 
        #break
    if prawda:
        print(x)
        break
