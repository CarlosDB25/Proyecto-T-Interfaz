from abc import ABC, abstractmethod


class PCrud(ABC):

    @abstractmethod
    def create(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def searchBy(self, **kwargs):
        raise NotImplementedError