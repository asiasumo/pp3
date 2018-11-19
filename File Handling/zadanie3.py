file = open("NoEducation.txt","r")
lines = file.readlines()
print(lines[1],lines[2], sep = "")
file.close()