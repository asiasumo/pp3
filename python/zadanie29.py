ciag = [0,1]
for x in range(2,51):
    ciag.append(ciag[x - 2] + ciag[x-1])
for x in ciag:
    print(x, end = " ")
    