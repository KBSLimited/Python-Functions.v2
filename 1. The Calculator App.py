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


#Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.
