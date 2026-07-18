class Employee:
    def __init__(
        self,
        name,
        company,
    ):
        # Pass remaining arguments up the MRO chain
        super().__init__()
        self.name = name
        self.company = company

    def show(self):
        print(f"The Name is {self.name} and the Company is {self.company}")


class Coder:
    def __init__(
        self,
        language="Python",
    ):
        # Pass remaining arguments up the MRO chain
        super().__init__()
        self.language = language

    def printLanguages(self):
        print(f"Out of All the languages here is your language {self.language}")


class Programer(Employee, Coder):
    company = "ITC infotech"

    def __init__(self, name, company, language="Python"):
        # Pass named arguments up so each class gets what it needs
        super().__init__(name=name, company=company, language=language)

    def showLanguage(self):
        print(f"The Name is {self.name} and he is Good With {self.language}")


# Execution
b = Programer("Eass", "IHC BANK", "Python")

b.show()
b.printLanguages()
b.showLanguage()
