file = open("liczby.txt","r")
lines = file.readlines()
var = 0 
for x in lines:
    var += int(x)
print(var)

