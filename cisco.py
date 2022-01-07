from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
secret = getpass("enter secret: ")

cisco1 = {
    "device_type": "cisco_ios",
    "host": "192.168.137.111",
    "username": "admin",
    "password": password,
    "secret" : secret,
}

commands = ["logging buffered 100000"]

for devices in (cisco1):
    with ConnectHandler(**devices) as net_connect:
    # Call 'enable()' method to elevate privileges
    net_connect.enable()
    print(net_connect.find_prompt())

    output = net_connect.send_config_set(commands)
    output += net_connect.save_config()

    # net_connect.disconnect()




print()
print(output)
print()
net_connect.disconnect()
