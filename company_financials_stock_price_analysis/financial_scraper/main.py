
from handlers.YFSessionHandler import YFSessionHandler
from factories.YFRequestFactory import YFRequestFactory


def main():
      #ticker_list = functions.load_tickers()
      ticker = "TSLA"

      session_handler = YFSessionHandler()
      print(session_handler.session, session_handler.crumb)

      request_handler = YFRequestFactory.make_request_object(session_handler, "statistics")
      response = request_handler.request_data(ticker=ticker)
      
      return 

if __name__=="__main__":
      main()