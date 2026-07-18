class Employee:
    a = 1


class Coder(Employee):
    b = 2


class Programer(Coder):
    c = 3


o = Programer()
print(o.a, o.b, o.c)
