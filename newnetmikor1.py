from netmiko import ConnectHandler
import devices


R1 = {
    "device_type": "cisco_ios", "ip": "192.168.146.139", "username": "admin", "password": "cisco"
}

R2 = {
    "device_type": "cisco_ios", "ip": "192.168.146.139", "username": "admin", "password": "cisco"
}

alldevices = [R1,R2]


for R in alldevices:
    
    net_connect = ConnectHandler(**R)
    net_connect.enable()
    print "connection established with" + R["ip"]


#send_command -> enable commands
#send_config_set -> conf t commands

    output = net_connect.send_command("sh run int vlan 10")
    print output

    output1 = net_connect.send_config_set("vlan 40")
    print output1