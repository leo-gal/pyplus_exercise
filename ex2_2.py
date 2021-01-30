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
        "global_delay_factor": 2,
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = 'show lldp neighbors detail'
start_time = datetime.now()
output = net_connect.send_command(command)              
print()
print(output)
print()
end_time = datetime.now()
print(end_time - start_time)

start_time = datetime.now()
output = net_connect.send_command(command, delay_factor=16)              
print()
print(output)
print()
end_time = datetime.now()
print(end_time - start_time)


