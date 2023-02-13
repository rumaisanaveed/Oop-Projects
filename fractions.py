# Class to tell the value of a fraction after divison
class Fraction:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def fractionDivison(self):
        answer = (self.a) / (self.b)
        print(f"The value of the fraction {self.a} / {self.b} is {answer}.")

n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
of1 = Fraction(n1,n2)
of1.fractionDivison()

f1 = "9 / 3"
f2 = "8 / 2"
x = f1.split("/")
y = f2.split("/")
a = int(x[0])
b = int(x[1])
c = int(y[0])
d = int(y[1])
if b == d:
    i = a + c
    print(f"The sum of {f1} and {f2} is {i} / {d}.") 
else:
    j = b * d
    k = a * j // b
    l = c * j // d
    f = k + l
    print(f"The sum of {f1} and {f2} is {f} / {j}.")

class Fractions():
    def __init__(self,f1,f2):
        self.f1 = f1
        self.f2 = f2
    
    def addFractions(self):
        x = self.f1.split("/")
        y = self.f2.split("/")
        a = int(x[0])
        b = int(x[1])
        c = int(y[0])
        d = int(y[1])
        if b == d:
            i = a + c
            if i / d == i // d:
                ans = i // d
                print(f"The sum of {self.f1} and {self.f2} is {ans}.")
            else:
                print(f"The sum of {self.f1} and {self.f2} is {i} / {d}.") 
        else:
            j = b * d
            k = a * j // b
            l = c * j // d
            f = k + l
            if f / j == f // j:
                ans = f // j
                print(f"The sum of {self.f1} and {self.f2} is {ans}.")
            else:
                print(f"The sum of {self.f1} and {self.f2} is {f} / {j}.")

f1 = str(input("Enter the fraction 1:"))
f2 = str(input("Enter the fraction 2:"))
obj = Fractions(f1,f2)
obj.addFractions()
