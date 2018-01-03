import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/Hallshit/newdir/Finance/Cryptos/historicalCryptos/btc.csv')
df['marketcap(USD)'].tail(100).plot()
plt.show()

