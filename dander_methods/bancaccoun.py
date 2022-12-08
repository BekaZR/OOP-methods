class BancAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.balance + other


Beka = BancAccount("Beka", 1000)

print(Beka + 100)
