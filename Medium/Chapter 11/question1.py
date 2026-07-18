class Employee:

    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def salary(self):
        return self._salary

    @name.setter
    def name(self, value):
        self._name = value

    @age.setter
    def age(self, value):
        self._age = value

    @salary.setter
    def salary(self, value):
        self._salary = value

    def show(self):
        print(f"NAME : {self._name}")
        print(f"AGE : {self._age}")
        print(f"SALARY : {self._salary}")

emp = Employee("Mubashir ", 21, 112000)

emp.show()