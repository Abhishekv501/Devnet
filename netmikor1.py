from netmiko import ConnectHandler
import devices


'''R1 = {
    "device_type": "cisco_ios", "ip": "192.168.146.139", "username": "admin", "password": "cisco"
}'''

alldevices = [devices.sw1, devices.sw2, devices.sw3]

for device in alldevices:
    
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    print "connection established with" + device["ip"]


#send_command -> enable commands
#send_config_set -> conf t commands

    output = net_connect.send_command("sh run int vlan 10")
    print output

    output1 = net_connect.send_config_set("vlan 40")
    print output1
    
