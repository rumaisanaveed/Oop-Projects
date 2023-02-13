###Class
##class JobInterviews:
##    #class attribute.These attributes can be used anywhere while the
##    #instance attributes are bounded to only instance function.
   a = "This is class attribute."
   def __init__(self,name,age,experience):
       #Instance attributes
       self.name = name
       self.age = age
       self.experience = experience
#instance
person1 = JobInterviews("Rumaisa",18,"6 years")
print(person1.name,"is",person1.age,"years old","and has a experience of",person1.experience)
print(person1.a)
print(JobInterviews.a)

# ###Class
# ##
# ##class DrivingLicense():
# ##    def __init__(self,name,age):
# ##        self.name = name
# ##        self.age = age
# ##        print(name)
# ##        print(age)
# ##
# ##    def canDrive(self,age):
# ##        if age > 18:
# ##            print("You can drive.")
# ##
# ##    def cantDrive(self,age):
# ##        if age == 18:
# ##            print("You can't drive.")
# ##
# ##odrivingLicense = DrivingLicense("Rumaisa",18)
# ##odrivingLicense.canDrive(20)
# ##odrivingLicense.cantDrive(20)
# ##
# ##
# ##class Introduction():
# ##    
# ##
# ##    def printIntroduction(self,myName,myAge,myProfession,myHobby):
# ##        print(f"My name is {myName}.")
# ##        print(f"My age is {myAge}.")
# ##        print(f"My profession is {myProfession}.")
# ##        print(f"My hobby is {myHobby}.")
# ##
# ##ointroduction = Introduction()
# ##ointroduction.printIntroduction("Rumaisa",18,"Software engineering","Book reading")
# ##
# ##
# ##class Student():
# ##    def __init__(self,name,age,emailAddress,currentGrade):
# ##        self.name = name
# ##        self.age = age
# ##        self.emailAddress = emailAddress
# ##        self.currentGrade = currentGrade
# ##
# ##    def showInfo(self,name,age,emailAddress,currentGrade):
# ##        print(name)
# ##        print(age)
# ##        print(emailAddress)
# ##        print(currentGrade)
# ##        print()
# ##
# ##ofirstStudent = Student("Rumaisa",19,"rumaisanaved@gmail.com","BSSE")
# ##ofirstStudent.showInfo("Rumaisa",19,"rumaisanaved@gmail.com","BSSE")
# ##osecondStudent = Student("Muzna",16,"muznanaved@23gmail.com","First Year")
# ##osecondStudent.showInfo("Muzna",16,"muznanaved@23gmail.com","First Year")
# ##                         
# ##
# ##
# ##class Player():
# ##    def __int__(self,name,points,health,location):
# ##        self.name = name
# ##        self.points = points
# ##        self.health = health
# ##        self.location = location
# ##
# ##    def printMenu(self,name,points,health,location):
# ##        print("YOUR MENU")
# ##        print("Name =",name)
# ##        print("Points =",points)
# ##        print("Health =",health)
# ##        print("Location =",location)
# ##        print()
# ##
# ##
# ##ofirstPlayer = Player()
# ##ofirstPlayer.printMenu("Rumaisa",100,"Normal","Pakistan")
# ##
# ##
# ##class Person():
# ##    def __init__(self,name,address,phoneNumber,birthday):
# ##        self.name = name
# ##        self.address = address
# ##        self.phoneNumber = phoneNumber
# ##        self.birthday = birthday
# ##
# ##    def showAddressBook(self,name,address,phoneNumber,birthday):
# ##        print("--------------------MY ADDRESS BOOK--------------------")
# ##        print(name)
# ##        print(address)
# ##        print(phoneNumber)
# ##        print(birthday)
# ##
# ##omyAddressBook = Person()
# ##omyAddressBook.showAddressBook("Rumaisa","P&t Society,House no B-148,Korangi,Karachi","03171848879","24th May")
# ##
# ##
# ##class SalesPerson():
# ##    def __init__(self,firstName,lastName):
# ##        self.firstName = firstName
# ##        self.lastName = lastName
# ##
# ##    sales = 0
# ##    def makeSale(self,saleValue):
# ##        self.sales += saleValue
# ##
# ##    def salesReport(self):
# ##        print(f"My total sales are {self.sales}.")
# ##
# ##o = SalesPerson("Rumaisa","Naveed")
# ##o.makeSale(500)
# ##o.salesReport()
# ##
# ##class Vehicle():
# ##    def __init__(self,carAge,carColor,carSeats):
# ##        self.carAge = carAge
# ##        self.carColor = carColor
# ##        self.carSeats = carSeats
# ##
# ##    def showInfo(self):
# ##        print(f"The car is {self.carAge} years old.")
# ##        print(f"The color of the car is {self.carColor}.")
# ##        print(f"The number of seats in the car is {self.carSeats}.")
# ##
# ##car1 = Vehicle(20,"Red",8)
# ##car1.showInfo()
# ##
# ##
# ###INSTANCE VARIABLES
# ###The variables which we define for each object and can be changed for every object
# ##
# ###Class Variables
# ###The variables which we define under a class and these variables gets change if we
# ###want to change it for a single object
# ##
# ##class Car():
# ##
# ##    wheels = 4
# ##
# ##    def __init__(self):
# ##        self.companyName = "BMW"
# ##        self.mil = 10
# ##
# ##    def showData(self):
# ##        print("The Car's Company Name =",self.companyName)
# ##        print("The Car's mileage is =",self.mil)
# ##        
# ##car1 = Car()
# ##car1.showData()
# ##car1 = Car()
# ##print(car1.companyName)
# ##print(car1.wheels)
# ##car2 = Car()
# ##a = car2.companyName = "Ferrari"
# ##b = car2.mil = 12
# ##print(a,b)
# ##print(car2.wheels)
# ##print(Car.wheels)
# ##Car.wheels = 5
# ##print(Car.wheels)
# ##print(car1.wheels)
# ##print(car2.wheels)
# ##        
# ##
# ##class Student():
# ##
# ##    school = "abcd"
# ##
# ##    def __init__(self,m1,m2,m3):
# ##         self.m1 = m1
# ##         self.m2 = m2
# ##         self.m3 = m3
# ##
# ##    # Instance Method
# ##    def average(self):
# ##        a = (self.m1 + self.m2 + self.m3) / 3
# ##        print(f"The average of marks is {a}.")
# ##        print("School is :",self.school)
# ##
# ##    # Getters/Accessers
# ##    def get_m1(self):
# ##        self.m1 = m1
# ##        print(self.m1)
# ##
# ##    # Setters/Mutators
# ##    def set_m1(self,value):
# ##         return self.m1 = value
# ##
# ##    # Class Method
# ##    @classmethod
# ##    def Info(cls):
# ##        print(cls.school)
# ##
# ##    # Static method
# ##    # The methods to do extra work.These are neither for instance variables nor for class variables
# ##    @staticmethod
# ##    def info():
# ##        print("This is a static method.")
# ##        
# ##    
# ##student1 = Student(23,45,67)
# ###student1.average()
# ###student1.get_m1()
# ###print(student1.set_m1(50))
# ##Student.Info()
# ### Ye static method hai to isko class name se call karen gy
# ##student1.info()
# ##Student.info()
# ####
# ##class Student():
# ##
# ##    def __init__(self,name,rollNo):
# ##        self.name = name
# ##        self.rollNo = rollNo
# ##        self.laptop = self.Laptop()
# ##
# ##    def show(self):
# ##        print("Name = ",self.name)
# ##        print("roll No = ",self.rollNo)
# ##        self.laptop.show()
# ##
# ##    class Laptop:
# ##
# ##        def __init__(self):
# ##            self.brand = "HP"
# ##            self.cpu = "i5"
# ##            self.ram = 8
# ##
# ##        def show(self):
# ##            print(self.brand,self.cpu,self.ram)
# ##
# ##s = Student("Rumaisa",66)
# ###print(type(s))
# ##s.show()
# ##
# ##    
# ##### Inheritance
# ##### Parent class
# ### B class me A class ki sari properties aagayin hain
# # parent class
# ##class B:
# ##     def feature3(self):
# ##         print("Feature 3 is working.")
# ##
# ##     def feature4(self):
# ##        print("Feature 4 is working.")
# ###child class
# ##class A(B):
# ##
# ##    def feature1(self):
# ##        print("Feature 1 is working.")
# ##
# ##    def feature2(self):
# ##        print("Feature 2 is working.")
# ##
# ### Child class
# ##class B:
# ##     def feature3(self):
# ##         print("Feature 3 is working.")
# ##
# ##     def feature4(self):
# ##        print("Feature 4 is working.")
# ##class C(B):
# ##    def feature5(self):
# ##        print("Feature 5 is working.")
# ##
# ##a1 = A()
# ##a1.feature1()
# ##a1.feature2()
# ##a1.feature3()
# ##a1.feature4()
# ##
# ##b1 = B()
# ##b1.feature1()
# ##b1.feature2()
# ##b1.feature3()
# ##b1.feature4()
# ##
# # Multilevel inheritance
# ##class A:
# ##
# ##    def feature1(self):
# ##        print("Feature 1 is working.")
# ##
# ##    def feature2(self):
# ##        print("Feature 2 is working.")
# ##
# ##
# ##class B(A):
# ##     def feature3(self):
# ##         print("Feature 3 is working.")
# ##
# ##     def feature4(self):
# ##        print("Feature 4 is working.")
# ##
# ##class C(B):
# ##    def feature5(self):
# ##        print("Feature 5 is working.")
# ##
# ##
# ### Multiple Inheritance
# # parent class
# ####class A:
# ##    def feature1(self):
# ##        print("Feature 1 is working.")
# ##
# ##    def feature2(self):
# ##        print("Feature 2 is working.")
# ##
# ##parent class    
# ##class B:
# ##     def feature3(self):
# ##         print("Feature 3 is working.")
# ##
# ##     def feature4(self):
# ##        print("Feature 4 is working.")
# ##child class
# ##class C(A,B):
# ##    def feature5(self):
# ##        print("Feature 5 is working.")
# ##
# ##
# ##### Topic:constructor in inheritance
# ####
# ##class A:
# ##     def __init__(self):
# ##          print("Init of A.")
# ##
# ##     def feature1(self):
# ##          print("Feature 1.")
# ##
# ##     def feature2(self):
# ##          print("Feature 2 is working.")
# ##
# ##class B(A):
# ##     def __init__(self):
# ##          # Here we are calling the init of the inherited class.We can do this by using the super() keyword.
# ##          super().__init__()
# ##          print("Init of B.")
# ##     # If we have same methods and we call the method,so the method of the class is executed.
# ##     def feature1(self):
# ##          print("Feature 1 is working.")
# ##
# ##     def feature2(self):
# ##          print("Feature 2 is working.")
# ##
# ##o1 = B()
# ##o1.feature1()


