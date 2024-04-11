from coding.github.personal.data_projects.company_financials_stock_price_analysis.interfaces.IRequestHandler import IRequestHandler
from coding.github.personal.data_projects.company_financials_stock_price_analysis.interfaces.ISessionHandler import ISessionHandler
from typing import Optional
import requests
import time

class YFRequestHandler(IRequestHandler):

      def __init__(self, session_handler:ISessionHandler, url:str, headers:str):
            self._session_handler = session_handler
            self._url = url
            self._headers = headers

      def url(self, ticker:str) -> str:
            url = self._url
            url = url.replace("[TICKER]", ticker)
            url = url.replace("[CRUMB]", self._session_handler.crumb)
            return url

      def headers(self, ticker:str) -> dict:
            headers = self._headers
            headers["Referer"] = headers["Referer"].replace("[TICKER]", ticker)
            return headers

      def payload(self):
            NotImplemented

      def new_session(self):
            self._session_handler.session = self._session_handler.new_session()
            return 
      
      def new_crumb(self):
            self._session_handler.crumb = self._session_handler.new_crumb()
            return

      def request_data(self, ticker:str, retries=0, max_retries=3) -> Optional[requests.models.Response]:
            if retries >= max_retries:
                  print(f"REQUEST FAILED :: aborting request.")
                  return
            self._session_handler.session.headers = self.headers(ticker=ticker)
            response = self._session_handler.session.get(self.url(ticker=ticker))
            if response.status_code != 200:
                  print(f"REQUEST FAILED :: STATUS CODE: {response.status_code} :: RETRIES : {retries}")
                  retries += 1
                  self._session_handler.new_session()
                  time.sleep(1)
                  self._session_handler.new_crumb()
                  time.sleep(1)
                  return self.request_data(ticker, retries)
            else:
                  return response
