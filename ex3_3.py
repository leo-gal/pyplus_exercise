#!/usr/bin/env python
import re
from pprint import pprint
import json



with open("ex3_3_input.json", "r") as f:
   json_data = json.load(f)




ipv4_list = []
ipv6_list = []

for intf,ipaddr_dict in json_data.items():
   for ipv4_or_ipv6,addr_info in ipaddr_dict.items():  
      for addr,pfx_length  in addr_info.items():
         pfxl = pfx_length['prefix_length']
         if ipv4_or_ipv6 == 'ipv4':
            ipv4_list.append(f"{addr}/{pfxl}")  
         if ipv4_or_ipv6 == 'ipv6':
            ipv6_list.append(f"{addr}/{pfxl}")

print(ipv4_list)
print(ipv6_list)