# ### If we have multiple inheritance then,we can also call the init of inherited classes.
# ### First of all,it will call the init of own class.
# ### We can do this simply by using super() keyword.
# ### But which init will call.It will follow the MRO(method resolution order)
# # It will call the init of that class which will be on the left.

# class A:
#      def __init__(self):
#           print("Init of A.")

#      def feature1(self):
#           print("Feature 1-A is working.")

#      def feature2(self):
#           print("Feature 2-A is working.")

# class B:
#      def __init__(self):
#           print("Init of B.")

#      def feature1(self):
#           print("Feature 1-B is working.")

#      def feature2(self):
#           print("Feature 2 is working.")

# class C(A,B):
#      def __init__(self):
#           print("Init of C.")
#           super().__init__()

#      def feature1(self):
#           print("Feature 1 is working.")
#           super().feature1()

#      def feature2(self):
#           print("Feature 2 is working.")
#           super().feature2()

# c1 = C()
# c1.feature1()


# ## MRO is also used for methods
# ####
# ###Polymorphism means one thing can take many forms
# ### 1) Duck typing
# ### A thing which can swim like duck,walk like duck may be a duck.
# ### And that's duck typing
# ##class PyCharm:
# ##
# ##     def execute(self):
# ##          print("Compiling.")
# ##          print("Running.")
# ##          
# ##class MyEditor:
# ##
# ##     def execute(self):
# ##          print("Spell check.")
# ##          print("Convention Check.")
# ##          print("Compiling.")
# ##          print("Running.")
# ##          
# ##class Laptop:
# ##
# ##     def code(self,ide):
# ##          ide.execute()
# ## If there is an object which is ide and it has a method execute then.we are not concerned about which class
# ## we are only concerned about the method execute
# ##ide = MyEditor()
# ##
# ##lap1 = Laptop()
# ##lap1.code(ide)
# ##
# ##
# ###9. Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said
# ###class and print the original and modified values of the said attributes.
# ##
# ##
# ##class Student():
# ##
# ##     def __init__(self,studentName,marks):
# ##          self.studentName = studentName
# ##          self.marks = marks
# ##          print(studentName)
# ##          print(marks)
# ##
# ##o = Student("Rumaisa",90)
# ##o2 = Student("Muzna",79)
# ##
# ####1. Write a Python class named Student with two attributes student_id, student_name.
# ####Add a new attribute student_class. Create a function to display
# ####the entire attribute and their values in Student class.
# ##
# ##class Student():
# ##
# ##     def __init__(self,student_name,student_id,student_class):
# ##          self.student_name = student_name
# ##          self.student_id = student_id
# ##          self.student_class = student_class
# ##
# ##     def show(self):
# ##          print(self.student_name)
# ##          print(self.student_id)
# ##          print(self.student_class)
# ##
# ##o = Student("Rumaisa",56789,"BSSE")
# ##o.show()
# ##     
# ##
# ####(The Account class) Design a class named Account that contains:
# ####■ A private int data field named id for the account.
# ####■ A private float data field named balance for the account.
# ####■ A private float data field named annualInterestRate that stores the current
# ####interest rate.
# ####■ A constructor that creates an account with the specified id (default 0), initial
# ####balance (default 100), and annual interest rate (default 0).
# ####■ The accessor and mutator methods for id, balance, and annualInterestRate.
# ####■ A method named getMonthlyInterestRate() that returns the monthly
# ####interest rate.
# ####■ A method named getMonthlyInterest() that returns the monthly interest.
# ####■ A method named withdraw that withdraws a specified amount from the
# ####account.
# ####■ A method named deposit that deposits a specified amount to the account.
# ###Write a test program that creates an Account object with an account id of 1122, a
# ####balance of $20,000, and an annual interest rate of 4.5%. Use the withdraw
# ####method to withdraw $2,500, use the deposit method to deposit $3,000, and print
# ####the id, balance, monthly interest rate, and monthly interest.
# ##
# ##class Account():
# ##
# ##     def __init__(self,withDrawAmount,depositAmount,id = 0,balance = 100,annualInterestRate = 0):
# ##          self.__id = id
# ##          self.__balance = balance
# ##          self.annualInterestRate = annualInterestRate
# ##
# ##     def getId(self):
# ##          return self.__id
# ##
# ##     def getBalance(self):
# ##          return self.__balance
# ##
# ##     def getAnnualInterestRate(self):
# ##          return self.__annualInterestRate
# ##
# ##     def monthlyInterestRate(self):
# ##          return self.annualInterestRate / 12
# ##
# ##     def withDraw(self):
# ##          return self.withDrawAmount
# ##
# ##     def deposit(self):
# ##          return self.__balance + self.depositAmount
# ##
# ##myAccount = Account(2500,3000,1122,20000,4.5)
# ##print(myAccount.getId())
# ##print(myAccount.getBalance())
# ##print(myAccount.monthlyInterestRate())
# ##
# ####(The Fan class) Design a class named Fan to represent a fan. The class contains:
# ####■ Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to
# ####denote the fan speed.
# ####■ A private int data field named speed that specifies the speed of the fan.
# ####■ A private bool data field named on that specifies whether the fan is on (the
# ####default is False).
# ####■ A private float data field named radius that specifies the radius of the fan.
# ####■ A private string data field named color that specifies the color of the fan.
# ####■ The accessor and mutator methods for all four data fields.
# ####■ A constructor that creates a fan with the specified speed (default SLOW), radius
# ####(default 5), color (default blue), and on (default False).
# ####Write a test program that creates two Fan objects. For the first object, assign
# ####the maximum speed, radius 10, color yellow, and turn it on. Assign medium speed, radius 5,
# ####color blue, and turn it off for the second object. Display each object’s speed,
# ####radius, color, and on properties.
# ##
# ##class Fan():
# ##     slow = 1
# ##     medium = 2
# ##     fast = 3
# ##
# ##     def __init__(self,speed = slow,on = False,radius = 5,color = "blue"):
# ##          self.__speed = speed
# ##          self.__on = on
# ##          self.__radius = radius
# ##          self.__color = color
# ##
# ##     def getSpeed(self):
# ##          return self.__speed
# ##
# ##     def getOn(self):
# ##          return self.__on
# ##
# ##     def getRadius(self):
# ##          return self.__radius
# ##
# ##     def getColor(self):
# ##          return self.__color
# ##
# ##     def show(self):
# ##          print(self.__speed)
# ##          print(self.__on)
# ##          print(self.__radius)
# ##          print(self.__color)
# ##     
# ##fan1 = Fan(Fan.fast,True,10,"yellow")
# ##fan1.show()
# ##fan2 = Fan(Fan.medium)
# ##fan2.show()
# ##
# ##
# ####(Stopwatch) Design a class named StopWatch. The class contains:
# ####■ The private data fields startTime and endTime with get methods.
# ####■ A constructor that initializes startTime with the current time.
# ####■ A method named start() that resets the startTime to the current time.
# ####■ A method named stop() that sets the endTime to the current time.
# ####■ A method named getElapsedTime() that returns the elapsed time for the
# ####stop watch in milliseconds
# ####Write a test program that measures the execution time of adding numbers from 1 to
# ####1,000,000.
# ####import time
# ####
# ####class StopWatch():
# ####
# ####     def __init__(self):
# ####          self.__startTime = startTime
# ####          self.__endTime = endTime
# ####
# ####     def getStartTime(self):
# ####          return self.__startTime
# ####
# ####     def getEndTime(self):
# ####          return self.endTime
# ####
# ####     def start(self):
# ####          self.__startTime = time.strftime("%H:%M:%S")
# ####
# ####     def stop(self):
# ####          self.__endTime = time.strftime("%H:%M:%S")
# ####
# ####     def getElapsedTime(self):
# ##
# ### Operator overloading          
# ##class Student:
# ##
# ##     def __init__(self,m1,m2):
# ##          self.m1 = m1
# ##          self.m2 = m2
# ##
# ##     def __add__(self,other):
# ##          m1 = self.m1 + other.m1
# ##          m2 = self.m2 + other.m2
# ##          s3 = Student(m1,m2)
# ##
# ##          return s3
# ##
# ##s1 = Student(58,69)
# ##s2 = Student(60,65)
# ##
# ##s3 = s1 + s2
# ####print(s3.m1)
# ##
# ##class Student:
# ##
# ##     def __init__(self,m1,m2):
# ##          self.m1 = m1
# ##          self.m2 = m2
# ##
# ##     def __str__(self):
# ##          return '{} {}'.format(self.m1,self.m2)
# ### After this line s1 address will not show
# ##          return self.m1,self.m2
# ### With this line the s1 will return address
# ##
# ##s1 = Student(2,3)
# ##print(s1)
# ##print(s1.__str__())
# ##
# ### Whenever we call print ,it calls __str__ method
# ### If we don't want the address of object,then we will override the __str__ function.
# ###Overriding means change built-in functions according to our needs.
# #Operator overloading
# ###In overloading operands or parameters gets changed.
# ### In overloading,we have the same method name but the arguments are different or may be the number of
# ### arguments or the types of argument are different.
# #----------------------------------------------------------------------------------------------
# ## Method overloading
# ### In the same class,we have two same methods with the different parameters.This is
# ### called method overloading.
# ### But in python it is not supported.
# ### We will use a trick to do it.
# ### Student class
# ###def average(a,b):
# ###def average(a,b,c):
# ##------------------------------------------------------------------------------------------------
# ### code of method overloading
# ##class Student:
# ##
# ##     def sum(self,a = None,b = None,c = None):
# ##          if a != None and b != None and c != None:
# ##               s = a + b + c 
# ##          elif a != None and b != None:
# ##               s = a + b
# ##          else:
# ##               s = a
# ##          return s
# ##s1 = Student()
# ##print(s1.sum(5))
# # Method overriding
# ### In the different classes we have the same methods with same or different parameters.This is called
# ### method overriding.
# ###parent class
# ##class A:
# ##     def show(self):
# ##          print("Show in A.")
# ### child class
# ##class B(A):
# ###    pass
# ##      def show(self):
# ##           print("Show in B.")
# ##s1 = B()
# ##s1.show()
# ##a = A()
# ##a.show()
# ### Jab B me show method nhi tha to usne parent class ka show kia aur jab usky paas apna aik show method tha to usne
# # apna ahow method use kiya.
# #-----------------------------
# # Topics covered
# #-----------------------------
# # Objects and classes
# # Inhertitance
# # 1) Multilevel inheritance
# # 2) Multiple inheritance
# # 3) Single inheritance
# # 4) Hierarchical inheritance
# # 5) Hybrid Inheritance
# # Polymorphism
# # 1) Duck typing
# # 2) Operator overloading
# # 3) Method overloading
# # 4) Method overriding
# # Variables
# # 1)Instance variables
# # 2)Class variables
# # Methods
# # 1)Class methods
# # 2)Static methods
# # 3)Instance methods
# # Getters/Accessors
# # Setters/Modifiers/Mutators
# #-----------------------------
# # Remaining topics
# # Encapsulation
# # Abstraction
# # Destructor
# # UML
# #-------------------------------
# # Encapsulation in python
# #-------------------------------
# # It describes the idea of wrapping data and the methods that work on data withion one single unit called class.
# # This puts restriction on accessing variables and methods directly and can prevent the accidental modification of data.
# # Access  modifiers
# # Access modifiers are used to restrict access to the variables and methods of the class.
# # There are three types of access modifiers
# # Public Modifier
# # The members of a class that are declared public are easily accessible from any part of the program.All data members
# ### and member functions of a class are public by default.
# ##class Car:
# ##    def __init__(self,color,company,speed):
# ##        # Public members
# ##        self.color = color
# ##        self.company = company
# ##        self.speed = speed
# ##        
# ##    # public member function
# ##    def getInfo(self):
# ##        # Acessing public members inside the class
# ##        print(self.color)
# ##        print(self.company)
# ##        print(self.speed)
# ##        
# ##c1 = Car("Black","Audi",700)
# ##c1.getInfo()
# ### Accessing public members outside the class
# ##print(c1.color)

