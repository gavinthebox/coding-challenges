import unittest

from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Create two bank accounts for testing
        self.account1 = BankAccount("Alice", 1000)
        self.account2 = BankAccount("Bob", 500)

    def test_deposit(self):
        self.account1.deposit(100)
        self.assertEqual(self.account1.get_balance(), 1100)

    def test_withdraw(self):
        self.account1.withdraw(1500)  # Should raise an error
        self.assertEqual(self.account1.get_balance(), 1000)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(-100)

    def test_apply_interest(self):
        self.account1.apply_interest()
        expected_balance = 1000 + (1000 * 0.02)  # 2% interest
        self.assertEqual(self.account1.get_balance(), expected_balance)

    def test_transfer(self):
        self.account1.transfer(200, self.account2)
        self.assertEqual(self.account1.get_balance(), 800)
        self.assertEqual(self.account2.get_balance(), 700)

    def test_transfer_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account1.transfer(2000, self.account2)  # Should raise an error

    def test_transfer_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account1.transfer(-100, self.account2)

    def test_transaction_history(self):
        self.account1.deposit(100)
        self.account1.withdraw(50)
        self.account1.apply_interest()
        self.account1.transfer(200, self.account2)

        history = self.account1.get_transaction_history()
        self.assertEqual(len(history), 4)  # Four transactions should have been recorded

        # Verify the content of transaction history
        self.assertEqual(history[0], {"type": "deposit", "amount": 100})
        self.assertEqual(history[1], {"type": "withdraw", "amount": 50})
        self.assertEqual(history[2]["type"], "interest")  # Interest type
        self.assertGreater(history[2]["amount"], 0)  # Interest amount should be positive
        self.assertEqual(history[3], {"type": "transfer", "amount": 200, "to": "Bob"})

    def test_apply_interest_negative_balance(self):
        self.account1.withdraw(1000)  # Withdraw all funds, making balance negative
        with self.assertRaises(ValueError):
            self.account1.apply_interest()  # Should raise an error

if __name__ == '__main__':
    unittest.main()