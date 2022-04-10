from DemoAccount import DemoAccount
import numpy as np
from config import *
import time


class TradeBot:

    def __init__(self, model):
        self.advisor = model
        self.account = DemoAccount()
        self.trade_amount = TRADE_AMOUNT
        self.initial_balance = self.account.balance

    def buy(self):
        prev_bought_at = self.account.btc_bought_at          # Last bought price
        if self.account.balance - self.trade_amount >= 0:    # Check if there is enough fund to trade
            if prev_bought_at == 0 or self.account.last_transaction_was_sold or (prev_bought_at > self.account.btc_price):
                print(">> BUYING $", self.trade_amount, " WORTH OF BITCOIN")
                self.account.btc_amount += self.trade_amount / self.account.btc_price
                self.account.balance -= self.trade_amount
                self.account.btc_bought_at = self.account.btc_price
                self.account.last_transaction_was_sold = False
            else:
                print(">> Not worth buying more BTC at the moment")
        else:
            print(">> Not enough USD left in your account to buy BTC ")

    def sell(self):
        if self.account.btc_balance - self.trade_amount >= 0:
            if self.account.btc_price > self.account.btc_bought_at: # Is it profitable?
                print(">> SELLING $", self.trade_amount, " WORTH OF BITCOIN")
                self.account.btc_amount -= (self.trade_amount / self.account.btc_price)
                self.account.balance += self.trade_amount
                self.account.last_transaction_was_sold = True
            else:
                print(">> Declining sale: Not profitable to sell BTC")
        else:
            print(">> Not enough BTC left in your account to buy USD ")

    def runSimulation(self, samples, prices):
        print("> Trading Automatically for ", TESTING_MONTHS)
        day_count = 0
        for i in range(0,len(samples)):

            if i % 24 == 0:
                day_count += 1
                print("#################################################################################################")
                print("#           Account Balance: $", (self.account.balance + self.account.btc_balance), " BTC: $",
                      self.account.btc_balance, " USD: $", self.account.balance, "")
                print("#################################################################################################")
                print("##########################################   DAY ", day_count, "   #########################################")

            if i % TRADE_FREQUENCY == 0: # Perform a prediction every 6 hours
                prediction = self.advisor.predict(np.array([samples[i]]))
                # btc_price = samples[i][len(samples[i])-1]
                btc_price = prices[i]

                if self.account.btc_price != 0:
                    self.account.btc_balance = self.account.btc_amount * btc_price

                self.account.btc_price = btc_price

                if prediction == 1:
                    self.buy()
                else:
                    self.sell()

                self.account.btc_balance = self.account.btc_amount * btc_price

                time.sleep(DISPLAY_SPEED)  # Only for Visual Purposes

        print("#################################################################################################")
        print("#           Account Balance: $", (self.account.balance + self.account.btc_balance), " BTC: $",
              self.account.btc_balance, " USD: $", self.account.balance, "")
        print("#################################################################################################")
        print()
        print("##########################################   Summary   ##########################################")
        print("#           Initial Balance: ${:.2f}".format(self.initial_balance))
        print("#           Final Balance:   ${:.2f}".format(self.account.balance+self.account.btc_balance))
        print("#           Profit/Loss:     ${:.2f} ({:.2f}%)".format(self.account.balance+self.account.btc_balance-self.initial_balance,
                                                                      ((self.account.balance+self.account.btc_balance-self.initial_balance) / self.initial_balance) * 100))
        print("#################################################################################################")