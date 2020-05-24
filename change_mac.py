#!/usr/bin/python3

###CHANGE MAC ADDRESS

#IMPORT MODULES
import subprocess
import optparse
import socket
import random


def change_mac_address_with_user_input():
    """Use function to change mac address option come from user input"""
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest="NET_NAME", help="Interface to change")
    parser.add_option('-m', '--mac', dest="NEW_MAC", help="New mac address")
    (options, argments ) = parser.parse_args()
    NET_NAME = options.NET_NAME
    NEW_MAC = options.NEW_MAC
    print(NET_NAME, NEW_MAC)
    subprocess.call("ifconfig " + NET_NAME + " down", shell=True)
    subprocess.call("ifconfig " + NET_NAME + " hw ether " + NEW_MAC, shell=True)
    subprocess.call("ifconfig " + NET_NAME + " up", shell=True)


#USE AUTO GENERATE FUNCTION
def get_name_of_network_card():
    """Get name of network interface exclude lo"""
    return [i[1] for i in socket.if_nameindex() if i[1] != 'lo'][0].strip("'")


def generate_mac():
    """Generate mac address"""
    a = random.randrange(1,10)
    b = random.randrange(1,10)
    return str(a) + str(b) + ":"


def auto_change_generate_mac():
    """Auto change mac address without user input"""
    MAC = ""

    for _ in range(6):
        MAC += generate_mac()

    NEW_MAC = MAC.rstrip(":")
    NET_NAME = get_name_of_network_card()
    print("Network name :", NET_NAME, " new mac address :", NEW_MAC)

    subprocess.call("ifconfig " + NET_NAME + " down", shell=True)
    subprocess.call("ifconfig " + NET_NAME +" hw ether " + NEW_MAC, shell=True)
    subprocess.call("ifconfig " + NET_NAME + " up", shell=True)

if __name__ == '__main__':
    #TO USE AUTO GENERATE SECTION UNCOMENT NEXT LINE
    print("Begin...")
    #auto_change_generate_mac()
    #TO USE USER INPUT ARGUMENTS OPTION'S COMMENT BEYOUND LINE AND UNCOMENT BELOW LINE!
    change_mac_address_with_user_input()

