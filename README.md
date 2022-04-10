# AI Crypto TradeBot


## Introduction
The AI of our TradeBot is a simple Deep Recurrent Neural Network which uses immediate information from the past to predict whether BTC will go up or down in the near future.
Our TradeBot will then use this AI as an advisor to make its BUY/SELL decision.

### How it works
For Example, the default `TRADE_FREQUENCY` is set to `6`, which means that every 6 hours, our bot will attempt to make a trade.
1. First, the bot will ask the AI for advice
2. The AI will look at the data for the past 6 hours and tell our bot whether the price of BTC will go up or down in the next 6 hours.
3. The it's up to out TradeBot what to do with that information. If it decides to BUY or SELL, it will do so in batches of a preset fixed amount.

If you change the frequency, it will still follow the same steps.

### General Bot Rules
1. As mentioned above, whenever our TradeBot decides to make a trade, the BUY/SELL order will be a fixed amount (default to be $100/trade). This can be changed in the config file.
2. Consecutive BUY only if the price has gone down.
3. Only SELL at a profit.


## Installation


1. Clone the project
```Bash
git clone https://github.com/4m3r1c4nP13/AI-Crypto_TradeBot.git
```
2. Do some customziations if needed in the next section 
3. Run the command to start the demonstration
- Windows:
```Bash
python ControlStation.py --train_and_trade
```
- Unix:
```Bash
python3 ControlStation.py --train_and_trade
```


## Customize Configuration
Once you've cloned the project, you can make some adjustment in the `config.py` file.

### Initial Balance
This is basically the budget that you give our TradeBot to trade. The default balance is set to $1000.

To change this, you just need to change the value assigned to `INITIAL_BALANCE` in `config.py` file.

### Trade Amount
This is the fixed amount mentioned above, which our TradeBot trade in batches. The default amount is set to $100 per trade. It means that
everytime our bot decide to BUY or SELL, it will be always $100 worth of BTC.

To change this, you just need to change the value assigned to `TRADE_AMOUNT` in `config.py` file.

### Trade Frequency
This is the freqency mentioned above. The default frequency is set to every 6 hour. It means that for every 6 hour, our TradeBot will attempt to make a trade.

To change this, you just need to change the value assigned to `TRADE_FREQUENCT` in `config.py` file.

### Display Speed
This is only for display purposes. This value represents the speed at which our demo will run. The value should range from 0 to 1. At 1, the script will 
run slow enough for user to read the output as our TradeBot making decisions. The default value is set to 0.2

To change this, you just need to change the value assigned to `DISPLAY_SPEED` in `config.py` file.
