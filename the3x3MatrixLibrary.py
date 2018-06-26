import sys
def PrintMatrix(message,matrix):
    print(message)
    for x in range(3):
        print(matrix[x])

def ModifyMatU(m,Mat,i1,i2):
    for x in range(3):
        Mat[i1][x] += (m*Mat[i2][x])

def GenerateMat(a):
    for i in range(3):
        a.append([0]*3)
print("This is a program that deals with 3x3 matrices")
    
def Inv(message):
    print(message)
    MatA = []
    GenerateMat(MatA)
    for i in range(3):
        for j in range(3):
            MatA[i][j] = float(input("What is your a"+str(i+1)+str(j+1)+"?"))
    print("\nThis is your matrix") 
    for x in range(0,3):
        print(MatA[x])

    det1 = MatA[0][0] * ((MatA[1][1]*MatA[2][2])-(MatA[1][2]*MatA[2][1]))
    det2 = MatA[0][1] * ((MatA[1][0]*MatA[2][2])-(MatA[1][2]*MatA[2][0]))
    det3 = MatA[0][2] * ((MatA[1][0]*MatA[2][1])-(MatA[1][1]*MatA[2][0]))
    detA = det1 - det2 + det3
    print("\nDeterminant:",detA)

    if detA ==0:
        print("Matrix is singular")
    else:
        MatB = [[((MatA[1][1]*MatA[2][2]) - (MatA[1][2] * MatA[2][1]))/detA,((MatA[2][1]*MatA[0][2]) - (MatA[2][2] * MatA[0][1]))/detA,((MatA[0][1]*MatA[1][2]) - (MatA[0][2] * MatA[1][1]))/detA],
                [((MatA[1][2]*MatA[2][0]) - (MatA[1][0] * MatA[2][2]))/detA,((MatA[0][0]*MatA[2][2]) - (MatA[2][0] * MatA[0][2]))/detA,((MatA[0][2]*MatA[1][0]) - (MatA[0][0] * MatA[1][2]))/detA],
                [((MatA[1][0]*MatA[2][1]) - (MatA[1][1] * MatA[2][0]))/detA,((MatA[2][0]*MatA[0][1]) - (MatA[2][1] * MatA[0][0]))/detA,((MatA[0][0]*MatA[1][1]) - (MatA[0][1] * MatA[1][0]))/detA]]

        PrintMatrix("\nThis is the inverse matrix",MatB)


def Simul():
    print("We will start with the coefficients")
    MatS = Inv("Please enter coefficient of each entry for the simulataneous equations")
    mat = [0,0,0]
    for i in range(3):
        mat[i] = float(input("Please give three values the equations are equal to:"))
    print("This is your Matrix")
    for i in range(3):
        print(mat[i])
    
    matg = [0,0,0]
    matg[0] = mat[0]*MatS[0][0] + mat[1]*MatS[0][1] + mat[2]*MatS[0][2]  
    matg[1] = mat[0]*MatS[1][0] + mat[1]*MatS[1][1] + mat[2]*MatS[1][2]
    matg[2] = mat[0]*MatS[2][0] + mat[1]*MatS[2][1] + mat[2]*MatS[2][2]
    print("These are the solutions:")
    print(str(matg[0]) + "=x")
    print(str(matg[1]) + "=y")
    print(str(matg[2]) + "=z")
    
def LUdecomp():
    print("First, we can start with the values of the matrix:")
    MatA = []
    MatL = []
    MatU = []
    GenerateMat(MatA)
    GenerateMat(MatL)
    GenerateMat(MatU)
    for i in range(3):
        for j in range(3):
            MatA[i][j] = float(input("What is your a"+str(i+1)+str(j+1)+"?"))
            MatU[i][j] = MatA[i][j]
    print("\nThis is your matrix") 
    for x in range(0,3):
        print(MatA[x])

    m1 = MatU[1][0] / (-1*MatU[0][0])
    
    ModifyMatU(m1,MatU,1,0)
    
    m2 = MatU[2][0]/(-1*MatU[0][0])
    
    ModifyMatU(m2,MatU,2,0)
    
    m3 = MatU[2][1] / (-1*MatU[1][1])
    
    ModifyMatU(m3,MatU,2,1)
    
    MatL[1][0] = -1*m1
    MatL[2][0] = -1*m2
    MatL[2][1] = -1*m3
    MatL[0][0] = 1
    MatL[1][1] = 1
    MatL[2][2] = 1
    PrintMatrix("\nThis is the L matrix",MatL)
    PrintMatrix("\nThis is the U matrix",MatU)


                       
def theFunk():
    choiceA = int(input("Please choose what you'd like to do:\n1:Inverse 2:LU decomposition 3:Simultaneous Equations(3 values)"))
    
    if choiceA == 1:
        Inv("First, we can start with the values of the matrix:")
    elif choiceA == 2:
        LUdecomp()
    elif choiceA == 3:
        Simul()
        
    choiceB = int(input("Please choose whether you'd like to carry on:\n1:Yes 2:No"))
    
    if choiceB == 1:
        theFunk()
    elif choiceB ==2:
        sys.exit()
