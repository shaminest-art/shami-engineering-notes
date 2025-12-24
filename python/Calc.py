import math

operator = input("Enter the Operator: +, -, *, %, /: ")
num1 = float(input("Enter the first Number: "))
num2 = float(input("Enter the second Number: "))

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(round(num1*num2,3))
elif operator == "/":
    print(round(num1/num2,3))
elif operator=="%":
    print(round(num1%num2,3))
else:
    print(f"You have entered WRONG operator:{operator} ")




