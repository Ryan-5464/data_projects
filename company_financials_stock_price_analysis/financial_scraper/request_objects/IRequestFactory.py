from abc import ABC, abstractmethod
from IRequest import IRequest


class IRequestFactory(ABC):

    @classmethod
    @abstractmethod
    def make_request_object(cls, *args, **kwargs) -> IRequest:
        NotImplementedError