#Calculator
from replit import clear
from imports.art import logo

def add(n1, n2):
    """Esta funcion suma 2 numeros pasados por parametros"""
    return n1 + n2
    
def subtraction(n1, n2):
    """Esta funcion resta 2 numeros pasados por parametros"""
    return n1 - n2
    
def multiply(n1, n2):
    """Esta funcion multiplica 2 numeros pasados por parametros"""
    return n1 * n2
    
def split(n1, n2):
    """Esta funcion divide 2 numeros pasados por parametros"""
    return n1 / n2

operation_dic = {
    "+": add(),
    "-": subtraction(),
    "*": multiply(),
    "/": split(),
}

print(logo)


other_operation = False
total_operation = False
total = 0
while not other_operation:
    if total_operation == False:
        n1 = float(input("What´s the first number?: "))
    else:
        n1 = total
        print(f"The first number is {total}")
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    n2 = float(input("What´s the next number?: "))
    if operation == "+":
        total = add(n1, n2)
    elif operation == "-":
        total = subtraction(n1, n2)
    elif operation == "*":
        total = multiply(n1, n2)
    elif operation == "/":
        total = split(n1, n2)
    print(f"{n1} {operation} {n2} = {total}")
    new_calculation = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ")
    if new_calculation == "y":
        total_operation = True
        clear()
    else:
        other_operation = True
        print("Goodbye.")