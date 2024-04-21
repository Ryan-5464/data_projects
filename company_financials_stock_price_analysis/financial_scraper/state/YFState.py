from interfaces.IState import IState
import pandas
import json


class YFState(IState):

      def __init__(self, root_dir):
            self.root_dir = root_dir
            self.ticker_list = YFState.__load_tickers(self.root_dir)
            self.ticker_count = len(self.ticker_list)

      @staticmethod
      def __load_tickers(root_dir):
            csv = pandas.read_csv(f"{root_dir}/tickers/company_ticker_list.csv")
            ticker_list = csv.iloc[:,0] 
            return list(ticker_list)
      
      def next_input(self):
            next_ticker = self.ticker_list[-1]
            self.ticker_list = self.ticker_list[:-1]
            return next_ticker

      def save_state(self):
            state = {
                  "ticker_list": self.ticker_list,
                  "ticker_count": self.ticker_count
            }
            with open(f"{self.root_dir}/state/current_state.json", 'w') as f:
                  f.write(json.dumps(state, indent=4))

      def load_state(self):
            try:
                  with open(f"{self.root_dir}/state/current_state.json", 'r') as f:
                        state = json.loads(f.read())
                  self.ticker_list = state.get("ticker_list")
                  self.ticker_count = state.get("ticker_count")
            except FileNotFoundError:
                  pass

      def current_progress(self):
            progress = round(((self.ticker_count-len(self.ticker_list)) / self.ticker_count) * 100, 2)
            print(f"\n [{self.ticker_count-len(self.ticker_list)}/{self.ticker_count}] Progress {progress}% \n")