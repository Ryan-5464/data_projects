import pandas
import requests

def load_tickers():
    csv = pandas.read_csv("company_ticker_list.csv")
    ticker_list = csv.iloc[:,0] 
    return list(ticker_list)

def get_company_statistics(ticker):
    statistics_html = requests.get(f"https://uk.finance.yahoo.com/quote/{ticker}/key-statistics")
    company_statistics = CompanyStatistics()
    return company_statistics

def get_company_income_statement(ticker):
    income_statement_html = requests.get("https://uk.finance.yahoo.com/quote/{ticker}/financials").text
    return income_statement_html

def get_company_balance_sheet(ticker):
    balance_sheet_html = requests.get("https://uk.finance.yahoo.com/quote/{ticker}/balance-sheet").text
    return balance_sheet_html

def get_company_cash_flow(ticker):
    cash_flow_html = requests.get("https://uk.finance.yahoo.com/quote/{ticker}/cash-flow").text
    return cash_flow_html
