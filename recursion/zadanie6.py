tab = [2,3,5,2,9,8,1,3,9,1,1,4,7,7,1,4]
tab.sort()
x = len(tab)
if x % 2 == 0:
    half = x//2
    var = (tab[half] + tab[half-1]) / 2
    print("Srednia: " + str(var))
else: 
    half = x//2  
dom = {}
for i in tab:
    if i in dom: 
        dom[i] += 1
    else:
        dom[i] = 1
numb = 1
for i in dom:
    if dom[i] > dom[numb]: 
        numb = i

print("Dominanta: " + str(numb))

def aver(n):
    tab.sort()
    x = len(tab)
    if x % 2 == 0:
        half = x//2
        var = (tab[half] + tab[half-1]) / 2
        print("Srednia: " + str(var))
    else: 
        half = x//2  
aver(tab)

def dom(n):
    dom = {}
    for i in tab:
        if i in dom: 
            dom[i] += 1
        else:
            dom[i] = 1
    numb = 1
    for i in dom:
        if dom[i] > dom[numb]: 
            numb = i
    print("Dominanta: " + str(numb))
dom(tab)

 

    

