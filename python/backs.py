import random
def Run():
    tab = []
    for x in range(1,5):
        tab.append(random.randint(0,255))
    print(*tab, sep = ".")
Run()

