#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_ios"
#        "session_log": session_log.txt
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = 'delete flash:/cisco3-cfg-May--6-11-15-42.192-60'
output = net_connect.send_command(command, expect_string=r'cisco3-cfg-May', strip_prompt=False, strip_command=False )                
output += net_connect.send_command('\n', expect_string=r'confirm', strip_prompt=False, strip_command=False )                
output += net_connect.send_command('y', expect_string=r'#', strip_prompt=False, strip_command=False)                
print(output)
