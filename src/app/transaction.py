import datetime
import time
import random


class Transaction:
    def __init__(self, *, sender, recipient, subject, amount, transaction_ID ):
        assert isinstance(transaction_ID, int), 'Sender needs to be an integer'
        assert isinstance(sender, int), 'Sender needs to be an integer'
        assert isinstance(recipient, int), 'Recipient needs to be an integer'
        assert isinstance(amount, float), 'Amount needs to be a float'
        assert amount > 0, 'Amount needs to be greater than 0'
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.amount = amount
        self.transaction_ID = transaction_ID
        ts = time.time()
        self.st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    def info(self):
        # 'From 1 to 2: Test transaction - 10.0 €'
        return f'DATE: {self.st} Transaction_ID: {self.transaction_ID} From Account Nr.{self.sender} to Account Nr.'\
            f' {self.recipient} Subject: {self.subject} - {self.amount} €'

