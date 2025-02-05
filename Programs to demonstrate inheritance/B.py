# Base class Account
class Account:
    def __init__(self, accnumber, balance):
        self._accnumber = accnumber  # Protected member
        self._balance = balance  # Protected member

# SBAccount (Savings Bank Account) class
class SBAccount(Account):
    def __init__(self, accnumber, init_balance):
        super().__init__(accnumber, init_balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance:.2f}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if self._balance - amount >= 1000:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance:.2f}")
        else:
            print("Insufficient balance! You must maintain a minimum balance of Rs.1000/-")

    def calc_interest(self):
        interest = self._balance * 0.04  # 4% annual interest
        self._balance += interest
        print(f"Interest of {interest:.2f} added. New balance: {self._balance:.2f}")

# FDAccount (Fixed Deposit Account) class
class FDAccount(Account):
    def __init__(self, accnumber, period, deposit_amount):
        super().__init__(accnumber, deposit_amount)
        self._period = period  # in years

    def calc_interest(self):
        interest = self._balance * (0.0825 * self._period)  # 8.25% annual interest
        return interest

    def close(self):
        interest = self.calc_interest()
        self._balance += interest
        print(f"Account closed. Interest of {interest:.2f} added. Final balance: {self._balance:.2f}")

# Customer class
class Customer:
    def __init__(self, cust_id, name, address):
        self.cust_id = cust_id
        self.name = name
        self.address = address
        self.sb_account = None
        self.fd_account = None

    def createAccount(self, acc_type, accnumber, balance_or_deposit, period=None):
        if acc_type == 'SB':
            self.sb_account = SBAccount(accnumber, balance_or_deposit)
            print(f"SBAccount created for {self.name}.")
        elif acc_type == 'FD':
            self.fd_account = FDAccount(accnumber, period, balance_or_deposit)
            print(f"FDAccount created for {self.name}.")
        else:
            print("Invalid account type!")

    def transaction(self, acc_type, transaction_type, amount=None):
        if acc_type == 'SB' and self.sb_account:
            if transaction_type == 'deposit':
                self.sb_account.deposit(amount)
            elif transaction_type == 'withdraw':
                self.sb_account.withdraw(amount)
            elif transaction_type == 'calc_interest':
                self.sb_account.calc_interest()
            else:
                print("Invalid transaction type for SBAccount!")
        elif acc_type == 'FD' and self.fd_account:
            if transaction_type == 'close':
                self.fd_account.close()
            else:
                print("Invalid transaction type for FDAccount!")
        else:
            print(f"No {acc_type} account found for {self.name}!")

# BankDemo class to demonstrate functionality
class BankDemo:
    def main(self):
        # Create customers
        customer1 = Customer(1, "Alice", "123 Wonderland")
        customer2 = Customer(2, "Bob", "456 Nowhere Lane")

        # Customer 1 creates SB account and performs transactions
        customer1.createAccount('SB', 1001, 5000)
        customer1.transaction('SB', 'deposit', 1500)
        customer1.transaction('SB', 'withdraw', 2000)
        customer1.transaction('SB', 'calc_interest')

        # Customer 2 creates FD account and performs transactions
        customer2.createAccount('FD', 2001, 100000, 2)  # FD for 2 years
        customer2.transaction('FD', 'close')

        # Add customers to a list
        customers = [customer1, customer2]

        # Demonstrate manipulations
        for customer in customers:
            print(f"\nCustomer ID: {customer.cust_id}, Name: {customer.name}")
            if customer.sb_account:
                customer.transaction('SB', 'calc_interest')
            if customer.fd_account:
                customer.transaction('FD', 'close')

# Run the main program
if __name__ == "__main__":
    BankDemo().main()
