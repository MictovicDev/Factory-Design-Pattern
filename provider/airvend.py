from .base import BaseFactory


class AirVend(BaseFactory):

    def __init__(self):
        print("Initialized AirVend Payment")

    def verify_payment(self):
        pass

    def money_transfer(self):
        print("AirVend Sending Money")