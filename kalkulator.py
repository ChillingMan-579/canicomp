import math

def calculate(num1, num2, op):
  result = 0
  if op == "+":
    result = num1 + num2
  elif op == "-":
    result = num1 - num2
  elif op == "*":
    result = num1 * num2
  elif op == "/":
    result = num1 / num2
  elif op == "^":
    result = pow(num1, num2)
  elif op == "sin":
    result = math.sin(math.radians(num1))
  elif op == "cos":
    result = math.cos(math.radians(num1))
  elif op == "tan":
    result = math.tan(math.radians(num1))
  elif op == "sqr.r":
    result = math.sqrt(num1)
  return result

num1 = int(input("num1: "))
op = input("operator (+, -, *, /, ^, sin, cos, tan, sqr.r): ")
num2 = int(input("num2: "))
print(f"result = {calculate(num1, num2, op)}")
