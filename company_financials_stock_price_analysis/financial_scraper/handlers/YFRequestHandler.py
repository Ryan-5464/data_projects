from interfaces.IRequestHandler import IRequestHandler
from interfaces.ISessionHandler import ISessionHandler
from typing import Optional
import requests
import time

class YFRequestHandler(IRequestHandler):

      def __init__(self, session_handler:ISessionHandler, url:str, headers:str, product_type:str):
            self._session_handler = session_handler
            self._url = url
            self._headers = headers
            self._product_type = product_type

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

      def request_data(self, ticker:str, root_dir:str, retries=0, max_retries=1) -> Optional[requests.models.Response]:
            if retries >= max_retries:
                  print(f"REQUEST FAILED :: aborting request.")
                  with open(f"{root_dir}/state/missing_ticker.txt",'a') as f:
                        f.write(f"[{ticker}]")
                  return
            self._session_handler.session.headers = self.headers(ticker=ticker)
            print("/n Headers =:", self._session_handler.session.headers)
            print("/n Url =:", self.url(ticker=ticker))
            response = self._session_handler.session.get(self.url(ticker=ticker))
            if response.status_code != 200:
                  print(f"REQUEST FAILED :: STATUS CODE: {response.status_code} :: RETRIES : {retries}")
                  retries += 1
                  self._session_handler.new_session()
                  time.sleep(3)
                  self._session_handler.new_crumb()
                  time.sleep(3)
                  return self.request_data(ticker, root_dir, retries)
            else:
                  return response
            
      def get_product_type(self) -> str:
            return self._product_type
