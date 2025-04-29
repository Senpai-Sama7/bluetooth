import asyncio
from bleak import BleakScanner
from bluetooth import discover_devices
from scapy.all import sniff, BluetoothHCISocket, HCI_Event_Hdr
import logging

class BluetoothScanner:
    def __init__(self, interface='hci0'):
        self.interface = interface
        self.logger = logging.getLogger('scanner')

    def classic_scan(self, duration=8):
        """Discover classic Bluetooth devices"""
        devices = []
        try:
            for addr, name in discover_devices(duration=duration, lookup_names=True, flush_cache=True):
                devices.append({
                    "address": addr,
                    "name": name or "Unknown",
                    "type": "BR/EDR",
                    "protocol": "Classic"
                })
        except Exception as e:
            self.logger.error(f"Classic scan failed: {str(e)}")
        return devices

    async def ble_scan(self, duration=5):
        """Discover BLE devices"""
        devices = []
        try:
            async with BleakScanner() as scanner:
                await asyncio.sleep(duration)
                for d in scanner.discovered_devices:
                    devices.append({
                        "address": d.address,
                        "name": d.name or "Unknown",
                        "type": "BLE",
                        "rssi": d.rssi,
                        "metadata": d.metadata
                    })
        except Exception as e:
            self.logger.error(f"BLE scan failed: {str(e)}")
        return devices

    def sniff_ads(self, duration=10):
        """Sniff advertising packets using Scapy"""
        packets = []
        def packet_handler(pkt):
            if pkt.haslayer(HCI_Event_Hdr):
                packets.append({
                    "timestamp": pkt.time,
                    "type": pkt.type,
                    "data": bytes(pkt).hex()
                })
        
        try:
            with BluetoothHCISocket(0) as sock:
                sniff(opened_socket=sock, prn=packet_handler, timeout=duration)
        except Exception as e:
            self.logger.error(f"Sniffing failed: {str(e)}")
        return packets
