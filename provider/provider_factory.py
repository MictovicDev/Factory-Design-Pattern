from .gtbank import GTBank
from .airvend import AirVend
from .shago import Shago

class ProviderFactory:
    @staticmethod
    def create_provider(choice):
        try:
            if choice == 'shago':
                return Shago()
            elif choice == 'airvend':
                return AirVend()
            elif choice == 'gtbank':
                return GTBank()
            raise NotImplementedError
        except NotImplementedError:
            print("Bank Service Not Yet Implemented")

            