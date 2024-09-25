class BankAccount:
    def __init__(self, account_number, account_holder):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = 0

    def get_account_number(self):
        return self._account_number

    def get_account_holder(self):
        return self._account_holder
    
    def get_balance(self):
        return self._balance
    
    def make_deposit(self, deposit_amt):
        self._balance += deposit_amt

    def make_withdrawal(self, withdrawal_amt):
        if self._balance >= withdrawal_amt:
            self._balance -= withdrawal_amt
        else:
            print(f'You do not have sufficient funds for this withdrawal. Your currrent balance is {self._balance}.')

    def get_account_details(self):
        print(f'Account Holder: {self._account_holder}')
        print(f'Account Number: {self._account_number}')
        print(f'Balance: {self._balance}')

acct1 = BankAccount(12345, "Lisa Jones")
acct1.make_deposit(150)
acct1.get_account_details()
acct1.make_withdrawal(75)
print(acct1.get_balance())
acct1.make_withdrawal(100)
