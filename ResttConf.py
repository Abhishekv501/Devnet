import requests
import json
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

url = "https://192.168.146.140/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"


payload =  { "ietf-interfaces:interface": {
          "name": "GigabitEthernet2",
          "description": "Added with RESTCONF",
          "type": "iana-if-type:ethernetCsmacd",
          "enabled": True,
          "ietf-ip:ipv4": {
              "address": [
                  {
                      "ip": "200.1.1.1",
                      "netmask": "255.255.255.0"
                  }
              ]
          }
      }
  }
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',

}

auth = HTTPBasicAuth("admin", "cisco")


response = requests.put(url, headers=headers, auth=auth, data = json.dumps(payload), verify = False)



print(response.text.encode('utf8'))