a = [1,2,3]
b = [1,2,3]
def check(x,y):
    if len(x) == len(y):
        for i in range(len(x)):
            if (x[i] == y[i]):
                return True
    else: 
        return False
print(check(a,b)) 