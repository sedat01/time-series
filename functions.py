import yfinance
from prophet import Prophet
import riskfolio as rp
import matplotlib.pyplot as plt

def get_current_prices (stock: str,period: str = "5y"):
    '''
    Function to download and prepare the data for current prices
    '''
    data = yfinance.download(stock, period=period)[["Adj Close"]]
    data = data.reset_index()
    data = data.rename(columns={"Date":"ds","Adj Close":"y"})
    return data


def get_future_prices (historical_data,period: int = 365):
    '''
    Function to predict the prices
    '''
    model = Prophet()
    model.fit(historical_data)
    future_dates = model.make_future_dataframe(periods=period)
    future_prices = model.predict(future_dates)
    return future_prices[["ds","yhat"]]

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
    '''
    Plot portfolio
    '''
    ax = plt.figure()
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