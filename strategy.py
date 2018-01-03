import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


cols = []
for file in os.listdir('/Users/Hallshit/newdir/Finance/Cryptos/historicalCryptos'):
    cols.append(file[:-4])

all = pd.DataFrame(columns=cols)

for file in os.listdir('/Users/Hallshit/newdir/Finance/Cryptos/historicalCryptos'):

    df = pd.read_csv('/Users/Hallshit/newdir/Finance/Cryptos/historicalCryptos/' + file)
    df = df.tail(30)
    crypto = file[:-4]
    all[crypto] = df['price(USD)']



    # break

pctchCols = []
sma1Cols = []
sma2Cols = []
cumReturnCols = []
for c in cols:
    all[c + ' pct_ch'] = all[c] / all[c].shift(1) - 1
    all[c + ' sma1'] = all[c].rolling(5).mean()
    all[c + ' sma2'] = all[c].rolling(10).mean()
    all[c + ' cum return'] = (1 + all[c + ' pct_ch']).cumprod() - 1
    pctchCols.append(c + ' pct_ch')
    sma1Cols.append(c + ' sma1')
    sma2Cols.append(c + ' sma2')
    cumReturnCols.append(c + ' cum return')

stratCols = []
for c in cols:
    print 1/float(len(cols))
    all[c + ' position'] = np.where(all[c + ' sma1'] > all[c + ' sma2'], 1, 0)
    all[c + ' strategy'] = all[c + ' position'] * all[c + ' pct_ch'] * (1/float(len(cols)))
    stratCols.append(c + ' strategy')

fig, ax = plt.subplots(1)


all['total return'] = all[stratCols].sum(axis=1)
all['cum return'] = (1 + all['total return']).cumprod() - 1
all['cum return'].plot()
# all[cumReturnCols].plot()
print all.tail()
fig.autofmt_xdate()
# all[cols].plot()
#
plt.show()



