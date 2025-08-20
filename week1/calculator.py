def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero")
        return None
    else:
        return a / b
print("Select operation/n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide")
ch = input("Enter choice (1/2/3/4): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if ch == '1':
    print("Result:", add(a, b))
elif ch == '2':
    print("Result:", subtract(a, b))
elif ch == '3':
    print("Result:", multiply(a, b))
elif ch == '4':
    print("Result:", divide(a, b))
else:
    print("Invalid choice")