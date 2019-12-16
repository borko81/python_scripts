import threading
import subprocess
import sys

test_list = ['192.168.1.1', '192.168.1.22']


def pingcheck(ip):
    try:
        # This always return True ?
        otg = subprocess.check_output(f'ping -n 2 {ip}', shell=True)
    except Exception as e:
        print(e)
    else:
        print(f"[+] {ip}")


def create_threads(list, function, data):

    all_threads = []

    for ip in list:
        t = threading.Thread(target=function, args=(ip,))
        t.start()


if __name__ == '__main__':
    create_threads(test_list, pingcheck, 'ip addr show')
