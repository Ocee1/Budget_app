class budget:

    def __init__(self, name):
        self.name = name
        self.records = {}

    def deposit(self, amount):
        self.records[self.name] = amount
        print(self.records)
    
    
    def withdraw(self, amount):

        if (self.check_funds() & self.records[self.name] != 0):
          self.records[self.name] -= amount
          self.get_balance()
         




          


    def  get_balance(self):
      print(self.records[self.name])
      
    
    def transfer(self, amount, category):

        if(self.check_funds(amount)):
            self.withdraw(amount)
            category.deposit(amount)


    def check_funds(self, amount):
      if self.records[self.name] <= amount:
        return True
    

Food = budget(Food)
Food.deposit(50)
Food.withdraw(10)
Food.get_balance()
Food.transfer(20, Clothing)

Clothing = budget(Clothing)
Clothing.deposit(50)
Clothing.withdraw(10)
Clothing.get_balance()
Clothing.transfer(20, Food)

Entertainment = budget(Entertainment)
Entertainment.deposit(50)
Entertainment.withdraw(10)
Entertainment.get_balance()
Entertainment.transfer(20, Clothing)

