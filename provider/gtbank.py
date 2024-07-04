from .base import BaseFactory


class GTBank(BaseFactory):

    def __init__(self):
        print("Initialized GTBank Payment")

    def verify_payment(self):
        pass

    def money_transfer(self):
        print("GTBank Sending Money")
