# Set banana
my_set = {10, 20, 30, 40}
print(my_set)

# Duplicate values khud remove ho jati hain
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)
# Khali set banane ka sahi tareeqa
empty_set = set()
print(empty_set)

# Element add karo
my_set.add(50)
print(my_set)

# Ek se zyada elements add karo
my_set.update([60, 70, 80])
print(my_set)

# Kisi element ko remove karo (error dega agar na ho)
my_set.remove(20)
print(my_set)

# Kisi element ko delete karo (error nahi dega agar na ho)
my_set.discard(100)
print(my_set)

# Random element remove aur return kare
print(my_set.pop())
print(my_set)

# Set ki copy banao
copy_set = my_set.copy()
print(copy_set)

# Do sets ka union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

# Do sets ka intersection
print(set1.intersection(set2))

# Difference (sirf set1 ke unique elements)
print(set1.difference(set2))

# Symmetric difference (common ke ilawa sab)
print(set1.symmetric_difference(set2))

# Union update kare
set1.update(set2)
print(set1)

# Intersection update kare
set3 = {1, 2, 3}
set4 = {2, 3, 4}
set3.intersection_update(set4)
print(set3)

# Difference update kare
set5 = {1, 2, 3}
set6 = {2, 4}
set5.difference_update(set6)
print(set5)

# Symmetric difference update kare
set7 = {1, 2, 3}
set8 = {3, 4, 5}
set7.symmetric_difference_update(set8)
print(set7)

# Kya dono sets bilkul alag hain?
print({1, 2}.isdisjoint({3, 4}))

# Kya pehla set doosre ka subset hai?
print({1, 2}.issubset({1, 2, 3}))

# Kya pehla set doosre ka superset hai?
print({1, 2, 3}.issuperset({1, 2}))

# Sab elements delete kar do
my_set.clear()
print(my_set)
