from .base import BaseFactory


class Shago(BaseFactory):
    def __init__(self):
        print("Initialized Shago Payment")
        
    def verify_payment(self):
        pass

    def money_transfer(self):
        print("Shago Sending Money")