import os
class FilesList():
   def __init__(self,p):
       self.path = p

   def listOfFiles(self):
       directory = os.scandir(self.path) # returns files names
       for i in directory:
           if i.is_file(): # checks if it's a file or not
               if i.name.endswith(".txt"): # checks if it's a text file
                    print(i.name)
               
p = "C:\\Users\Humayun\Desktop"        
o1 = FilesList(p)
o1.listOfFiles()
p = "C:\\Users\Humayun\Documents"
o2 = FilesList(p)
o2.listOfFiles()
p = "C:\\SalesData"
o3 = FilesList(p)
o3.listOfFiles()

def scanner(path):
    try:
       directory = os.scandir(path)
       for i in directory:
          if i.is_file():
              if i.name.endswith(".txt"):
                  print(i.name)
          else:
              scanner(i)
    except:
        print("Permission denied.")

scanner("C:\\")
