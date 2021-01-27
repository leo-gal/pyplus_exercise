#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from datetime import datetime
import time

password = getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}


start_time = datetime.now()

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
net_connect.config_mode()
print(net_connect.find_prompt())
net_connect.exit_config_mode()
print(net_connect.find_prompt())
net_connect.write_channel("disable\n")
print(net_connect.find_prompt())
time.sleep(2)
output = net_connect.read_channel()
print(output)
net_connect.enable()
print(net_connect.find_prompt())


net_connect.disconnect()

end_time = datetime.now()

print("Total Execution Time: {}\n\n".format(end_time - start_time))
