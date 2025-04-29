from scapy.all import *
from .utils import logger, save_session_json

class GATT:
    def __init__(self, interface: str):
        self.interface = interface

    async def read_all(self, address: str):
        # use bleak for async GATT operations
        pass

    async def write(self, address: str, handle: int, data: bytes):
        # write characteristic
        pass
