size = int(input("Wymiar: "))
matrix = []
for i in range(size):
    matrix.append([])
    for j in range(size):
        matrix[i].append(1 if j == i else 0)
        
print(matrix)

