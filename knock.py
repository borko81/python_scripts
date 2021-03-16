import socket
import time

IP="Here put the ip"
MY_PORTS = [10, 11, 12, 13]


def generate_url_with_port(MY_PORTS):
    for p in MY_PORTS:
        yield p


def generate_socket(IP, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((IP, port))
    except socket.error:
        pass
    

print('knock... knock...')
for res in generate_url_with_port(MY_PORTS):
    generate_socket(IP, res)
    time.sleep(1)
