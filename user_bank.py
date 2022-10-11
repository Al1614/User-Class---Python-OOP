class User:

    def __init__(self, name="Unassigned", starting_balance=0, interest_rate=0.04):
        self.name = name
        self.account = BankAccount(starting_balance, interest_rate)


    # have this method decrease the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    # have this method print the user's name and account balance to the terminal
    # eg. User: Guido van Rossum, Balance: $150
    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def yield_interest(self):
        self.account.yield_interest()
        return self

class BankAccount:

    bank_name = "First National Dojo"
    all_accounts = []


    def __init__(self, balance=0, interest=0.4):
        self.balance = balance
        self.interest_rate = interest
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        print("Depositing $" + str(amount))
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
        else:
            print("Withdrawing $" + str(amount)) 
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Account Balance: $" + str(self.balance))
        print("Interest Rate:", self.interest_rate)
        return self

    def yield_interest(self):
        print("Yielding interest...")
        self.balance += self.balance * self.interest_rate
        return self


    # Extra Class Methods for Testing (Bank Account Assignment Bonus)
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum

    @classmethod
    def print_all(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        return cls


# User test
sadie = User("Sadie Sink")
sadie.display_user_balance().make_deposit(100).display_user_balance()
sadie.make_withdrawal(55).display_user_balance()
sadie.yield_interest().display_user_balance()

sami = User(name="Samantha Bee", interest_rate=0.02)
sami.display_user_balance().make_deposit(500)
sami.make_withdrawal(150).display_user_balance()
sami.yield_interest().display_user_balance()
