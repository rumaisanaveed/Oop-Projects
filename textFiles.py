import os
import time
class TextFiles():
    def __init__(self,filePath):
        self.filePath = filePath
        

    def fileProperties(self):
        self.cTime = os.path.getctime(self.filePath)
        self.c_time = time.ctime(self.cTime)
        print(f"The file was created on {self.c_time}.")
        self.mTime = os.path.getmtime(self.filePath)
        self.cMTime = time.ctime(self.mTime)
        print(f"The file was last modified on {self.cMTime}.")
        self.a_time = os.path.getatime(self.filePath)
        self.c_a_Time = time.ctime(self.a_time)
        print(f"The file access time is {self.c_a_Time}.")
        self.fileSize = os.path.getsize(self.filePath)
        print(f"The size of the file is {self.fileSize}.")
        
        
    def getWords(self):
           self.fileOpen = open(self.filePath,"r")
           self.fileContent = self.fileOpen.readlines()
           for i in self.fileContent:
              words = i.split( )
              for j in words:
                 print(j)
           self.fileOpen.close()

    def getSentences(self):
        self.fileOpen = open(self.filePath,"r")
        self.fileData = self.fileOpen.readlines()
        self.filedata = self.fileOpen.readline()
        print(self.filedata)
        for i in self.fileData:
            print(i)
            print()
        self.fileOpen.close()

    def getParagraphs(self):
        self.fileOpen = open(filePath,"r")
        for paragraph in self.fileOpen:
            print(paragraph)
                

filePath = str(input("Enter the absolute path of text file:"))
try:
   f_properties = TextFiles(filePath)
   f_properties.fileProperties()
   w = TextFiles(filePath)
   w.getWords()
   s = TextFiles(filePath)
   s.getSentences()
   p = TextFiles(filePath)
   p.getParagraphs()
except IOError:
    print("The file doesn't exist.")
            
        
        
        
