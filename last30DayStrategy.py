import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import combineData



cols, df = combineData.combineData()

# Strategy uses 5 and 10 day moving averages to determine momentum.  Those with the highest difference in their
# smas were ranked.  Top 3 chosen and placed into an equally weighted portfolio.  Every long crypto is held for one day
# then the process repeats for the next day.  This is problematic since getting your coins can take up to a week.
# Next strat should look at holding for a week. or maybe holding some extra coin to sell in order to reduce risk.

# These are lists I make to call all the columns in the dataframes faster

pctchCols = []
sma1Cols = []
sma2Cols = []
cumReturnCols = []
smaDiffs = []

# For each of the columns:

for c in cols:

    # Get the back test returns from holding tomorrow price to the day after price
    df[c + ' pct_ch'] = df[c].shift(-2) / df[c].shift(-1) - 1
    # Get simple moving averages
    df[c + ' sma1'] = df[c].rolling(5).mean()
    df[c + ' sma2'] = df[c].rolling(10).mean()
    # Calculate the difference from sma1 to sma2 for ranking.  The greater the number the higher the momentum
    df[c + ' sma diff'] = df[c + ' sma1'] / df[c + ' sma2'] - 1
    # Get cumulative return for holding single crypto
    df[c + ' cum return'] = (1 + df[c + ' pct_ch']).cumprod() - 1

    # Append these column names to list for easy retrieval
    pctchCols.append(c + ' pct_ch')
    smaDiffs.append(c + ' sma diff')
    sma1Cols.append(c + ' sma1')
    sma2Cols.append(c + ' sma2')
    cumReturnCols.append(c + ' cum return')

# Rank the sma differences to check for momentum
ranked = df[smaDiffs].rank(axis=1)


stratReturns = []

# For each crypto, check if momentum is in top rank amongst other cryptos and place into equally weighted portfolio

for c in cols:
    df[c + ' rank'] = ranked[c + ' sma diff']
    # 0 or 1 if position is long
    df[c + ' long'] = np.where(df[c + ' rank'] > 8, 1, 0)
    # multiply backtest return * if long (0 or 1) * portfolio weight
    df[c + ' strat'] = df[c + ' long'] * df[c + ' pct_ch'] * .2

    stratReturns.append(c + ' strat')

# fig, ax = plt.subplots(1)

# Sum up the returns for the long strategies
df['sum return strat'] = df[stratReturns].sum(axis=1)
# Get cumulative returns for entire strategy
df['cum return strat'] = (1 + df['sum return strat']).cumprod() - 1

ax = df[['btc cum return', 'eth cum return', 'cum return strat', 'ltc cum return', 'dash cum return']].plot()

vals = ax.get_yticks()
ax.set_yticklabels(['{:3.2f}%'.format(x*100) for x in vals])
# print df['dash']
# df['dash'].plot()


# fig.autofmt_xdate()
plt.show()






# print df.tail()