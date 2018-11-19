from random import randint
m,n = int(input("Podaj m: ")),int(input("Podaj n: "))
p,q = int(input("Podaj p: ")),int(input("Podaj q: "))
print()
A = []
B = []
C = []
if n != p:
    print("Złe wymiary")
else:
    for i in range(m):
        A.append([])
        for j in range(n):
            A[i].append(randint(1,9))
    print("macierz A = ")
    print(*A, sep = "\n")
    print()
    for i in range(p):
        B.append([])
        for j in range(q):
            B[i].append(randint(1,9))
    print("macierz B = ")
    print(*B, sep = "\n")
    for i in range(m):
        C.append([])
        for j in range(q):
            C[i].append(0)
    print("macierz C = ")        
    
    for x in range(m):
        for y in range(q):
            for z in range(n):
                C[x][y] += A[x][z] * B[z][y]
print(*C, sep = "\n")

                