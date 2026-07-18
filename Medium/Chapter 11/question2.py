class Bank:
    def __init__(self,balance):
        self._balance=balance
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self,value):
        self._balance=value


user=Bank(12900)
print(user._balance)