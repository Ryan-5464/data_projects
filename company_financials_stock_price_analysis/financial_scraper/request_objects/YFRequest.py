from IRequest import IRequest
from company_financials_stock_price_analysis.financial_scraper.handlers.ISessionHandler import ISessionHandler
from typing import Optional



class YFRequest(IRequest):

      def __init__(self, url:str, headers:str, crumb=None):
            self._url = url
            self._headers = headers
            self._crumb

      def url(self, ticker:str) -> str:
            url = self._url
            url = url.replace("[TICKER]", ticker)
            url = url.replace("[CRUMB]", self._crumb)
            return url

      def headers(self, ticker:str) -> dict:
            headers = self._headers
            headers["Referer"] = headers["Referer"].replace("[TICKER]", ticker)
            return headers

      def payload(self):
            NotImplemented


