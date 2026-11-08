# This is a simple calculator
#print(9+6)
#print(9-6)
#print(9*6)
#print(9/6)
#print(9//6)
#print(9%6)
#print(9**6)


a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if b == 0:
    print("The second number must not be zero.")
else:
    print("The value of", a, "+", b, "is", a + b)
    print("The value of", a, "-", b, "is", a - b)
    print("The value of", a, "*", b, "is", a * b)
    print("The value of", a, "/", b, "is", a / b)
    print("The value of", a, "//", b, "is", a // b)
    print("The value of", a, "%", b, "is", a % b)
    print("The value of", a, "**", b, "is", a ** b)