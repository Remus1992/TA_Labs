import datetime
import time


class BankAccount:
    def __init__(self, first_name, last_name, beginning_amount, interest_rate, pin_number, list_transactions=None):
        self.fname = first_name
        self.lname = last_name
        self.balance = beginning_amount
        self.interest = interest_rate
        self.pin = pin_number
        self.locked = False

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

    def set_account(self, account_number):
        if account_number in self.accounts:
            self.account_number = self.accounts[account_number]
            return True
        return False

    def pin_verification(self, pin_entry):
        if self.account_number.pin == pin_entry:
            return True
        else:
            return False

    def user_authentication(self):
        username = input("What is your account number?: ")
        is_user = self.set_account(username)
        if is_user and not self.account_number.locked:
            attempts = 0
            while attempts < 3:
                pin_prompt = int(input("Enter Pin: "))
                if self.pin_verification(pin_prompt):
                    return is_user
                else:
                    if attempts < 2:
                        print("Not valid pin")
                        remaining_guesses = 2 - attempts
                        print("You have {} attempts left.".format(remaining_guesses))
                    else:
                        print("Account Locked")
                        self.account_number.locked = True
                        return False
                    attempts += 1
        elif self.account_number.locked:
            print("Contact admin. Your account is locked.")
            return False

        else:
            print("Not a valid account number.")
            return False

    def atm_menu(self, user_test):
        if user_test:
            while True:
                prompt = input('what would you like to do(deposit, withdraw, check balance, history, calc interest)?: ')
                if prompt == 'deposit':
                    money = int(input('How much would you like to add?: '))
                    self.deposit(money)
                elif prompt == 'withdraw':
                    money = int(input('How much would you like to withdraw?: '))
                    self.withdraw(money)
                elif prompt == 'calc interest':
                    print(atm.calc_interest())
                elif prompt == 'check balance':
                    print(atm.check_balance())
                elif prompt == 'history':
                    self.account_number.total_transactions()
                elif prompt == 'logout':
                    print("Have a nice day, {}".format(self.account_number.fname))
                    self.logout()
                    break
                else:
                    print("Sorry not a valid option.")

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

    def logout(self):
        self.account_number = None
        return False


dictionary_atm = {'0001': BankAccount("Remington", "Henderson", 100, 0.001, 1234,
                                      {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'}),
                  "0002": BankAccount("Louis", "Parker", 100, 0.001, 1234,
                                      {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'}),
                  "0003": BankAccount("Jerry", "Seinfeld", 100, 0.001, 1234,
                                      {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'}),
                  "0004": BankAccount("Walter", "White", 100, 0.001, 1234,
                                      {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'}),
                  "0005": BankAccount("Beth", "Wintermute", 100, 0.001, 1234,
                                      {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'}),
                  "0006": BankAccount("Topher", "Grace", 100, 0.001, 1234,
                                      {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'}),
                  "0007": BankAccount("Jessie", "Stirrup", 100, 0.001, 1234,
                                      {datetime.datetime.now().isoformat(timespec='seconds'): 'opened account'})
                  }

atm = ATM('ATM', dictionary_atm)

while True:
    user = atm.user_authentication()
    atm.atm_menu(user)
