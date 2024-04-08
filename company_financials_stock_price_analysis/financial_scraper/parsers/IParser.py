from abc import ABC, abstractmethod


class IParser(ABC):

      @staticmethod
      @abstractmethod
      def parse_data(data: dict) -> dict:
            NotImplementedError