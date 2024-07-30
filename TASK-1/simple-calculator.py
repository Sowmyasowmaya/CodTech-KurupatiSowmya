# Define a function for each operation
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return "Error: Division by zero!"
  else:
    return x / y

# Main program
print("Simple Calculator")
print("----------------")

# Get user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get user input for operation
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1/2/3/4): "))

# Perform the selected operation
if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = subtract(num1, num2)
elif choice == 3:
    result = multiply(num1, num2)
elif choice == 4:
    result = divide(num1, num2)
else:
    result = "Error: Invalid choice!"

# Display the result
print("Result:", result)
