from config import *


class DemoAccount:
    def __init__(self):
        self.balance = INITIAL_BALANCE
        self.btc_amount = 0
        self.btc_balance = 0
        self.btc_price = 0
        self.btc_bought_at = 0
        self.last_transaction_was_sold = False
