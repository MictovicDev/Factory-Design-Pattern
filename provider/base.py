from abc import ABC, abstractmethod

class BaseFactory(ABC):
    @abstractmethod
    def verify_payment(self):
        pass