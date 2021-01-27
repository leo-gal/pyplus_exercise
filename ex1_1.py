#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_nxos"
#       "session_log": session_log.txt
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
