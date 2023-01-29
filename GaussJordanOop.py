class GaussJordan():
   def __init__(self):
         self.noOfRows = int(input("Enter the number of rows of matrix :"))
         self.noOfCols = int(input("Enter the number of columns of matrix :"))
         self.matrix = []
         for columns in range(self.noOfRows):
              self.n = list(eval(input(f"Enter the elements of row {columns + 1} separated by comma:")))
              self.matrix.append(self.n)
        

   def displayMatrix(self):
        for row in self.matrix:
            print(row)


        return self.matrix

   def elementaryRowOperations(self):
        self.pr = int(input("Enter the pivot row:"))
        self.pr -= 1
        self.pc = int(input("Enter the pivot column:"))
        self.pc -= 1
        self.pe = self.matrix[self.pr][self.pc]
        self.nr = len(self.matrix)
        self.nc = len(self.matrix[0])
        if not self.pe == 0:
           for i in range(self.nc):
              self.matrix[self.pr][i] = round(self.matrix[self.pr][i] / self.pe,3)

           for j in range(self.nr):
               if not j == self.pr:
                  self.makeZero = self.matrix[j][self.pc]
                  for k in range(self.nc):
                    self.matrix[j][k] = round(self.matrix[j][k] - self.matrix[self.pr][k] * self.makeZero,3)


        self.displayMatrix()
            
o = GaussJordan()
o.displayMatrix()
user_confirmation = "Y"
while user_confirmation != "N":
      o.elementaryRowOperations()
      user_confirmation = str(input("Enter Y to continue and N to quit:"))
 
        
        
