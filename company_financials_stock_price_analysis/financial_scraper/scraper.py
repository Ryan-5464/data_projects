import time
import functions as f
import objects as o


def scraper():
    ticker_list = f.load_tickers()
    print(ticker_list)
    ticker_list = ["TSLA"]
    for ticker in ticker_list:
        company_statistics = f.get_company_statistics(ticker)
        balance_sheet = f.get_company_balance_sheet(ticker)
        income_statement = f.get_company_income_statement(ticker)
        cash_flow = f.get_company_cash_flow(ticker)


if __name__=="__main__":
    scraper()