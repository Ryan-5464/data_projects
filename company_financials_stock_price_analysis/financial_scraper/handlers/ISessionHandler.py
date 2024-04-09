from abc import ABC, abstractmethod
import requests

class ISessionHandler(ABC):

      session: requests.Session

      @classmethod
      @abstractmethod
      def new_session(cls) -> requests.Session:
            NotImplementedError
