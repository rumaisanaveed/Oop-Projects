##FIRST CODE:
##def matrix(): # to make a matrix from the given conditions and elements of user.
##    nr = int(input("Enter no. of rows: ")) #3
##    nc = int(input("Enter no. of coloumns: "))# 4
##    M = []
##    nr_M = []
##    for i in range(nr):
##        for j in range(nc):
##            n = float(input(f"Enter element of {i + 1} row & {j + 1} coloumn: "))
##            nr_M.append(n)
##        M.append(nr_M)
##        nr_M = []
##    return M
##
##def mat_rep(M): # to represent the matrix
##    print("----------------------------------------------------")
##    for i in M:
##        for j in i:
##            print(f"{j:<12}",end=" ")
##        print()
##    print("----------------------------------------------------")
##    return M #return the matrix soo we could use to perform operations.
##
##def operation(M): # to perform the elemntary row operations
##    pr = int(input("Enter Pivot row: "))
##    pc = int(input("Enter Pivot coloumn: "))
##    pr -= 1
##    pc -= 1
##    pe = M[pr][pc] # Pivot element.
##    Nr = len(M)
##    Nc = len(M[0])
##    if pe != 0:
##        for i in range(Nc):
##            M[pr][i] = round(M[pr][i] / pe, 7)
##        for j in range(Nr):
##            if j != pr:
##                a = M[j][pc]
##                for k in range(Nc):
##                    M[j][k] = round((M[pr][k] * a) - M[j][k], 7)
##    return M
##
##
##'''THE OPERATIONS PERFORMING BY USING THE FUNCTIONS''' 
##M_main = matrix()
###M_rand = [[1, 1, 2, 9], [2, 4, -3, 1], [3, 6, -5, 0]]
###M = mat_rep(M_rand) # M = mat_rep(M_rand)  when we take the given matrix
##pn = int(input("How many rows u want to do operation on ? "))
##for i in range(pn):
##    M = mat_rep(M_main)
##    M = operation(M_main)
##---------------------------------------------------------------------------------------------------------------------------

##SECOND CODE:
##def printMatrix(Matrix):
##    # M = parameter             main
##    NR = len(Matrix) #main
##    NC = len(Matrix[0]) #main
##    #r = local
##    #c = local
##    print ("---------------------------")
##    for r in range(NR):
##        for c in  range(NC):
##            print ("%8.2f" % (Matrix[r][c]), end= "   ")
##        print ()
##    print ("---------------------------")
##
##
##M = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
###M = [[1,1,2,9],[2,4,-3,1],[3,6,-5,0]]
##NR = len(M)
##NC = len(M[0])
##
##printMatrix(M)
##pr = int(input ("Enter pivot row :"))
##pc = int (input ("Enter pivot column :"))
##while (pr >= 0 and pc >=0):
##    pr -= 1
##    pc -= 1
##
##    if M[pr][pc] != 0:
##
##        pe = M[pr][pc]
##        for c in range(NC):
##           M [pr][c]= M[pr][c] / pe
##                
##        for r in range(NR):
##            makeZero = M[r][pc]
##            if (r == pr): continue
##            for c in range(NC):
##                M[r][c] = M[r][c] - makeZero*M[pr][c]
##
##        printMatrix(M)
##        
##    pr = int(input ("Enter pivot row :"))
##    pc = int (input ("Enter pivot column :"))
##---------------------------------------------------------------------------------------------------------------------------
##
def inputMatrix():
    noOfRows = int(input("Enter the number of rows of matrix :"))
    noOfCols = int(input("Enter the number of columns of matrix :"))
    matrix = []
    for columns in range(noOfRows):
        n = list(eval(input(f"Enter the elements of row {columns + 1} separated by comma:")))
        matrix.append(n)


    return matrix
        

def displayMatrix(matrix):
    for row in matrix:
        print(row)


    return matrix

def elementaryRowOperations(matrix):
    pr = int(input("Enter the pivot row:"))
    pr -= 1
    pc = int(input("Enter the pivot column:"))
    pc -= 1
    pe = matrix[pr][pc]
    nr = len(matrix)
    nc = len(matrix[0])
    if pe != 0:
        for i in range(nc):
            matrix[pr][i] = round(matrix[pr][i] / pe,3)

        for j in range(nr):
            if j != pr:
                makeZero = matrix[j][pc]
                for k in range(nc):
                    matrix[j][k] = round(matrix[j][k] - matrix[pr][k] * makeZero,3)


    displayMatrix(matrix)
            

main_f = inputMatrix()
original_matrix = displayMatrix(main_f)
user_confirmation = "Y"
while user_confirmation != "N":
      elementaryRowOperations(original_matrix)
      user_confirmation = str(input("Enter Y to continue and N to quit:"))
##

