import argparse
from config import *
from DataSet import Dataset
from LSTMModel import LSTMModel
from TradeBot import TradeBot
from CoinbaseAPI import CoinbaseAPI
import pickle

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_and_trade", action="store_true")
    args = parser.parse_args()

    dataset = Dataset()

    if args.train_and_trade:
        print(">>> Training Data for {}".format(COIN_PAIR))
        data = dataset.loadCoinData(COIN_PAIR, TRAINING_MONTHS)
        x_train, y_train, _ = dataset.createTrainTestSets(COIN_PAIR, data, training_window=TRAINING_WINDOW, labeling_window=LABELING_WINDOW)

        print(">>> Creating Testing Data for {}".format(COIN_PAIR))
        data = dataset.loadCoinData(COIN_PAIR, TESTING_MONTHS)
        x_test, y_test, prices = dataset.createTrainTestSets(COIN_PAIR, data, training_window=TRAINING_WINDOW, labeling_window=LABELING_WINDOW)

        test_model = LSTMModel(x_train)
        test_model.train(x_train, y_train, batch_size=64, epochs=10)
        test_model.evaluate(x_test,y_test)

        trade_bot = TradeBot(test_model)
        initial_amt = trade_bot.account.balance
        trade_bot.runSimulation(x_test, prices)
        final_amt = trade_bot.account.balance + trade_bot.account.btc_balance 
        profit_loss = final_amt - initial_amt

        print("##########################################   Summary   ##########################################")
        print("#           Initial Balance: ${:.2f}".format(initial_amt))
        print("#           Final Balance:   ${:.2f}".format(final_amt))
        print("#           Profit/Loss:     ${:.2f} ({:.2f}%)".format(profit_loss, (profit_loss/initial_amt)*100))
        print("#################################################################################################")

    else:
        print(">>> Please use an argument next time: --train_and_trade")

