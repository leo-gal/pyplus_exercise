#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_ios"
#        "session_log": session_log.txt
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = 'ping'
output = net_connect.send_command(command, expect_string=r'Protocol', strip_prompt=False, strip_command=False )                
output += net_connect.send_command('\n', expect_string=r'Target', strip_prompt=False, strip_command=False )                
output += net_connect.send_command('8.8.8.8', expect_string=r'Repeat', strip_prompt=False, strip_command=False)                
output += net_connect.send_command('\n', expect_string=r'Datagram', strip_prompt=False, strip_command=False)                
output += net_connect.send_command('\n', expect_string=r'Timeout', strip_prompt=False, strip_command=False)                
output += net_connect.send_command('\n', expect_string=r'Extended', strip_prompt=False, strip_command=False)                
output += net_connect.send_command('\n', expect_string=r'Sweep', strip_prompt=False, strip_command=False)                
output += net_connect.send_command_timing('\n')
print()
print(output)
print()

