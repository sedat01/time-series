import yfinance as yf
import pandas as pd
import riskfolio as rp
from typing import List
import matplotlib.pyplot as plt
from pycaret import regression

assets: List[str] = ["DE", "MSFT"]
assets.sort()

data = yf.download(assets, period="10y", threads=False)

data = data.loc[:, ("Adj Close")]
data.columns = assets


def estimate_portfolio(data):
    # Estimate optimal portfolio:
    Y = data.pct_change().dropna()
    print(Y)

    portfolio = rp.Portfolio(returns=Y)

    method_mu: str = "hist"  
    method_cov: str = "hist"

    portfolio.assets_stats(method_mu=method_mu, method_cov=method_cov, d=0.94)

    model: str = "Classic"  # Could be Classic (historical), BL (Black Litterman) or FM (Factor Model)
    rm: str = "MV"  # Risk measure used, this time will be variance
    obj: str = "Sharpe"  # Objective function, could be MinRisk, MaxRet, Utility or Sharpe
    hist: bool = True  # Use historical scenarios for risk measures that depend on scenarios
    rf: int = 0  # Risk free rate
    l: int = 0  # Risk aversion factor, only useful when obj is 'Utility'

    w = portfolio.optimization(model=model, rm=rm, obj=obj, rf=rf, l=l, hist=hist)
    return w


def plot_portfolio(w):
    ax = plt.subplot()
    ax = rp.plot_pie(
        w=w,
        title="Sharpe Mean Variance",
        nrow=25,
        cmap="tab20",
        height=6,
        width=10,
        ax=None,
    )
    plt.show()


calculated_portfolio = estimate_portfolio(data)
plot_portfolio(calculated_portfolio)
