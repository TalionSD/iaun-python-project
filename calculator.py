num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter an operator (+, -, *, /, **): ")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: division by zero is not allowed."
elif op == "**":
    result = num1 ** num2
else:
    result = "Invalid operator!"

print("Result:", result)
