file = open("potega.txt","w")
for x in range(1,11):
    double = x**2
    cube = x**3
    file.write(f'{x:2} {double:3} {cube:4}' + "\n")
    

