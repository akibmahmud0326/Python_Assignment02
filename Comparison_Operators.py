a = 10
b = 20
print("Equal?", a == b)

age1 = 29
age2 = 20
if age1 > age2:
    print("Person 1 is older")
else:
    print("Person 2 is older")

year = 1999
print("Before 2000" if year < 2000 else "After or in 2000")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Greater number:", num1 if num1 > num2 else num2)

mark1 = 85
mark2 = 85
print("Same marks?", mark1 == mark2)

n = 19
if n != 0:
    print("Result:", 100 / n)
else:
    print("Cannot divide by zero")
