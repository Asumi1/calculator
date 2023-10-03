num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

op = input("Enter basic mathematical operation: ")

i = 0

while (i == 0) :
  if op == "+":
    i += 1
    answer = num1 + num2
  elif op == "-":
    i += 1
    answer = num1 - num2
  elif op == "*":
    i += 1
    answer = num1 * num2
  elif op == "/":
    i += 1
    answer = num1 / num2
  else:
    op = input("Please input basic mathematical operation (+, -, *, /) ")

print("Answer is " + str(answer))