from cyberhead.strategies.strattest import strattest
from backtesting import Backtest, Strategy
from backtesting.test import SMA, GOOG


class SmaCross(Strategy):
    def init(self):
        Close = self.data.Close
        self.ma1 = self.I(SMA, Close, 10)
        self.ma2 = self.I(SMA, Close, 20)

    def next(self):
        strattest.iterate(self, strattest.data)


bt = Backtest(strattest.broker.prices,
              SmaCross,
              cash=strattest.broker.cash,
              commission=strattest.broker.commission)
bt.run()
bt.plot()

print('Backtest performed!')
