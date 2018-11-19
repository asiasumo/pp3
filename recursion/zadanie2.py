from random import randint 
tab1 = [randint(1,2000) for _ in range(2)]
tab2 = [randint(1,2000) for _ in range(2)]
tab3 = []
sum_ = 0
for i in range(len(tab1)):
    sum_ += (tab1[i] + tab2[i])
    tab3.append(sum_)
print(*tab1)
print()
print(*tab2)
print()
print(*tab3)

