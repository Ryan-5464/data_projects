from abc import ABC, abstractmethod
from typing import Optional

class IRequestObject(ABC):

      url: str
      headers: dict
      payload: Optional[dict]
      proxies: Optional[dict]

      @abstractmethod
      def url(cls, *args, **kwargs) -> str:
            NotImplementedError

      @abstractmethod
      def headers(cls, *args, **kwargs) -> dict:
            NotImplementedError

      @abstractmethod
      def payload(cls, *args, **kwargs) -> dict:
            NotImplementedError

      @abstractmethod
      def proxies(cls, *args, **kwargs) -> dict:
            NotImplementedError


