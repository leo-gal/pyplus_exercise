#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device1 = {
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_nxos",
        "session_log": "session_log.txt",
        
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = 'show lldp neighbors detail'
print(datetime.now())
output = net_connect.send_command(command, delay_factor=2)              
print()
print(output)
print()
print(datetime.now())


print(datetime.now())
output = net_connect.send_command(command, delay_factor=8)              
print()
print(output)
print()
print(datetime.now())


