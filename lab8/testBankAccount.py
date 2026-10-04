'''
Exercise Lab8
Jiaxi Pang
'''

import unittest
from bankaccount import BankAccount  

class TestBankAccount(unittest.TestCase):
   
    def setUp(self):
        self.account = BankAccount('Alice', 1000)

    
    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000)
        self.assertEqual(self.account.owner, 'Alice')
        
        default_account = BankAccount('Bob')
        self.assertEqual(default_account.balance, 0)

    
    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)
        
        self.account.deposit(250)
        self.assertEqual(self.account.balance, 1750)

    
    def test_withdraw(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 700)
        
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 500)

   
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)
        
        self.assertEqual(self.account.balance, 1000)

    
    def test_sequence_of_transactions(self):
        self.account.deposit(500)    
        self.account.withdraw(200)   
        self.account.deposit(1000)   
        self.account.withdraw(300)   
        self.account.withdraw(500)   
        self.assertEqual(self.account.balance, 1500)

if __name__ == '__main__':
    unittest.main()