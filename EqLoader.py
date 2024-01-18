import pandas as pd
import yfinance as yf
import pandas_datareader.data as web

class StockPriceManager:
    
    def __init__(self) -> None:
        pass
    
    def download_historical_prices(self, symbol, start_date, end_date):
        ticker = yf.Ticker(symbol)
        df = ticker.history(start=start_date, end=end_date)
        closing_prices = df['Close']
        return closing_prices

if __name__ == "__main__":
    spm = StockPriceManager()
    prices = spm.download_historical_prices('AAPL', '2019-01-01', '2020-01-01')
    print(prices)