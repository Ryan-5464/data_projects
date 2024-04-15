import json


def request_annual_balance_sheet():
      with open("./data/data0.text") as f:
            data = json.loads(f.read()) 
      return data

data = request_annual_balance_sheet()

