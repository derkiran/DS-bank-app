class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []

    def open_account(self, account):
        for item in self.accounts:   # schleife
            assert item['number'] != account['number'], 'Account number 1 already taken!'
        self.accounts.append(account)
        return self.accounts[-1]

    def add_transaction(self, *, sender, recipient, subject, amount):
        self.transaction = {'sender': sender, 'recipient': recipient, 'subject': subject, 'amount': amount}
        assert amount > 0, 'Amount has to be greater than 0'
        self.transactions.append([self.transaction])
        return self.transactions[-1]
