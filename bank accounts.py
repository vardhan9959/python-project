class customer:
    def __init__(self):
        self.details = 0
        print("Welcome to the customer!")
    def account(self, bank, Ifsc, account_number, branch_code):
        print("Name of the bank: ", bank)
        print("Ifsc code of the bank: ", Ifsc)
        print("your account_number: ", account_number)
        print("your branch_code: ", branch_code)
a = customer()
a.account("sbi", "sbi00567", "987675434209", 9087)


class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("welcome to deposite & withdrawal machine")

    def deposite(self):
        amount = float(input("Enter amount be deposited: "))
        self.balance += amount
        print("Amount deposited: ", amount)

    def withdrawal(self):
        amount = float(input("Enter amount to withdrawal: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You withdraw: ", amount)
        else:
            print("Insufficient balance ")

    def display(self):
        print("Net Available Balance=", self.balance)


s = Bank_Account()
s.deposite()
s.withdrawal()
s.display()





