try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("2.txt", "r") as f2:
        print(f2.read())
except Exception as e:
    print(e)
try:
    with open("3.txt", "r") as f3:
        print(f3.read())
except Exception as e:
    print(e)

print("Program ends with success")
