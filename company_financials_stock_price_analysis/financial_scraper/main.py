
from handlers.YFSessionHandler import YFSessionHandler
from factories.YFRequestFactory import YFRequestFactory
import time
import os

def main():
      #ticker_list = functions.load_tickers()
      ticker_list = ["TSLA", "AAPL"]

      session_handler = YFSessionHandler()
      #print(session_handler.session, session_handler.crumb)

      #request_handler = YFRequestFactory.make_request_object(session_handler, "statistics")
      #response = request_handler.request_data(ticker=ticker)

      request_types = [
            "annual_balance_sheet",
            "quarterly_balance_sheet",
            "annual_cash_flow",
            "quarterly_cash_flow",
            "annual_income_statement",
            "quarterly_income_statement",
            "statistics",
            "analysis"
      ]

      request_handlers = []
      for request_type in request_types:
            request_handlers.append(YFRequestFactory.make_request_object(session_handler, request_type))
      
      i = 0
      for ticker in ticker_list:
            for request_handler in request_handlers:
                  print("i =", i)
                  print("/n Sleeping 3 seconds")
                  time.sleep(3)
                  response = request_handler.request_data(ticker=ticker)
                  with open(f"./portfolio_work/data_projects/company_financials_stock_price_analysis/financial_scraper/data/data{i}.text", 'w') as f:
                        f.write(response.text)
                  i += 1
      return 

if __name__=="__main__":
      main()