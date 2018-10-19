import random

class Device:
    peer_MAC = []       # list of strings
    peer_name = []      # list of strings
    peer_latlon = []    # stores tuple of lat, lon in a form of (version, lat, lon)
    lat_mean = 0
    lon_mean = 0
    ver = 0         # version of lat, lon
    lat = 0
    lon = 0

    def __init__(self):
        self.lat = random.random() * 100
        self.lon = random.random() * 100

    def scan(self):
        service = DiscoveryService()
        devices = service.discover(2)

        for address, name in devices.items():
            print("name: {}, address: {}".format(name, address))

    def register(self):
        service = DiscoveryService()
        devices = service.discover(2)
        for address, name in devices.items():
            if "boy" == name[:3] :
                self.send_latlon(address)
                peer_MAC.append(address)
                peer_name.append(name)

    def send_latlon(self, address):
        port = 1
        bd_addr = address
        sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        sock.connect((bd_addr, port))
        obj = {"address": address, "name": name, "ver": ver, "lat": lat, "lon": lon}
        sock.send(obj)
        sock.close()

    def accept_latlon(self):
        server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        port = 1
        server_sock.bind(("",port))
        server_sock.listen(1)

        client_sock,address = server_sock.accept()
        print "Accepted connection from ",address

        data = client_sock.recv(1024)
        print("data received = "+str(data))

        if not (data.address in self.peer_MAC and "boy" == data.name[:3]):
            peer_MAC.append(address)
            peer_name.append(name)
            peer_latlon.append((-1, 0, 0))

        idx = peer_MAC.index(data.address)
        if peer_latlon[idx][0] < data.ver:
            peer_MAC[idx] = (data.ver, data.lat, data.lon)

        client_sock.close()
        server_sock.close()
