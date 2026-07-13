# ✅ Rule 1: Variable name must start with a letter or underscore (_)
name = "Ali"
_age = 20

# ❌ Invalid: Starts with a number
# 1name = "Ali"


# ✅ Rule 2: Variable name can contain letters, numbers, and underscores
student1 = "Mubashir"
total_marks = 95

# ❌ Invalid: Special characters are not allowed
# total-marks = 95
# total@marks = 95


# ✅ Rule 3: Variable names are case-sensitive
age = 20
Age = 25
print(age)  # 20
print(Age)  # 25


# ❌ Rule 4: Don't use Python keywords as variable names
# if = 10
# class = "CS"


# ✅ Rule 5: Use meaningful variable names
student_name = "Mubashir"
course = "Python"


# ✅ Rule 6: Multiple variable assignment
x, y, z = 10, 20, 30

# ✅ Same value to multiple variables
a = b = c = 100

print(student_name)
print(x, y, z)
print(a, b, c)
