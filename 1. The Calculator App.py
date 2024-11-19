#Task 1: Create functions for each arithmetic operation
# Function for Addition
def add(a, b):
    return a + b

# Function for Subtraction
def subtract(a, b):
    return a - b

# Function for Multiplication
def multiply(a, b):
    return a * b

# Function for Division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed"

# Function for Modulus (Remainder)
def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Division by zero is not allowed"

# Function for Exponentiation
def exponentiate(a, b):
    return a ** b

# Function for Integer Division (Floor Division)
def integer_divide(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: Division by zero is not allowed"

#Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
# Function for Addition
def add(a, b):
    return a + b

# Function for Subtraction
def subtract(a, b):
    return a - b

# Function for Multiplication
def multiply(a, b):
    return a * b

# Function for Division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed"

# Function for Modulus (Remainder)
def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Division by zero is not allowed"

# Function for Exponentiation
def exponentiate(a, b):
    return a ** b

# Function for Integer Division (Floor Division)
def integer_divide(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: Division by zero is not allowed"

# Main program
def main():
    print("Welcome to the Python Calculator!")
    
    # Ask the user for the operation
    operation = input("Enter the operation you want to perform (add, subtract, multiply, divide, modulus, exponentiate, integer_divide): ").lower()

    # Ask the user for the numbers to use in the operation
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "modulus":
            result = modulus(num1, num2)
        elif operation == "exponentiate":
            result = exponentiate(num1, num2)
        elif operation == "integer_divide":
            result = integer_divide(num1, num2)
        else:
            result = "Invalid operation"

        print(f"The result of {operation} {num1} and {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")
    
if __name__ == "__main__":
    main()

#Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.
# Function for Addition
def add(a, b):
    return a + b

# Function for Subtraction
def subtract(a, b):
    return a - b

# Function for Multiplication
def multiply(a, b):
    return a * b

# Function for Division
def divide(a, b):
    try:
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Function for Modulus (Remainder)
def modulus(a, b):
    try:
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a % b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Function for Exponentiation
def exponentiate(a, b):
    return a ** b

# Function for Integer Division (Floor Division)
def integer_divide(a, b):
    try:
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a // b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Main program
def main():
    print("Welcome to the Python Calculator!")

    # Ask the user for the operation
    operation = input("Enter the operation you want to perform (add, subtract, multiply, divide, modulus, exponentiate, integer_divide): ").lower()

    # Ask the user for the numbers to use in the operation
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "modulus":
            result = modulus(num1, num2)
        elif operation == "exponentiate":
            result = exponentiate(num1, num2)
        elif operation == "integer_divide":
            result = integer_divide(num1, num2)
        else:
            result = "Invalid operation"

        print(f"The result of {operation} {num1} and {num2} is: {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()