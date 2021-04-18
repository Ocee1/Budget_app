

class budget:

    def __init__(self, name):
        self.name = name
        self.records = list()

    def deposit(self, amount):
        self.records.append({self.name: amount})
        print(self.records)
    
    
    def withdraw(self, amount):

        if (self.check_funds(amount)):
            self.records.append({"amount": -amount})
            return True;
        return False


    def  get_balance(self):
        total_cash = 0
        for item in self.records:
            total_cash += item["amount"]
            return total_cash
    
    def transfer(self, amount, category):

        if(self.check_funds(amount)):
            self.withdraw(amount,"Transfer to " + budget.name)
            category.deposit(amount, "transfer from " + self.name)
            return True
        return False


    #def check_funds(self, amount):

food = budget('rice')
food.deposit(18)
