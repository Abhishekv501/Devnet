from ncclient import manager 
import xml.dom.minidom
import xmltodict

IOS_XE_1 = {
    "host": "192.168.146.140", "netconf_port": "830", "username": "admin", "password": "cisco"
}

# Create an XML configuration template for ietf-interfaces

netconf_interface_template = """
 <config>
     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
         <interface>
             <name>{name}</name>
             <description>{desc}</description>
             <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                 ianaift:softwareLoopback
             </type>
             <enabled>{status}</enabled>
             <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                 <address>
                     <ip>{ip_address}</ip>
                     <netmask>{mask}</netmask>
                 </address>
             </ipv4>
         </interface>
     </interfaces>
 </config>"""

# Ask for the Interface Details to Add

new_loopback = {}
new_loopback["name"] = "Loopback" + raw_input("What loopback number to add? ")
new_loopback["desc"] = raw_input("What description to use? ")
#new_loopback["type"] = IETF_INTERFACE_TYPES["loopback"]
new_loopback["status"] = "true"
new_loopback["ip_address"] = raw_input("What IP address? ")
new_loopback["mask"] = raw_input("What network mask? ")

# Create the NETCONF data payload for this interface

netconf_data = netconf_interface_template.format(
         name = new_loopback["name"],
         desc = new_loopback["desc"],
         #type = new_loopback["type"],
         status = new_loopback["status"],
         ip_address = new_loopback["ip_address"],
         mask = new_loopback["mask"]
     )

with manager.connect(
  host=IOS_XE_1["host"],
  port=IOS_XE_1["netconf_port"],
  username=IOS_XE_1["username"],
  password=IOS_XE_1["password"],
  hostkey_verify=False
  ) as m:
    netconf_reply = m.edit_config(netconf_data, target = 'running')
    print netconf_reply
