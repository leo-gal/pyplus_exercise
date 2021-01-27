#!/usr/bin/env python
from pprint import pprint
from datetime import datetime
import yaml
from netmiko import ConnectHandler
'''
Doc
'''

with open(".netmiko.yml") as f:
    yaml_out = yaml.load(f)


cisco3 = yaml_out["cisco3"]
net_connect = ConnectHandler(**cisco3)


print()
print(net_connect.find_prompt())
print()
