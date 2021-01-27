#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from datetime import datetime


password = getpass()

nxos1 = {
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": password,
        "device_type": "cisco_nxos",
        "session_log": "session_log1.txt",
}

nxos2 = {
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": password,
        "device_type": "cisco_nxos",
        "session_log": "session_log2.txt",
}


start_time = datetime.now()


for device in (nxos1, nxos2):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())

    output = net_connect.send_config_from_file("my_changes.txt")                

    pprint(output)
    net_connect.save_config()
    net_connect.disconnect()

end_time = datetime.now()

print("Total Execution Time: {}\n\n".format(end_time - start_time))
