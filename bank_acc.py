class BankAccount:
    bank_name = "JP Morgan Chase"
    all_acc = [] # class attribute - list of all accounts; need to find out how to print this!
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, bal): 
        self.int_rate = int_rate
        self.bal = bal
        BankAccount.all_acc.append(self)

    def deposit(self):
        amount = input("How much would you like to deposit today?\n")
        amount = int(amount)
        self.bal = self.bal + amount
        print(f"You now have a balance of ${self.bal}")

    def withdraw(self):
        amount = input("How much would you like to withdraw today?\n")
        amount = int(amount)
        if amount <= self.bal:
            self.bal = self.bal - amount
            print(f"You now have a balance of ${self.bal}")
        else:
            c = input("You have insufficient funds. To continue withdrawing, we will charge you a fee of $5. Please confirm if you would like to continue. Y or N\n")
            if c == "y":
                self.bal = self.bal - amount - 5
                print(f"You now have a balance of ${self.bal}")
            else:
                c = input("Please enter an amount you would like to withdraw:\n")
                c = int(c)
                self.bal = self.bal - c
                print(f"You now have a balance of ${self.bal}")

    def display_account_info(self):
        print(f"Balance: ${self.bal}")
        m = input(f"Welcome to {BankAccount.bank_name}. What would you like to do today?\n Deposit\n Withdraw\n")
        if m == "deposit":
            self.deposit()
        elif m == "withdraw":
            self.withdraw()
        else:
            print("Thank you for banking with us. Have a nice day!")

    def yield_interest(self):
        self.bal = (self.bal * self.int_rate) + self.bal
        print(f"Current balance w/ interest accrued: ${self.bal}")

julie = BankAccount(0.04, 10000)
andrew = BankAccount(0.04, 9000)

julie.deposit()
julie.deposit()
julie.deposit()
julie.withdraw()
julie.yield_interest()
BankAccount.display_account_info(julie)

andrew.deposit()
andrew.deposit()
andrew.withdraw()
andrew.withdraw()
andrew.withdraw()
andrew.withdraw()
andrew.yield_interest()
BankAccount.display_account_info(andrew)