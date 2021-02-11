#!/usr/bin/env python
import re
from pprint import pprint
import yaml


cisco3 = {"device_name": "cisco3", "host": "cisco3.lasthop.io"}

cisco4 = {"device_name": "cisco4", "host": "cisco4.lasthop.io"}

arista1 = {"device_name": "arista1", "host": "arista1.lasthop.io"}

arista2 = {"device_name": "arista2", "host": "arista2.lasthop.io"}


my_devices = [cisco3, cisco4, arista1, arista2]

for device in my_devices:
   device['username'] = "janko"
   device['password'] = "hrasko"

print(my_devices)

with open("ex3_2_output.yml", "w") as f:
   yaml.dump(my_devices, f, default_flow_style=False)
