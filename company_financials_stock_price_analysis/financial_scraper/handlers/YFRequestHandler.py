from company_financials_stock_price_analysis.financial_scraper.request_objects.IRequest import IRequest
from handlers.IRequestHandler import IRequestHandler
from handlers.ISessionHandler import ISessionHandler
import requests
from typing import Optional


class YFRequestHandler(IRequestHandler):

    def __init__(self):
        pass

    def request_data(
            self, ticker:str, request_object:IRequest, session_handler:ISessionHandler, 
            session = None, retries=1, max_retries=10
    ) -> Optional[requests.models.Response]:

            if retries >= max_retries:
                print(f"REQUEST FAILED :: aborting request.")
                return None, session
            if session == None:
                session = session_handler.new_session()   
            session.headers = request_object.headers(ticker=ticker)
            response = session.get(request_object.url(ticker=ticker))
            if response.status_code != 200:
                print(f"REQUEST FAILED :: STATUS CODE: {response.status_code} :: RETRIES : {retries}")
                retries += 1
                session = session_handler.new_session()
                return self.request_data(request_object, session_handler, session, retries)
            else:
                return response, session
