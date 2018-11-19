import copy
def det(A):
    return ((A[0][0]*A[1][1]*A[2][2])+(A[1][0]*A[2][1]*A[0][2])+(A[2][0]*A[0][1]*A[1][2]))-((A[0][2]*A[1][1]*A[2][0])+(A[1][2]*A[2][1]*A[0][0])+(A[2][2]*A[0][1]*A[1][0]))
#   return ((x1*y2*z3)+(x2*y3*z1)+(x3*y1*z2))-((z1*y2*x3)+(z2*y3*x1)+(z3*y1*x2))

def Cramer(x1,y1,z1,x2,y2,z2,x3,y3,z3,res1,res2,res3):
    A = [
        [x1,y1,z1],
        [x2,y2,z2],
        [x3,y3,z3]
    ]
    copyA = copy.deepcopy(A)
    d = det(A)
    #print(d)
    if (det(A)) != 0:
        tmp = [0,0,0]
        U = [res1,res2,res3]
        W = [0,0,0]
        for i in range(len(A)):      
            for j in range(len(U)):
                tmp[j] = A[j][i]
                A[j][i] = U[j]
            #print(A)
            W[i] = det(A)/d
            #print(W[i])
            for j in range(len(U)):
                A[j][i] = tmp[j]
        print("Rozwiązanie układu : ")
        print(W)
    else: 
        print("Wyznacznik = 0 ")

Cramer(2,8,-1,3,2,5,9,-6,4,5,4,1)


