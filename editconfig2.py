from ncclient import manager 
import xml.dom.minidom
import xmltodict

device = {
    "host": "192.168.146.140", "netconf_port": "830", "username": "admin", "password": "cisco"
}


#create a XML config template for IETF interafce data model
netconf_config = '''
 <config> 
     <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">
         <interface> 
             <name>{name}</name>
             <description>{desc}</description>
             <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type> 
             <enabled>true</enabled>
             <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                 <address>
                     <ip>{ip_address}</ip>
                     <netmask>{mask}</netmask>
                 </address>
             </ipv4>
             <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
         </interface>
     </interfaces>
 </config>'''

#under type-> interface type will be softwareLoopback for Loopback interfaces

#Ask for the interface details dynamically to add

new_interface= {}
new_interface["name"] = "Loopback" + raw_input("enter the gigabit interface number: ")
new_interface["desc"] = raw_input("enter the desc: ")
new_interface["ip_address"] = raw_input("enter Ip: ")
new_interface["mask"] = raw_input("enter mask: ")

#Create a netconf data payload for this interface 

netconf_data = netconf_config.format(
 name = new_interface["name"],
 desc = new_interface["desc"],
 ip_address = new_interface["ip_address"],
 mask = new_interface["mask"]
)

#Create a netconf connection with teh device to be configured
with manager.connect(
    host = device["host"], 
    port = device["netconf_port"],
    username = device["username"],
    password = device["password"],
    hostkey_verify = False  
    ) as m:
    netconf_reply = m.edit_config(netconf_config, target = "running")
    print netconf_reply 
    