# ### Protected Modifiers
# # Kisi bhi class k protected variables sirf usi class me accessible hoty hain jo us class se derived hoti hai

# ##class Student():
# ##
# ##    def __init__(self,name,age,rollNo):
# ##        self._name = name # Protected
# ##        self._age = age
# ##        self._rollNo = rollNo
# ### derived class
# ##class A(Student):
# ##
# ##    def displayDetails(self):
# ##        # Accessing protected variables in the derived class
# ##        print(self._name)
# ##        print(self._age)
# ##        print(self._rollNo)
# ##
# ##s1 = A("Rumaisa",18,66)
# ##s1.displayDetails()
# ##s2 = Student("Rumaisa",18,66)
# ##print(s2.name)
# ##
# # Private modifiers
# # ye variables sirf class me hi accessible hoty hain

# ##class Student():
# ##
# ##    def __init__(self,name,age,rollNo):
# ##        self.__name = name 
# ##        self.__age = age
# ##        self.__rollNo = rollNo
# ##
# ##    # Private Method
# ##    def __displayPrivateModifiers(self):
# ##        print(self.__name)
# ##        print(self.__age)
# ##        print(self.__rollNo)
# ##
# ##    def printPrivateModifiers(self):
# ##
# ##        self.__displayPrivateModifiers()
# ##
# ##s1 = Student("Rumaisa",18,66)
# ##s1.printPrivateModifiers()
# #---------------------------------------------------------------------------------------------------------------------------------
# # Abstract class
# # A class which contains absract methods is called abstract class.
# # Abstract Method
# # A method which has declaration but doesn't have any body is called abstract method.
# # We can't make an object from abstract class.
# # Python doesn't support creation of abstract classes,whereas it has module named abc to create
# # abstract classes.
# # When you inherit an abstract class as a parent class to the child class,the child class should define all the abstract
# # methods present in the parent class.
# # If it is not done then child class also becomes abstract class automatically.

