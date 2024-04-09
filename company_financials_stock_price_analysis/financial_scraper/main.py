import functions
import json

from handlers.YFSessionHandler import YFSessionHandler
from handlers.YFRequestHandler import YFRequestHandler
from company_financials_stock_price_analysis.financial_scraper.request_objects.RequestAnnualBalanceSheet import RequestAnnualBalanceSheet

def main():
      #ticker_list = functions.load_tickers()
      ticker = "TSLA"

      session_handler = YFSessionHandler()
      request_object = YFRequestFactory.make_request_object(request_object_type="analysis", session_handler=session_handler)

      request_handler = YFRequestHandler()
      session = session_handler.new_session()
      response, session = request_handler.request_data(ticker=ticker, request_object=request_object, session_handler=session_handler, session=session)



















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