"""
    use subprocess to invoke nets command,
    found wifi name's and return his password
"""

import subprocess
import re
import threading

command = 'netsh wlan show profile'.split()
match_name = re.compile(r"All User Profile\s+:\s(.*)\r")


def generate_list_with_networks():
    """
    Use to return list with nams
    :return: text
    """
    return subprocess.run(command, capture_output=True).stdout.decode(errors='ignore')


def found_network_name(list_with_profiles):
    """
    Use to return clean name of list with result, returner by netsh command
    :param list_with_profiles: List
    :return: matcher names
    """
    return match_name.findall(list_with_profiles)


def return_result(name):
    """
    Use to return UUSID name and password
    :param name: str
    :return:
    """
    wifi = {}
    profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"],
                                       capture_output=True).stdout.decode(errors='ignore')
    password = re.search("Key Content\s+: (.*)\r", profile_info_pass)
    if password is not None:
        wifi[name] = password[1]
        print(wifi)
    else:
        return


def generate_result(names):
    """
    main function
    :param names: str
    :return:
    """
    if len(names) != 0:
        for name in names_list:
            t = threading.Thread(target=return_result, args=(name,))
            t.start()
            # t.join()


if __name__ == '__main__':
    list_with_network = generate_list_with_networks()
    names_list = found_network_name(list_with_network)
    generate_result(names_list)
