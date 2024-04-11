from abc import ABC, abstractmethod
from typing import Optional
import requests
from ISessionHandler import ISessionHandler


class IRequestHandler(ABC):

      _session_handler: ISessionHandler
      _url: str
      _headers: dict

      @abstractmethod
      def url(self, *args, **kwargs) -> str:
            NotImplementedError

      @abstractmethod
      def headers(self, *args, **kwargs) -> dict:
            NotImplementedError

      @abstractmethod
      def payload(self, *args, **kwargs) -> Optional[dict]:
            NotImplementedError

      @abstractmethod
      def new_session(self, *args, **kwargs):
            NotImplementedError

      @abstractmethod
      def new_crumb(self, *args, **kwargs):
            NotImplementedError

      @abstractmethod
      def request_data(self, *args, **kwargs) -> Optional[requests.models.Response]:
            NotImplementedError

