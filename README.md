# CryptoBacktest

This cryptocurrency backtester uses a momentum strategy using Simple moving average crossovers.  I examine 13 different crypto currencies.  Each one is inputted to the SingleCrypto class to do basic calculations and dataframe setup.  Then all of the them are combined into one dataframe in [combineData](https://github.com/nigel-hall-codes/CryptoBacktest/blob/master/combineData.py)

Then you can find the strategy return calculations in [last30DayStrategy.py](https://github.com/nigel-hall-codes/CryptoBacktest/blob/master/last30DayStrategy.py)

This initial strategy showed ![this](https://github.com/nigel-hall-codes/CryptoBacktest/blob/master/DailyTradeCryptoStrategy.png?raw=true)

This was ok but I found usually when I trade on exchanges you are not able to buy and sell same day.  This led me to create an algorithm with a longer hold period

![Here](https://github.com/nigel-hall-codes/CryptoBacktest/blob/master/WeekHoldStrategy.png?raw=true)




