s1 = {1, 2, 3, 4, 5}
s2 = {5, 7, 8, 9, 10}
print(s1.union(s2))

print(f"InterSection {s1} and {s2} : ", s1.intersection(s2))

print(f"InterSection {s1} and {s1} : ", s1.intersection(s1))

print(s1 - s2)
