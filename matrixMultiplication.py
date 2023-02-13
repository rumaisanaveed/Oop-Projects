def inputMatrix():
    noOfRows = int(input("Enter the number of rows :"))
    noOfCols = int(input("Enter the number of columns:"))
    matrix = []
    for rows in range(noOfCols):
        rows = []
        for columns in range(noOfRows):
            n = eval(input("Enter the number of elements one by one:"))
            rows.append(n)
        matrix.append(rows)

    return matrix


def matrixMultiplication(m1,m2):
        answer = []
        for i in range(len(m1)):
            r = []
            for j in range(len(m2[0])):
                p = 0
                for k in range(len(m2)):
                   p += m1[i][k] * m2[k][j]
                r.append(p)
            answer.append(r)

        return answer

          
def printMatrix(m):
    for i in m:
        for j in i:
            print(j,end = "\t")
        print()


A = inputMatrix()
B = inputMatrix()
if len(A) == len(B[0]):
     result = matrixMultiplication(A,B)
     print("Product of matrices A and B")
     finalMatrix = printMatrix(result)
else:
    print("Matrix multiplication is not possible.")

#ADDITION OF MATRICES

def inputMatrix():
    noOfRows = int(input("Enter the number of rows :"))
    noOfCols = int(input("Enter the number of columns:"))
    matrix = []
    for rows in range(noOfCols):
        rows = []
        for columns in range(noOfRows):
            n = eval(input("Enter the number of elements one by one:"))
            rows.append(n)
        matrix.append(rows)

    return matrix

def addMatrices(m1,m2):
    newMatrix = []
    for i in range(len(m1)):
        r = []
        for j in range(len(m2)):
            a = m1[i][j] + m2[i][j]
            r.append(a)
        newMatrix.append(r)

    return newMatrix
            


def printMatrix(m):
    for i in m:
        for j in i:
            print(j,end = "\t")
        print()
    
    
print("Enter only the square matrices.")
A = inputMatrix()
B = inputMatrix()
s_matrix = addMatrices(A,B)
answer = printMatrix(s_matrix)
