list_of_toppers = ["mubashir", "eass", "tayyab", "kaif", "sohaib"]

name = input("Enter your name to check whether you are in topppers list or not : ")

if name in list_of_toppers:
    print(f"Congratulation {name} you are in topper ")
else:
    print(f"Good Luck try again {name}")
