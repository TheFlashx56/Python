list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = int(input("Enter Number you want table for : "))
for i in list:
    print(f"{number} x {i} =", i * number)

list2 = ["Apples ", "grapes", "3.3", "220"]
print(list2[0])
# list are mutable( value can be changes)
list2[0] = "new value"
print(list2[0])
