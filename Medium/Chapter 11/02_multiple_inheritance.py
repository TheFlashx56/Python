class Employee:
    company = "ITC"
    name = "Default Name"

    def show(self):
        print(f"The Name is {self.name} and the Company is {self.company}")


class Coder:
    language = "Python"

    def printLanguages(self):
        print(f"Out of All the  languages here is your language {self.language}")


class Programer(Employee, Coder):
    company = "ITC infotech"

    def showLanguage(self):
        print(f"The Name is {self.name} and he is Good With {self.language}")


a = Employee()
b = Programer()

b.show()
b.printLanguages()
b.showLanguage()
