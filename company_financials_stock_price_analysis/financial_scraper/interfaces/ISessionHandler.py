from abc import ABC, abstractmethod
import requests
from typing import Optional

class ISessionHandler(ABC):

      session: requests.Session
      crumb: str

      @abstractmethod
      def new_session(self):
            NotImplementedError

      @abstractmethod
      def new_crumb(self):
            NotImplementedError