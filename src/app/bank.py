import app


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    def open_account(self, account):
        assert isinstance(account, app.Account), 'Account should be an app.Account'
        assert account.number not in self.accounts, 'Account number ' + str(account.number) + ' already taken!'
        self.accounts[account.number] = account
        return account

    def add_transaction(self, *, sender, recipient, subject, amount, transaction_ID):
        assert sender.number in self.accounts, 'Sender has no account yet!'
        assert recipient.number in self.accounts, 'Recipient has no account yet!'
        assert sender.has_funds_for(amount), 'Account has not enough funds'
        ids = []
        for transaction in self.transactions:
            ids.append(transaction.transaction_ID)
        assert transaction_ID not in ids ,'Transaction_ID ' + str( transaction_ID ) + ' already taken!'


        self.transactions.append(app.Transaction(sender=sender.number, recipient=recipient.number, subject=subject,
                                                 amount=amount, transaction_ID=transaction_ID))
        sender.subtract_from_balance(amount)
        recipient.add_to_balance(amount)
        return self.transactions[-1]

def account_info(self, account.info)
    for number, account in bank.accounts.items():
    print(account.info())

for transaction in bank.transactions:
    if transaction.sender == Eugen.number or transaction.recipient == Eugen.number:
            print(transaction.info())


accountlist=[]
for number, account in bank.accounts.items():
        print( account.number, account.firstname, account.lastname)
        accountlist.append(account)

for number, account in bank.accounts.items():
        sorted(accouinaccount.number)

list2= sorted(accountlist, key=lambda x:x.number)


for item in list2:
    print(item.number, item.firstname, item.lastname)