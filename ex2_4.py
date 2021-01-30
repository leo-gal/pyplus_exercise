#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from datetime import datetime

device1 = {
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_ios",
#        "session_log": session_log.txt,
}

cfg = [
    "ip name-server 1.1.1.1",
    "no ip name-server 1.0.0.1",
    "ip domain-lookup",
]

start_time = datetime.now()

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_config_set(cfg)                

pprint(output)

ping_output= net_connect.send_command("ping google.com")
if "!!" in ping_output:
    print("Ping Successful:")
    print("\n\nPing Output: {}\n\n".format(ping_output))
else:
    raise ValueError("\n\nPing Failed: {}\n\n".format(ping_output))
net_connect.disconnect()

end_time = datetime.now()

net_connect.disconnect()
print("Total Execution Time: {}\n\n".format(end_time - start_time))
