#Steps
#Matrix input
#Choose pivot column and pivot row
#Make pivot column zero
#Repeat steps 2 and 3
#Print matrix


##class SimplexMethod():
##    def __init__(self):
##          self.matrix = []
##          self.noOfRows = int(input("Enter no of rows of matrix :"))
##          for rows in range(self.noOfRows):
##               self.r = list(eval(input(f"Enter the numbers of {rows + 1} row separated by comma:")))
##               self.matrix.append(self.r)
##               
##    def operations(self):  
##           self.minV = min(self.matrix[0])
##           while self.minV < 0:
##              self.pc = self.matrix[0].index(self.minV)
##              self.a = len(self.matrix[0]) - 1
##              self.minR = []                           
##              for j in range(len(self.matrix)):            
##                if j == 0:
##                   continue            
##                self.d = self.matrix[j][self.pc]
##                self.c = self.matrix[j][self.a] / self.d
##                self.minR.append(self.c)
##    
##              self.pr = self.minR.index(min(self.minR)) + 1
##        
##              self.pe = self.matrix[self.pr][self.pc]
##              self.nr = len(self.matrix)
##              self.nc = len(self.matrix[0])
##              for i in range(self.nc):
##                 self.matrix[self.pr][i] = round(self.matrix[self.pr][i] / self.pe,3)
##
##              for s in range(self.nr):
##                 if s != self.pr:
##                     self.makeZero = self.matrix[s][self.pc]
##                     for k in range(self.nc):
##                          self.matrix[s][k] = round(self.matrix[s][k] - self.matrix[self.pr][k] * self.makeZero,3)
##        
##              self.minV = min(self.matrix[0])
##
##    def printMatrix(self):
##        for i in self.matrix:
##            print(i)
##        
##o = SimplexMethod()
##o.operations()
##o.printMatrix()


matrix = []
noOfRows = int(input("Enter the no of rows:"))
noOfCols = int(input("Enter the number of columns:"))
for i in range(noOfRows):
    rows = []
    for j in range(noOfCols):
        n = eval(input("Enter the number one by one:"))
        rows.append(n)
    matrix.append(rows)
print(matrix)

minV = min(matrix[0])        
while minV < 0:
    pc = matrix[0].index(minV)
    a = len(matrix) - 1
    minR = []
    for i in range(len(matrix)):
        if i == 0:
            continue
        c = matrix[i][a]
        ratio = c / matrix[i][pc]
        minR.append(ratio)
    pr = minR.index(min(minR)) + 1




        
        
    
























    

