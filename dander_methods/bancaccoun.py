class BancAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def __add__(self, other):
        if isinstance(other, BancAccount):
            return self.balance + other.balance
        
        if isinstance(other, (int, float)):
            return self.balance + other


Beka = BancAccount("Beka", 1000)

Nurs = BancAccount("Nurs", 1000)

print(Beka + Nurs)
