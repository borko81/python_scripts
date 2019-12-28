import sys
from pprint import pprint


class GetInfo:
    """ Class Get ip and mac from
    terminal, to check validity of them"""

    def __init__(self):
        try:
            self._ip = sys.argv[1]
            self._mak = sys.argv[2]
        except IndexError as e:
            print(e)
            sys.exit()

    def check_ip(self):
        # Check ip is valid, check all is number and first
        # is between 0 and 255
        ips = self._ip.split(".")
        if len(ips) == 4 and all(i.isdigit() for i in ips) and (1 <= int(ips[0]) <= 255):
            return True
        else:
            print(f"[-] ip {self._ip} not recognize as valid ip address")
            sys.exit()
            raise

    def check_mask(self):
        # Validate mask
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
        mask = self._mak.split(".")

        if (len(mask) == 4) and all(i.isdigit() and int(i) in masks for i in mask) and (
            int(mask[0]) == 255 and (
                int(mask[0]) >= int(mask[1]) >= int(mask[2]) >= int(mask[3]))):
            return True
        else:
            print(f"[-] {self._mak} not looked good")
            sys.exit()
            raise

    def result(self):
        if self.check_ip() and self.check_mask():
            return (self._ip, self._mak)
        else:
            print("Gain Error")
            sys.exit()
            raise

    def __repr__(self):
        return f"IP: {self._ip} MAK: {self._mak}"


class CalculateSubnet:
    """Return number of hosts and netmask if filed valid netmask address"""

    def __init__(self, data):
        self._ip, self._mask = data

    def calc_subnet(self):
        result = "".join([bin(int(i)).lstrip('0b').zfill(8)
                          for i in self._mask.split(".")])
        # Use to check netmask and hosts
        zeros = result.count('0')
        # Netmask for example: /26
        netmask = 32 - zeros
        # substract gateway and broadcast to get hosts
        hosts = abs(2 ** zeros - 2)
        return (zeros, netmask, hosts)

    def calc_broadcast(self):
        """ Calculate broadcast and network address """
        zeros, netmask, hosts = self.calc_subnet()
        result = "".join([bin(int(i)).lstrip('0b').zfill(8)
                          for i in self._ip.split(".")])

        network_address_boundary = result[:netmask] + "0" * zeros
        networ_broadcast_boundary = result[:(netmask)] + "1" * zeros

        net_address = ".".join(
            [str(int(network_address_boundary[i:i + 8], 2)) for i in range(0, 32, 8)])
        network_broadcast = ".".join(
            [str(int(networ_broadcast_boundary[i:i + 8], 2)) for i in range(0, 32, 8)])

        global_date = {
            "IP": sys.argv[1],
            "Netmask": sys.argv[2],
            "Netmask/24": netmask,
            "Hosts": hosts,
            "HostMin": ".".join(i for i in net_address.split(".")[:3]) + "." + str(int(net_address.split(".")[-1]) + 1),
            "HostMax": ".".join(i for i in network_broadcast.split(".")[:3]) + "." + str(int(network_broadcast.split(".")[-1]) - 1)
        }
        return dict(global_date)


if __name__ == '__main__':
    print(CalculateSubnet(GetInfo().result()).calc_broadcast())
