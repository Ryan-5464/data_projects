
from handlers.YFSession import YFSession

def main():
      #ticker_list = functions.load_tickers()
      ticker = "TSLA"

      session_handler = YFSession()
      print(session_handler.session, session_handler.crumb)
      
      return 

if __name__=="__main__":
      main()