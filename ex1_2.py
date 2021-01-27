#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

devices = [
   {
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_nxos"
      # "session_log": session_log.txt
   },
   {
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_nxos"
       #"session_log": session_log.txt
    }
]



#print(devices)

for device in devices:
   net_connect = ConnectHandler(**device)
   print(net_connect.find_prompt())
   if device['host'] == 'nxos1.lasthop.io':
       show_version = net_connect.send_command("show version")
       with open("ex1_3_show_version.txt",mode="w") as f:
            f.write(f"{show_version}\n")
   net_connect.disconnect()
