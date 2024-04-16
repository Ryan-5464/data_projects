from abc import ABC, abstractmethod

class IState(ABC):

      @abstractmethod
      def save_state(self):
            NotImplementedError

      def load_state(self):
            NotImplementedError

      