marks = {"Mubashir": 100, "Sidhart": 23, "Rohail": 56, "list": [1, 22, 44, 21]}

# poori dictionary print karo
print(marks)

# key aur value ke pairs print karo
print(marks.items())

# sirf keys print karo
print(marks.keys())

# sirf values print karo
print(marks.values())

# existing value update karo aur nayi key add karo
marks.update({"Mubashir": 99, "Eass": 55})
print(marks)

# key ki value hasil karo
print(marks.get("Eass"))

# agar key na ho to None return karega
print(marks.get("Ali"))

# direct key se value access karo
print(marks["Mubashir"])

# agar key na ho to add kar de warna purani value return kare
print(marks.setdefault("Ahmed", 80))
print(marks)

# di hui key remove karke uski value return kare
print(marks.pop("Eass"))
print(marks)

# aakhri key-value pair remove kare
print(marks.popitem())
print(marks)

# dictionary ki copy banao
copy_marks = marks.copy()
print(copy_marks)

# di hui keys ke sath nayi dictionary banao
print(dict.fromkeys(["A", "B", "C"], 0))

# poori dictionary khali kar do
marks.clear()
print(marks)
