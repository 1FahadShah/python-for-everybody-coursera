#using function to perform basic calculator operations

def operation(a,b,op):
    if (op == '+'):
        print(f"Addition: \n {a} + {b} = {a+b}")
    elif (op == '-'):
        print(f"Subtraction: \n {a} - {b} = {a-b}")
    elif (op == '*'):
        print(f"Multiplication: \n {a} * {b} = {a*b}")
    elif (op == '/'):
        if b == 0:
            print("Error!!! Division by Zero")
        else:
            print(f"Multiplication: \n {a} / {b} = {a/b}")
    else:
        print("Unknown Operation")
    
a = float(input("Enter First Number: "))
op = input("Enter operation to perform (+, -, *, /): ")
b = float(input("Enter Second Number: "))
operation(a,b,op)
