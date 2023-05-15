# calculator
# Add
def add(a, b):
    return a + b

# Subtract
def subtract(a, b):
    return a - b

# Multiply
def multiply(a, b):
    return a * b

# Divide
def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
from art import logo
print(logo)
def calculator():
    num1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    new_cal = False
    while not new_cal:
        operation_symbol = input("Pick an operation from above: ")
        num2 = float(input("Enter the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer
        cont = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to start a new calculation. ")
        if cont == 'n':
            new_cal = True
            calculator()

calculator()