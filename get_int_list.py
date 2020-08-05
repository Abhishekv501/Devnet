from ncclient import manager 
import xml.dom.minidom
import xmltodict

device = {
    "host": "192.168.146.140", "netconf_port": "830", "username": "admin", "password": "cisco"
}

netconf_filter = '''
 <filter> 
    <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface> </interface>
    </interfaces>
 </filter>'''

with manager.connect(
    host = device["host"], 
    port = device["netconf_port"],
    username = device["username"],
    password = device["password"],
    hostkey_verify = False  
    ) as m:

    netconf_reply = m.get_config(source = "running", filter = netconf_filter)
    print netconf_reply

print xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"] ["data"]

interfaces = netconf_data ["interfaces"] ["interface"]
print interfaces

for x in interfaces:
    print "interface {}'s enabled status is {}" .format(
        x["name"], 
        x["enabled"]
    )
#dataModel
#get_config ->config
#edit_config -> modify config
#get ->stats
