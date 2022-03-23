import cbpro
import json
import datetime
import time


class CoinbaseAPI:
    def __init__(self):
        print("Coinbase API Initiated")
        self.public_client = cbpro.PublicClient()

    def getHistoricalData(self, coin_pair, start, end, granularity):
        print(">>> Collecting historical data for {} from {} to {} every {} second".format(coin_pair, start, end, granularity))

        data = []
        start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end, "%Y-%m-%d")