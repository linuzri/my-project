#!/usr/bin/env python3
# https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md
from netmiko import ConnectHandler
import time

cisco1 = {
    'device_type': 'cisco_ios',
    'host': 'SW1',
    'username': 'admin',
    'password': 'cisco',
}
cisco2 = {
    'device_type': 'cisco_ios',
    'host': 'SW2',
    'username': 'admin',
    'password': 'cisco',
}

for devices in (cisco1,cisco2):
    cfg_file = devices['host'] + '.txt'
    net_connect = ConnectHandler(**devices)
    print("connecting to "+devices['host']+"...")
    time.sleep(1)
    net_connect.send_config_from_file(cfg_file)
    print("pushing config for "+devices['host']+"...")
    time.sleep(1)
    net_connect.save_config()
    print("saving config for "+devices['host']+"...")
    time.sleep(1)
    net_connect.disconnect()
    print("disconnecting from "+devices['host']+"...")
    time.sleep(1)
    print("done!")
