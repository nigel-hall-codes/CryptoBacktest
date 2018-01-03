import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SingleCryptoTA:
    def __init__(self, df, sma1Per, sma2Per):

        self.name = df.name

        # _ indicates name of column
        self._price = self.name + ' price'
        self._sma1 = self.name + ' sma1'
        self._sma2 = self.name + ' sma2'
        self._smaDiff = self.name + ' smaDiff'
        self._BTreturns = self.name + ' BTreturns'

        self.df = pd.DataFrame(columns=[self._price, self._sma1, self._sma2, self._BTreturns])
        self.df[self._price] = df
        self.sma1Per = sma1Per
        self.sma2Per = sma2Per
        self.holdPeriod = 7  # in days

        self.__sma__()
        self.__backtestReturns__()

    def __sma__(self):
        self.df[self._sma1] = self.df[self._price].rolling(self.sma1Per).mean()
        self.df[self._sma2] = self.df[self._price].rolling(self.sma2Per).mean()
        self.df[self._smaDiff] = self.df[self._sma1] / self.df[self._sma2] - 1


    def __backtestReturns__(self):
        self.df[self._BTreturns] = (self.df[self._price].shift(-self.holdPeriod) / self.df[self._price].shift(-1)) - 1





