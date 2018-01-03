import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import combineData
import SingleCrypto




cols, df = combineData.combineData()

helper = combineData.AllCryptoDF(cols, df)



cryptos = helper.concatDataframes()

cryptos = cryptos.iloc[::7, :]

# print cryptos

stratReturns = []
cumprods = []
for c in cols:
    cryptos[c + ' long'] = np.where(cryptos[c + ' rank'] > 8, 1, 0)
    cryptos[c + ' strat returns'] = cryptos[c + ' long'] * cryptos[c + ' BTreturns'] * .2
    cryptos[c + ' cum prod'] = (1 + cryptos[c + ' BTreturns']).cumprod() - 1
    cumprods.append(c + ' cum prod')
    stratReturns.append(c + ' strat returns')

cryptos['total Strat'] = cryptos[stratReturns].sum(axis=1)

cryptos['cum prod'] = (1 + cryptos['total Strat']).cumprod() - 1
print cryptos.tail()

cryptos[['cum prod', 'btc cum prod', 'ltc cum prod', 'dash cum prod', 'eth cum prod']].plot()

plt.show()



