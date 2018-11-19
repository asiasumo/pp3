file = open("NoEducation.txt","r")
lines = file.readlines()
for line in lines:
    l = len(line)
    print(l,line)
file.close()
