import subprocess
from .utils import logger

class Attacks:
    def __init__(self, interface: str):
        self.interface = interface

    def l2cap_flood(self, address: str):
        # subprocess l2ping flood
        pass

    def crack_pin(self, address: str):
        # call Crackle wrapper
        pass

    def bluejack(self, address: str, message: str):
        # OBEX push via PyOBEX
        pass
