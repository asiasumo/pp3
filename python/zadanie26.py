a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b :"))

for x in range(a):
    if x ==0 or x == a-1:
        print("*" * b)
    else: 
        print("{}{}{}".format("*" , " " * (b - 2) , "*" ))
