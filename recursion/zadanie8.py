from random import randint
size = int(input("Wymiar: "))
matrix = []
for i in range(size):
    matrix.append([])
    for j in range(size):
        matrix[i].append(randint(1,9))
print(matrix)
print()
print(list(map(list, zip(*matrix))), sep = "\n")
