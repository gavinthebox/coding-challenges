class BankAccount:
    def __init__(self, owner, balance=0, interest_rate=0.02):
        self.owner = owner
        self.balance = balance
        self.interest_rate = interest_rate
        self.transaction_history = []

    def deposit(self, amount):
        if amount < 0:
            print("Cannot deposit a negative amount.")
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        print(f"Deposited ${amount}. New balance is: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount < 0:
            print("Cannot withdraw a negative amount.")
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: ${amount}")
        print(f"Withdrew ${amount}. New balance is: ${self.balance}")

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        self.transaction_history.append("Interest applied.")
        print(f"Interest applied at rate {self.interest_rate}. New balance is: ${self.balance}")

    def get_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)
        return self.transaction_history

    def transfer(self, amount, other_account):
        if self.balance < amount:
            print("Insufficient funds for transfer.")
        elif amount < 0:
            print("Cannot transfer a negative amount.")
        self.balance -= amount
        other_account.balance += amount
        self.transaction_history.append(f"Transferred ${amount} to {other_account.owner}")
        print(f"Transferred ${amount} to {other_account.owner}. New balance is: ${self.balance}")

    def get_balance(self):
        return self.balance

# Example usage:
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

account1.deposit(100)
account1.withdraw(1500)   # Should print insufficient funds
account1.apply_interest()
account1.transfer(200, account2)  # Transfer funds from Alice to Bob
account1.get_transaction_history()
print(account1.get_balance())
print(account2.get_balance())
