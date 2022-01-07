def mylist(**kwargs):
    for key,value in kwargs.items():
        print(key,value)


router1 = {"type": "cisco",
           "ipaddress": "10.10.10.11",
           "username": "admin",
           "password": "cisco"}

router2 = {"type": "cisco",
           "ipaddress": "10.10.10.12",
           "username": "admin",
           "password": "cisco"}

routers = (router1, router2)

# for devices in (router1,router2):
#    mylist(**devices)

# mylist(**router1)

for devices in routers:
    mylist(**devices)