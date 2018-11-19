from random import randint
m = int(input("m: "))
n = int(input("n: "))
matrix = []
matrix2 = []
matrix3 = []
for i in range(m):
    matrix.append([])
    for j in range(n):
        matrix[i].append(randint(1,9))
print(*matrix)
for i in range(m):
    matrix2.append([])
    for j in range(n):
        matrix2[i].append(randint(1,9))
print(*matrix2)
for i in range(m):
    matrix3.append([])
    for j in range(n):
        matrix3[i].append(0)
print(matrix3)
for i in range(len(matrix)):
    for j in range(n):
        matrix3[i][j] = matrix[i][j] + matrix2[i][j]
print(matrix3)

    



  
