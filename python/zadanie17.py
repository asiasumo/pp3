sum1 = 0
sum2 = 0
for x in range(1,51):
    if x % 2 == 0:
        sum1 = sum1 + x
    elif x % 2 != 0:
        sum2 = sum2 + x
print("Suma liczb parzystych wynosi: " + str(sum1))
print("Suma liczb nieparzystych wynosi: " + str(sum2))
        

        