file = open("NoEducation.txt","r")
lines = file.readlines()
for x, line in enumerate(lines):
    print(x+1,line)
file.close()