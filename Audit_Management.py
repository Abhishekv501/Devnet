from netmiko import ConnectHandler
import multiprocessing.pool
import colorama                                                                                                 # for color printing


def mgt_audit(hostname):
    file_out = open('output2.txt', 'a+')
    try:
        device_name_dict = {
            'device_type': 'cisco_ios',
            'ip': hostname,
            'username': '******',
            'password': '******',
            'secret': '******',
            'global_delay_factor': 2,
        }
        print("connecting to {}".format(hostname), end='')
        net_connect = ConnectHandler(**device_name_dict)
        print(colorama.Fore.GREEN + 'Successful' + colorama.Fore.RESET)
        distro_cdp = net_connect.send_command("show cdp neighbors", use_textfsm=True)
        find_mgmt = net_connect.send_command("show interfaces description", use_textfsm=True)
        distro_lldp = net_connect.send_command("show lldp neighbors", use_textfsm=True)
        mgt_vlan = ''
        for i in find_mgmt:
            if 'gpbmgt-lan' in i['descrip'].lower():
                print(i['port'])
                mgt_vlan = i['port'].lstrip('Vl')
                print(mgt_vlan)
        for i in distro_cdp:
            if 'ldr' in i['neighbor'].lower():
                print(i['local_interface'])
                allowed_vlans=net_connect.send_command('show interface {} switchport | inc Trunking VLANs Enabled'.format(i['local_interface'])).split(': ')[-1].split(',')
                print(allowed_vlans)
                if mgt_vlan in allowed_vlans:
                    print('GPB management vlan {} is passing in LDR trunk interface {}\n'.format(mgt_vlan, i['local_interface']))
                    file_out.write(hostname)
                else:
                    print('GPB management vlan {} is not passing in LDR trunk interface {}\n'.format(mgt_vlan, i['local_interface']))
            elif 'edr' in i['neighbor'].lower():
                print(i['local_interface'])
                allowed_vlans=net_connect.send_command('show interface {} switchport | inc Trunking VLANs Enabled'.format(i['local_interface'])).split(': ')[-1].split(',')
                print(allowed_vlans)
                if mgt_vlan in allowed_vlans:
                    print('GPB management vlan {} is passing in EDR trunk interface {}\n'.format(mgt_vlan, i['local_interface']))
                    file_out.write(hostname)
                else:
                    print('GPB management vlan {} is not passing in EDR trunk interface {}\n'.format(mgt_vlan, i['local_interface']))
        for i in distro_lldp:
            if 'ldr' in i['neighbor'].lower():
                print(i['local_interface'])
                allowed_vlans=net_connect.send_command('show interface {} switchport | inc Trunking VLANs Enabled'.format(i['local_interface'])).split(': ')[-1].split(',')
                print(allowed_vlans)
                if mgt_vlan in allowed_vlans:
                    print('GPB management vlan {} is passing in LDR trunk interface {}\n'.format(mgt_vlan, i['local_interface']))
                    file_out.write(hostname)
                else:
                    print('GPB management vlan {} is not passing in LDR trunk interface {}\n'.format(mgt_vlan, i['local_interface']))
            elif 'edr' in i['neighbor'].lower():
                print(i['local_interface'])
                allowed_vlans=net_connect.send_command('show interface {} switchport | inc Trunking VLANs Enabled'.format(i['local_interface'])).split(': ')[-1].split(',')
                print(allowed_vlans)
                if mgt_vlan in allowed_vlans:
                    print('GPB management vlan {} is passing in EDR trunk interface {}\n'.format(mgt_vlan, i['local_interface']))
                    file_out.write(hostname)
                else:
                    print('GPB management vlan {} is not passing in EDR trunk interface {}\n'.format(mgt_vlan, i['local_interface']))
    except Exception as e:
        print("NOT CONNECTED", e)

    file_out.close()

with open("devices2.txt",'r') as fe:
    for hostname in fe.readlines():
        mgt_audit(hostname)
