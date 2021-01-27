#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

device1 = {
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_ios",
#        "session_log": session_log.txt,
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show ver", use_textfsm=True)                
pprint(output)
output = net_connect.send_command("show lldp neighbor detail", use_textfsm=True)                
pprint(output)
pprint("Our neighbor " + output[0]["neighbor"] + ' connects on port ' + output[0]["neighbor_port_id"])
#  'neighbor': 'twb-sf-hpsw1',
#  'neighbor_interface': '17',
#  'neighbor_port_id': '17',
net_connect.disconnect()
