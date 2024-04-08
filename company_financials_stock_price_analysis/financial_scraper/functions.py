import pandas
import json

def load_tickers():
    csv = pandas.read_csv("./company_ticker_list.csv")
    ticker_list = csv.iloc[:,0] 
    return list(ticker_list)
"""
def download_and_save_data(
        ticker_list: list[str],
        request_handler: interfaces.RequestHandler,
        session_handler: interfaces.SessionHandler,
        save_handlers: interfaces.SaveHandler,
        request_objects: list[interfaces.APIRequest]
    ):
    for ticker in ticker_list:
        for request_object in request_objects:
            request_object.ticker = ticker
            request_handler.request_data(request_object, session_handler)
            for save_handler in save_handlers:
                save_handler.save(json.loads(request_handler.response.text))

"""