# from abc import ABC,abstractmethod

# # Abstract class
# class Computer(ABC):
#     @abstractmethod
#     def process(self):
#         print("It's running and compiling.")

# # Not an abstract class
# # Jab hmne abstract method define nhi kia tha to ye wali class bhi hamare pass abstract class thi
# # lekin jese hi humne wo abstract method define kardia to wo abstract class nhi rahi aur isi tarah agar
# # hum ne uska object bana lia...warna hum object nhi bana skty thy...
# class Laptop(Computer):
#      pass
#      def process(self):
#          print("It's running.")
# ###com = Computer()
# #com.process()
# lap = Laptop()
# lap.process()



# ##s = 0
# ##count = 0
# ##user = "continue"
# ##while user != "quit":
# ##    n = int(input("Enter the marks :"))
# ##    if n < 0:
# ##        break
# ##    else:
# ##       s += n # 30 60 25 
# ##       count += 1 # 1 2 3
# ##       avg = s / count
# ##    user = str(input("Enter continue to continue and quit to stop:"))
# ##print(avg)
    

# ##Destructors are called when an object gets destroyed. In Python,
# ##destructors are not needed as much as in C++ because Python has
# ##a garbage collector that handles memory management automatically. 
# ##The __del__() method is a known as a destructor method in Python.
# ##It is called when all references to the object have been deleted
# ##i.e when an object is garbage collected. 
##Syntax of destructor declaration : 
 
