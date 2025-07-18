# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

print("=== Simple Calculator ===")
print("Select Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
choice = input("Enter operation (1/2/3/4): ")

# Perform operation
if choice == '1':
    result = add(num1, num2)
    print(f"Result: {num1} + {num2} = {result}")
elif choice == '2':
    result = subtract(num1, num2)
    print(f"Result: {num1} - {num2} = {result}")
elif choice == '3':
    result = multiply(num1, num2)
    print(f"Result: {num1} * {num2} = {result}")
elif choice == '4':
    result = divide(num1, num2)
    print(f"Result: {num1} / {num2} = {result}")
else:
    print("Invalid operation choice!")
