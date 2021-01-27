#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_ios",
#        "session_log": session_log.txt,
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show ver")                
print(output)

net_connect.disconnect()
show_ver = output
#line = show_ver[1]
