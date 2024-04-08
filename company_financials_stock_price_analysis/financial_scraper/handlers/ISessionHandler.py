from abc import ABC, abstractmethod
import requests

class ISessionHandler(ABC):

      @classmethod
      @abstractmethod
      def new_session(cls) -> requests.Session:
            NotImplementedError
