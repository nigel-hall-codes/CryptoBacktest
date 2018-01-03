import pandas as pd
import numpy as np
import os
import SingleCrypto



def combineData():
    cols = []
    for file in os.listdir('/Users/Hallshit/newdir/Finance/Cryptos/historicalCryptos'):
        cols.append(file[:-4])

    all = pd.DataFrame(columns=cols)

    for file in os.listdir('/Users/Hallshit/newdir/Finance/Cryptos/historicalCryptos'):
        # if file == 'doge.csv':
        #     continue
        df = pd.read_csv('/Users/Hallshit/newdir/Finance/Cryptos/historicalCryptos/' + file)
        df = df.tail(40)
        crypto = file[:-4]
        all[crypto] = df['marketcap(USD)']
    return cols, all




class AllCryptoDF:
    def __init__(self, cols, df):
        self.df = df
        self.cols = cols
        self.sma1Cols = []
        self.sma2Cols = []
        self.smaDiffCols = []
        self.priceCols = []
        self.BTReturnCols = []
        self.ranks = []

        self.getColNames()
        self.cDf = pd.DataFrame()



    def getColNames(self):
        for c in self.cols:
            self.sma1Cols.append(c + ' sma1')
            self.sma2Cols.append(c + ' sma2')
            self.smaDiffCols.append(c + ' smaDiff')
            self.priceCols.append(c + ' price')
            self.BTReturnCols.append(c + ' BTreturns')

    def getRanks(self, df):
        print df

        ranks = df[self.smaDiffCols].rank(axis=1)

        for c in self.cols:
            df[c + ' rank'] = ranks[c + ' smaDiff']
            self.ranks.append(c + ' rank')
        return df


    def concatDataframes(self):

        self.cDf = SingleCrypto.SingleCryptoTA(self.df[self.cols[0]], 5, 10).df

        for c in self.cols[1:]:
            self.cDf = pd.concat([self.cDf, SingleCrypto.SingleCryptoTA(self.df[c], 5, 10).df], axis=1)

        self.cDf = self.getRanks(self.cDf)
        return self.cDf





