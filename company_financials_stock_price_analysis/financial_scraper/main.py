import functions
import json

from handlers.YahooFinanceSessionHandler import YahooFinanceSessionHandler
from handlers.YahooFinanceRequestHandler import YahooFinanceRequestHandler
from company_financials_stock_price_analysis.financial_scraper.request_objects.RequestAnnualBalanceSheet import RequestAnnualBalanceSheet

def main():
      #ticker_list = functions.load_tickers()
      ticker = "TSLA"
      response = YahooFinanceRequestHandler.request_data(
            request_object=RequestAnnualBalanceSheet(ticker),
            session_handler=YahooFinanceSessionHandler
      )
      data = json.loads(response.text)
      print(data)
      #formatted_data = YahooFinanaceBalanceSheetParser.parse(data)
      return

      request_handler = interfaces.YahooFinanceRequestHandler()
      session_handler = interfaces.YahooFinanceSessionHandler()
      save_handlers = [
            interfaces.LocalSaveHandler(),
            interfaces.PostgresSaveHandler(),
            interfaces.S3SaveHandler()
      ]
      request_objects = [
            interfaces.RequestBalanceSheet(),
            interfaces.YahooFinanceRequestCashFlow(),
            interfaces.YahoooFinanceRequestIncomeStatement(),
            interfaces.YahooFinanceRequestAnalysis(),
            interfaces.YahooFinanceRequestStatistics()
      ]
      functions.download_and_save_data(ticker_list, request_handler, session_handler, save_handlers, request_objects)
      return 

if __name__=="__main__":
      main()