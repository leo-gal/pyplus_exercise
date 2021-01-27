#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

device1 = {
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_ios",
#        "session_log": session_log.txt,
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show ip arp", use_textfsm=True)                
pprint(output)

for arp_entry in output:
    print('#' *12) 
    print(arp_entry['mac'])
    print(arp_entry['address'])
    print('#' *12) 
    print()
    #break

net_connect.disconnect()
