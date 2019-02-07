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

    def add_transaction(self, *, sender, recipient, subject, amount):
        assert sender.number in self.accounts, 'Sender has no account yet!'
        assert recipient.number in self.accounts, 'Recipient has no account yet!'
        assert sender.has_funds_for(amount), 'Account has not enough funds'

        self.transactions.append(app.Transaction(sender=sender.number, recipient=recipient.number, subject=subject,
                                                 amount=amount))
        sender.subtract_from_balance(amount)
        recipient.add_to_balance(amount)
        return self.transactions[-1]
