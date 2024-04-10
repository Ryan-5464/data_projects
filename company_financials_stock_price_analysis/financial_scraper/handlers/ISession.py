from abc import ABC, abstractmethod
import requests

class ISession(ABC):

      session: requests.Session

      @classmethod
      @abstractmethod
      def new_session(cls) -> requests.Session:
            NotImplementedError
