from ncclient import manager

device = {
    "host": "192.168.146.140", "netconf_port": "830", "username": "admin", "password": "cisco"
}

netconf_config = '''
 <config> 
    <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation = "delete"> 
            <name>Loopback10</name>
        </interface>
    </interfaces>
 </config>'''

with manager.connect(
    host = device["host"], 
    port = device["netconf_port"],
    username = device["username"],
    password = device["password"],
    hostkey_verify = False  
    ) as m:
    netconf_reply = m.edit_config(netconf_config, target = "running")
    print netconf_reply 