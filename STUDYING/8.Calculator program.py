# Python calculator
from pydoc import resolve

operator = input("Hello.Enter the operation you want to do (+ - * /): ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if operator == "+":
    result = a + b
    print(round(result, 2))
elif operator == "-":
    result = a - b
    print(round(result, 2))
elif operator == "*":
    result = a * b
    print(round(result, 2))
elif operator == "/":
    result = a / b
    print(round(result, 2))
else:
    print("Error")

input("End")


