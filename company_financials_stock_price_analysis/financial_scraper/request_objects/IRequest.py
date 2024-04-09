from abc import ABC, abstractmethod
from typing import Optional
import requests



class IRequest(ABC):

      _url: str
      _headers: dict
      _crumb: str

      @abstractmethod
      def url(self, *args, **kwargs) -> str:
            NotImplementedError

      @abstractmethod
      def headers(self, *args, **kwargs) -> Optional[dict]:
            NotImplementedError

      @abstractmethod
      def payload(self, *args, **kwargs) -> Optional[dict]:
            NotImplementedError

      @abstractmethod
      def request_data(self, *args, **kwargs) -> Optional[requests.models.Response]:
            NotImplementedError

