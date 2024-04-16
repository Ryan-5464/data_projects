
from handlers.YFSessionHandler import YFSessionHandler
from factories.YFRequestFactory import YFRequestFactory
from state.YFState import YFState
import time
import os
import json 

def main():

      ROOT_DIR = os.path.dirname(__file__)

      state = YFState(root_dir=ROOT_DIR)
      state.load_state()

      session_handler = YFSessionHandler()

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
      
      sleep_seconds = 5
      while len(state.ticker_list) > 0:

            ticker = state.next_input()
            state.current_progress()

            try:
                  os.mkdir(f"{ROOT_DIR}/data_lake/{ticker}")
            except FileExistsError:
                  pass

            for request_handler in request_handlers:

                  time.sleep(sleep_seconds)
                  response = request_handler.request_data(ticker=ticker)

                  with open(f"{ROOT_DIR}/data_lake/{ticker}/{request_handler.get_product_type()}.json", 'w') as f:
                        f.write(json.dumps(response.text, indent=4))

            state.save_state()

      return 

if __name__=="__main__":
      main()