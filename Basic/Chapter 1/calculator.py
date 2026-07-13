print("----------Calculator-------------")
print("Enter a : ")
a = float(input())
print("Enter b : ")
b = float(input())
print("Enter a operation you want to perform(+,-,*,/) :  ")
operation = input()
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(int(a * b))
elif operation == "/":
    print(a / b)
else:
    print("Invalid")