#def __del__(self):
##  # body of destructor
##
##class Employee:
## 
##    # Initializing
##    def __init__(self):
##        print('Employee created.')
## 
##    # Deleting (Calling destructor)
##    def __del__(self):
##        print('Destructor called, Employee deleted.')
## 
##obj = Employee()
##del obj
##
## 
##class Employee:
## 
##    # Initializing
##    def __init__(self):
##        print('Employee created')
## 
##    # Calling destructor
##    def __del__(self):
##        print("Destructor called")
## 
##def Create_obj():
##    print('Making Object...')
##    obj = Employee()
##    print('function end...')
##    return obj
## 
##print('Calling Create_obj() function...')
##obj = Create_obj()
##print('Program End...')
##
##
class A:
    def __init__(self, bb):
        self.b = bb
 
class B:
    def __init__(self):
        self.a = A(self)
    def __del__(self):
        print("die")
 
def fun():
    b = B()
 
fun()

##In this example when the function fun() is called, it creates an instance
##of class B which passes itself to class A, which then sets a reference to
##class B and resulting in a circular reference.Generally, Python’s garbage
##collector which is used to detect these types of cyclic references would
##remove it but in this example the use of custom destructor marks this item
##as “uncollectable”. Simply, it doesn’t know the order in which to destroy
##the objects, so it leaves them. Therefore, if your instances are involved
##in circular references they will live in memory for as long as the
##application run.
