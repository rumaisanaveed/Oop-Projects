# Factorial calculating program
##def factorial(n):
##    if n == 0:
##        return 1
##    else:
##        return(n * factorial(n - 1))

##x = int(input("ENTER THE NUMBER :"))
##y = factorial(x)
##print(f"The factorial of {x} is {y}.")
##
### Power calculating program
##
##def power1(n1,n2):
##    if n2 == 0:
##        return 1
##    else:
##        return(n1 * power1(n1,n2 - 1))
##
##def power2(num1,num2):
##    if num2 == 0:
##        return 1
##    else:
##        return(1 / num1 * power2(num1,num2 + 1))
##
##x = int(input("Enter number 1 :"))
##y = eval(input("Enter number 2:"))
##if x > 0 and y > 0:
##    result1 = power1(x,y)
##    print(f"{x} raised to the power {y} is {result1}.")
##if x > 0 and y < 0:
##    result2 = power2(x,y)
##    print(f"{x} raised to the power {y} is {result2}.")

# GCD Calculation Program

##def gcd(n1,n2):
##    r = n1 % n2
##    if n2 == 0:
##        return n1
##    else:
##        return(gcd(,))
##
##num1 = int(input("Enter the number 1:"))
##num2 = int(input("Enter the number 2:"))
##result = gcd(num1,num2)
##print(f"The gcd of {num1} and {num2} is {result}.")

## Euclidean algorithm
##n1 = 12
##n2 = 6
##while n2 != 0:
##    r = n1 % n2
##    n1 = n2
##    n2 = r
##print(f"The gcd is {n1}.")
##    
### 33 % 12 = 9
### 12 % 9 = 3
### 9 % 3 = 6
### 3 % 6 = 3
### 6 % 3 = 0
### 3 % 0 = 3

##def fib(n):
##    if n == 1:
##        return 0
##    elif n == 2:
##        return 1
##    else:
##        return fib(n-1) + fib(n-2)
##
##a = fib(5)
##print(a)

##def gcd(n1,n2):
##    if n2 == 0:
##        return n1
##    else:
##        return gcd(n2,n1 % n2)
##
##print(gcd(33,12))

##def fib(n):
##    if n == 1:
##        return 0
##    elif n == 2:
##        return 1
##    else:
##        return fib(n-1) + fib(n-2)
##print(fib(6))

##def factorial(n):
##    if n == 0:
##        return 1
##    else:
##        return (n * factorial(n-1))
##print(factorial(4))
##
### Even power
##def power(n1,n2):
##    if n2 == 0:
##        return 1
##    else:
##        return (n1 * power(n1,n2 -1))
##print(power(2,3))

##def oddPower(a,b):
##    if b == 0:
##        return 1
##    else:
##        return (1 / a * oddPower(a,b + 1))
##print(oddPower(2,-3))

# Factorial
# Power
# Fibbonaci sequence
# Euclidean algorithm


def factorial(n):
    if n == 0:
        return 1
    else:
        return(n * factorial(n - 1))
print(factorial(3))

def gcd(a,b):
    if b == 0:
        return a
    else:
        return (gcd(b,a % b))
print(gcd(33,12))

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))
print(fib(7))

def evenPower(a,b):
    if b == 0:
        return 1
    else:
        return (a * evenPower(a,b - 1))
print(evenPower(2,3))


def oddPower(a,b):
    if b == 0:
        return 1
    else:
        return (1 / a * oddPower(a,b + 1))
print(oddPower(2,-3))



























    
