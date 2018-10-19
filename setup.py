import bluetooth
from bluetooth.ble import DiscoveryService, GATTRequester, BeaconService
import sys
import time
import Beacon

def register():


def beacon():
    service = BeaconService()

    service.start_advertising("11111111-2222-3333-4444-555555555555",
                1, 1, 1, 200)
    time.sleep(15)
    service.stop_advertising()

    print("Done.")

def beacon_scan():
    service = BeaconService()
    devices = service.scan(2)

    for address, data in list(devices.items()):
        b = Beacon(data, address)
        print(b)

    print("Done.")
