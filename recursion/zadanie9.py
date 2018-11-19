from random import randint
import pprint
m = int(input("m: "))
n = int(input("n: "))
matrix = []
for i in range(m):
    matrix.append([])
    for j in range(n):
        matrix[i].append(randint(1,9))
print(matrix)
print(list(map(list, zip(*matrix))), sep = "\n")
