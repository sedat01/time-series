# Simple time series price predictor for stocks, bonds etc.

This is a simple predictor for stock market prices.

Disclaimer: This should not be taken as a real investing advice!! I DO NOT bear any responsibility for any gains or losses made with it. This is meant to be as an exercice in time series modelling!

## Installation

Current version is a jupyter notebook, therefore you need and IDE capable of running those, for example Visual Studio Code or Pycharm. On top of that you need the following:

Tested on Python 3.10.8

* yFinance - to download the current prices from Yahoo Finance
* prophet -  as in Facebook Prophet, you can just "pip install prophet" in terminal
* riskfolio - same as the above
* pandas, numpy and matplotlib

That's all!

## Usage

Just start the main.ipynb

The second cell contains the parameters:

* Stocks - list with stocks to include in the portfolios
* histotical_period = period to look back
* future_period = period to predict in number of days

After setting the parameters you can just click "Run all cells" in your IDE. The program will calculate the best distribution of assets using Sharpe objective and mean variance risk assesment. You can see the generated graphs with recommended asset distribution in your portfolio, separately for the data based on current prices and the predicticted prices. you can also see line plots for the prices vs the time.

You can find an excel spreadsheet with a list of valid ticker symbols in the repo.

## Known issues

Not yet, feel free to contact me:

## Developer

Sedat Mehmed, ML Engineer trainee @ Becode Gent

sedat-mehmed@becode.xyz
