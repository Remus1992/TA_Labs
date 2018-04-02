import datetime
import time


class BankAccount:
    def __init__(self, first_name, last_name, beginning_amount, interest_rate, list_transactions=None):
        self.fname = first_name
        self.lname = last_name
        self.balance = beginning_amount
        self.interest = interest_rate

        if list_transactions is None:
            self.transactions = {}
        else:
            self.transactions = list_transactions

    def total_transactions(self):
        print('**********%s\'s History**********' % self.fname)
        for i in self.transactions:
            print('--->' + i + ' | ' + self.transactions[i])


class ATM:
    def __init__(self, name, accounts=None):
        self.name = name
        self.account_number = None
        self.accounts = accounts or {}

    def check_balance(self):
        if self.account_number:
            return self.account_number.balance
        return None

    def deposit(self, deposit_amount):
        time.sleep(1)
        self.account_number.transactions[datetime.datetime.now().isoformat(
            timespec='seconds')] = '{} deposited ${}'.format(self.account_number.fname, deposit_amount)
        self.account_number.balance += deposit_amount
        return self.account_number.balance

    def check_withdrawal(self, desired_withdraw_amount):
        if self.account_number.balance - desired_withdraw_amount > 0:
            return True
        else:
            return False

    def withdraw(self, withdraw_amount):
        time.sleep(1)
        if self.check_withdrawal(withdraw_amount) is True:
            self.account_number.transactions[datetime.datetime.now().isoformat(
                timespec='seconds')] = '{} withdrew ${}'.format(self.account_number.fname, withdraw_amount)
            self.account_number.balance -= withdraw_amount
            return self.account_number.balance
        else:
            self.account_number.transactions[datetime.datetime.now().isoformat(
                timespec='seconds')] = 'Insufficient Funds'
            return "You don't have enough money"

    def calc_interest(self):
        time.sleep(1)
        interest_earned = self.account_number.balance * self.account_number.interest
        self.account_number.transactions[datetime.datetime.now().isoformat(
            timespec='seconds')] = 'Due to interest, ${} was added to {}\'s account'.format(interest_earned,
                                                                                            self.account_number.fname)
        self.account_number.balance = self.account_number.balance + interest_earned
        return self.account_number.balance

    def set_account(self, account_number):
        if account_number in self.accounts:
            self.account_number = self.accounts[account_number]
            return True
        return False

    def logout(self):
        self.account_number = None


dictionary_atm = {'remy': BankAccount("Remington", "Henderson", 100, 0.001,
                                      {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'}),
                  "louis": BankAccount("Louis", "Parker", 100, 0.001,
                                       {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'}),
                  "jerry": BankAccount("Jerry", "Seinfeld", 100, 0.001,
                                       {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'}),
                  "walter": BankAccount("Walter", "White", 100, 0.001,
                                        {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'}),
                  "beth": BankAccount("Beth", "Wintermute", 100, 0.001,
                                      {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'}),
                  "topher": BankAccount("Topher", "Grace", 100, 0.001,
                                        {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'}),
                  "jessie": BankAccount("Jessie", "Stirrup", 100, 0.001,
                                        {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'})
                  }

atm = ATM('ATM', dictionary_atm)

username = input("What is your username: ")
is_user = atm.set_account(username)
if is_user:
    while True:
        prompt = input('what would you like to do(deposit, withdraw, check balance, history)?: ')
        if prompt == 'deposit':
            money = int(input('How much would you like to add?: '))
            atm.deposit(money)
        elif prompt == 'withdraw':
            money = int(input('How much would you like to add?: '))
            atm.withdraw(money)
        elif prompt == 'check balance':
            print(atm.check_balance())
        elif prompt == 'history':
            print(atm.account_number.total_transactions())
        else:
            break

