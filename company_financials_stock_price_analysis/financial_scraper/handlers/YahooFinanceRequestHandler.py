from company_financials_stock_price_analysis.financial_scraper.request_objects.IRequestObject import IRequest
from handlers.IRequestHandler import IRequestHandler
from handlers.ISessionHandler import ISessionHandler
import requests
from typing import Optional


class YahooFinanceRequestHandler(IRequestHandler):

    def request_data(
                  request_object: IRequest, 
                  session_handler: ISessionHandler, 
                  session = None,
                  retries=1, 
                  max_retries=10
      ) -> Optional[requests.models.Response]:
            if retries >= max_retries:
                print(f"REQUEST FAILED :: aborting request.")
                return     
            if session == None:
                session = session_handler.new_session()   
            session.headers = request_object.headers
            response = session.get(request_object.url)
            if response.status_code != 200:
                print(f"REQUEST FAILED :: STATUS CODE: {response.status_code} :: RETRIES : {retries}")
                retries += 1
                session = session_handler.new_session()
                return YahooFinanceRequestHandler.request_data(request_object, session_handler, session, retries)
            else:
                return response
