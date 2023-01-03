import yfinance as yf
import pandas as pd 
import riskfolio as rp
from typing import List

assets: List[str] = ['DE', 'MSFT', 'HPQ', 'SEE', 'VZ', 'CNP', 'NI', 'T', 'BA']
assets.sort()

data = yf.download(assets,period="1y")
data = data.loc[:,('Adj Close')]
data.columns = assets
print(data)

Y = data[assets].pct_change().dropna()
print(Y)

portfolio = rp.Portfolio(returns=Y)

method_mu: str = 'hist' # Method to estimate expected returns based on historical data.
method_cov: str = 'hist' # Method to estimate covariance matrix based on historical data.

portfolio.assets_stats(method_mu=method_mu, method_cov=method_cov, d=0.94)

def estimate_portfolio ():
# Estimate optimal portfolio:

    model: str ='Classic' # Could be Classic (historical), BL (Black Litterman) or FM (Factor Model)
    rm: str = 'MV' # Risk measure used, this time will be variance
    obj: str = 'Sharpe' # Objective function, could be MinRisk, MaxRet, Utility or Sharpe
    hist: bool = True # Use historical scenarios for risk measures that depend on scenarios
    rf: int = 0 # Risk free rate
    l: int = 0 # Risk aversion factor, only useful when obj is 'Utility'

    w = portfolio.optimization(model=model, rm=rm, obj=obj, rf=rf, l=l, hist=hist)
print("WEights:")
print(w.T)
