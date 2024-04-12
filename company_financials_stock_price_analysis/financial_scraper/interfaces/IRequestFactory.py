from abc import ABC, abstractmethod
from interfaces.IRequestHandler import IRequestHandler


class IRequestFactory(ABC):

    @classmethod
    @abstractmethod
    def make_request_object(cls, *args, **kwargs) -> IRequestHandler:
        NotImplementedError