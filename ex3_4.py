#!/usr/bin/env python
import re
from pprint import pprint
import json



with open("ex3_4_input.json", "r") as f:
   json_data = json.load(f)



arp_dict = {}

for  arp_entry in json_data["ipV4Neighbors"]:
   ipaddr = arp_entry['address']
   macaddr = arp_entry['hwAddress']
   arp_dict[ipaddr] = macaddr

print(arp_dict)


#   for ipv4_or_ipv6,addr_info in ipaddr_dict.items():  
#      for addr,pfx_length  in addr_info.items():
#         pfxl = pfx_length['prefix_length']
#         if ipv4_or_ipv6 == 'ipv4':
#            ipv4_list.append(f"{addr}/{pfxl}")  
#         if ipv4_or_ipv6 == 'ipv6':
#            ipv6_list.append(f"{addr}/{pfxl}")
#
#print(ipv4_list)
#print(ipv6_list)


"""
{
    "dynamicEntries": 2,
    "ipV4Neighbors": [
        {
            "hwAddress": "dc38.e111.97cf",
            "address": "172.17.17.1",
            "interface": "Ethernet45",
            "age": 0
        },
        {
            "hwAddress": "90e2.ba5c.25fd",
            "address": "172.17.16.1",
            "interface": "Ethernet36",
            "age": 0
        }
    ],
    "notLearnedEntries": 0,
    "totalEntries": 2,
    "staticEntries": 0
}
"""
