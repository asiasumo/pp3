x1,y1 = int(input("Podaj x1: ")),int(input("Podaj y1: "))
x2,y2 = int(input("Podaj x2: ")),int(input("Podaj y2: "))
x3,y3 = int(input("Podaj x3: ")),int(input("Podaj y3: "))
matrix = [
     [x1,y1,1],
     [x2,y2,1],
     [x3,y3,1]
]
print(*matrix, sep = "\n")
determinant = ((x1*y2)+(x2*y3)+(x3*y1)) - ((y2*x3)+(y3*x1)+(y1*x2))
if determinant == 0:
     print("Punkty ABC są współliniowe")
else: 
     print("Punkty ABC nie są współliniowe")

        


