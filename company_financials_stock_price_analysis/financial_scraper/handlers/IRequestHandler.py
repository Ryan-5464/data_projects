from abc import ABC, abstractmethod
from handlers.ISessionHandler import ISessionHandler
from company_financials_stock_price_analysis.financial_scraper.request_objects.IRequestObject import IRequest
import requests
from typing import Optional



class IRequestHandler(ABC):

      @staticmethod
      @abstractmethod
      def request_data(
            request_object: IRequest,
            session_handler: ISessionHandler,
            *args,
            **kwargs 
      ) -> Optional[requests.models.Response]:
            NotImplementedError