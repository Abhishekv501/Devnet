from ncclient import manager 
import xml.dom.minidom
import xmltodict

device = {
    "host": "192.168.146.140", "netconf_port": "830", "username": "admin", "password": "cisco"
}



netconf_config = '''
 <config> 
    <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface> 
            <name>GigabitEthernet3</name>
            <description>This is configured by Abhishek</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type> 
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>20.1.1.1</ip>
                    <netmask>255.255.255.0</netmask>
                </address>
            </ipv4>
            <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
        </interface>
    </interfaces>
 </config>'''

#under type-> interface type will be softwareLoopback for Loopback interfaces

with manager.connect(
    host = device["host"], 
    port = device["netconf_port"],
    username = device["username"],
    password = device["password"],
    hostkey_verify = False  
    ) as m:
    netconf_reply = m.edit_config(netconf_config, target = "running")
    print netconf_reply 
    