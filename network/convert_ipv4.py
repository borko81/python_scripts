import socket
from binascii import hexlify


def convert_address():
    addr = '192.168.168.{}'
    for ip in range(1, 11):
        target_ip = addr.format(ip)
        # inet_aton, convert int dot addr to binascii
        packed_ip = socket.inet_aton(target_ip)
        # inet_ntoa convert binacyy to dot net address
        unpacked_addr = socket.inet_ntoa(packed_ip)
        # hexlify from binacii module convert bin to 2-digit hex representation
        print(f"{hexlify(packed_ip)}: {unpacked_addr}")


def get_hostname():
    # Return hostname
    host = socket.gethostname()
    # gethostbyname, return ip for hostname
    ipaddr = socket.gethostbyname(host)
    print(host, ipaddr)


def set_timeout():
    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # defaout timeout is zeto
    print("Default time is :", s.gettimeout())
    # change default timeout with socket.settimeout(100)
    s.settimeout(100)
    print("Now time is :", s.gettimeout())


set_timeout()
