import csv
import selenium
from selenium import webdriver

class AlphaVantage():
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://www.alphavantage.co/query?'
        self.data = None
    def get_earnings(self, ticker):
        self.data = requests.get(f'{self.base_url}function=EARNINGS&symbol={ticker}&apikey={self.api_key}')
        return self.data.json()
    def get_income_statement(self, ticker):
        self.data = requests.get(f'{self.base_url}function=INCOME_STATEMENT&symbol={ticker}&apikey={self.api_key}')
        return self.data.json()
    def get_balance_sheet(self, ticker):
        self.data = requests.get(f'{self.base_url}function=BALANCE_SHEET&symbol={ticker}&apikey={self.api_key}')
        return self.data.json()
    def get_cash_flow(self, ticker):
        self.data = requests.get(f'{self.base_url}function=CASH_FLOW&symbol={ticker}&apikey={self.api_key}')
        return self.data.json()
    def get_quote(self, ticker):
        self.data = requests.get(f'{self.base_url}function=GLOBAL_QUOTE&symbol={ticker}&apikey={self.api_key}')
        return self.data.json()
    def get_closing_price(self, ticker, date):
        self.data = requests.get(f'{self.base_url}function=TIME_SERIES_DAILY&symbol={ticker}&apikey={self.api_key}')
        data_json = self.data.json()
        closing_price = data_json['Time Series (Daily)'][date]['4. close']
        return closing_price

def make_directory(ticker):
    import os
    try:
        os.mkdir(f'{ticker}')
    except FileExistsError:
        pass

def make_dirs():
    with open('tickers.csv', 'r') as f:
        reader = csv.reader(f)
        tickers = list(reader)
        for t in tickers:
            make_directory(t[0])

apikey = open('apikey', 'r').read()
AV = AlphaVantage(apikey)

#blahblahblah
#Once I have an API Key: use the class above to get earnings dates and closing prices