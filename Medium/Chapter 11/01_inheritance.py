class Employee:
    company = "ITC"

    def show(self):
        print(f"The Name is {self.name} and the salary is {self.salary}")  # type: ignore


class Programer(Employee):
    company = "ITC infotech"

    def showLanguage(self):
        print(f"The Name is {self.name} and he is Good With {self.language}")  # type: ignore


a = Employee()
b = Programer()

print(a.company)
print(b.company)
