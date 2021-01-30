#!/usr/bin/env python
import re
from pprint import pprint


arp_data = """Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

arp_list = arp_data.splitlines()
#pprint(arp_list)

new_list = []
for arp_entry in arp_list:
   if re.search("^Protocol", arp_entry):
      continue
   _, ip, _, mac, _, intf =  arp_entry.split()
   dict = {'ip':ip, 'mac':mac, 'intf':intf}
   new_list.append(dict)
print(new_list)