#Second code (Without the inputs of pr and pc)
#------------------------------------------------------------------------------------------------------------------------------
def displayMatrix(matrix):
    for row in matrix:
        print(row)

    return matrix

noOfRows = int(input("Enter the number of rows of matrix :"))
noOfCols = int(input("Enter the number of columns of matrix :"))
matrix = []
for rows in range(noOfRows):
    n = list(eval(input(f"Enter the elements of row {columns + 1} separated by comma:")))
    matrix.append(n)

nr = len(matrix)
nc = len(matrix[0])
for r in range(nr):
    pr = r
    for c in range(nc):
        pc = c
        if pr == pc:
            pe = matrix[pr][pc]
            if not pe == 0:
               for i in range(nc):
                   matrix[pr][i] = round(matrix[pr][i] / pe,3)

               for j in range(nr):
                   if not j == pr:
                       makeZero = matrix[j][pc]
                       for k in range(nc):
                            matrix[j][k] = round(matrix[j][k] - matrix[pr][k] * makeZero,3)

print("The reduced form of matrix after gauss jordan method is:")
displayMatrix(matrix)

#------------------------------------------------------------------------------------------------------------------------------

##def inputMatrix():
##    noOfRows = int(input("Enter the number of rows of matrix :"))
##    noOfCols = int(input("Enter the number of columns of matrix :"))
##    matrix = []
##    for rows in range(noOfRows):
##       n = list(eval(input(f"Enter the elements of row {rows + 1} separated by comma:")))
##       matrix.append(n)
##
##    return matrix
##
##
##def displayMatrix(matrix):
##    for row in matrix:
##        print(row)
##
##    return matrix
##
##
##def makePivotElementOne(pe,pr,nc,nr,matrix):
##     if not pe == 0:
##        for i in range(nc):
##            matrix[pr][i] = round(matrix[pr][i] / pe,3)
##
##     return matrix
##
##def makePivotColZero(nr,pr,pc,nc,matrix):
##    for j in range(nr):
##        if not j == pr:
##            makeZero = matrix[j][pc]
##            for k in range(nc):
##                matrix[j][k] = round(matrix[j][k] - matrix[pr][k] * makeZero,3)
##
##    return matrix
##
##def finalMatrix(matrix):
##    nr = len(matrix)
##    nc = len(matrix[0])
##    for r in range(nr):
##        pr = r
##        for c in range(nc):
##            pc = c
##            if pr == pc:
##                pe = matrix[pr][pc]
##                makePivotElementOne(pe,pr,nc,nr,matrix)
##                makePivotColZero(nr,pr,pc,nc,matrix)
##    print("The reduced matrix:")
##    displayMatrix(matrix)
##
##
##M = inputMatrix()
##print("The original matrix:")
##N = displayMatrix(M)
####finalMatrix(N)
##
##def displayMatrix(matrix):
##    for row in matrix:
##        print(row)
##
##    return matrix
##
##noOfRows = int(input("Enter the number of rows of matrix :"))
##noOfCols = int(input("Enter the number of columns of matrix :"))
##matrix = []
##for rows in range(noOfRows):
##    n = list(eval(input(f"Enter the elements of row {rows + 1} separated by comma:")))
##    matrix.append(n)
##
##for r in range(len(matrix)):
##    pr = r
##    for c in range(len(matrix[0])):
##        pc = c
##        if pr == pc:
##            pe = matrix[pr][pc]
##            if not pe == 0:
##               for i in range(len(matrix[0])):
##                   matrix[pr][i] = round(matrix[pr][i] / pe,3)
##
##               for j in range(len(matrix)):
##                   if j != pr:
##                       makeZero = matrix[j][pc]
##                       for k in range(len(matrix[0])):
##                            matrix[j][k] = round(matrix[j][k] - matrix[pr][k] * makeZero,3)
##print("The reduced form of matrix after gauss jordan method is:")
##displayMatrix(matrix)

def displayMatrix(matrix):
    for row in matrix:
        print(row)

    return matrix

noOfRows = int(input("Enter the number of rows of matrix :"))
noOfCols = int(input("Enter the number of columns of matrix :"))
matrix = []
for rows in range(noOfRows):
    n = list(eval(input(f"Enter the elements of row {rows + 1} separated by comma:")))
    matrix.append(n)

for r in range(len(matrix)):
    pr = r
    for c in range(len(matrix[0])):
        pc = c
        if pr == pc:
            pe = matrix[pr][pc]
            if not pe == 0:
               for i in range(len(matrix[0])):
                   matrix[pr][i] = round(matrix[pr][i] / pe,3)

               for j in range(len(matrix)):
                   if j > pr:
                       makeZero = matrix[j][pc]
                       for k in range(len(matrix[0])):
                            matrix[j][k] = round(matrix[j][k] - matrix[pr][k] * makeZero,3)
print("The row echelon form of matrix is:")
displayMatrix(matrix)





