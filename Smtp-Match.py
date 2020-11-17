from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler

############################################

def smtp_match(device):
    try:
        device_name_dict = {
            'device_type': 'cisco_ios',
            'host': device ,
            'username':'*******',
            'password': '*******',
            'secret': '*******',
            'global_delay_factor': 2,
            'session_log': 'my_output_file.txt'
        }
        print("connecting to {}".format(device), end='')
        net_connect = ConnectHandler(**device_name_dict)
        net_connect.enable()
        smtp_match_list1 = []
        smtp_match_list2 = []
        sh_smtp1 = net_connect.send_command('sho ip access-lists 186 | inc permit tcp any 10.253.24.0 0.0.0.127 eq smtp')
        sh_smtp2 = net_connect.send_command('sho ip access-lists 186 | inc permit tcp any 10.7.209.0 0.0.0.63 eq smtp')
        if 'matches' in sh_smtp1:
            smtp_match_list1.append(device)
        else:
            print(device, ' : has no match for SMTP first line')
            with open("smtp_no_match.txt", 'a') as fe:
                fe.write(device)
        for i in smtp_match_list1:
            sh_match_list1 = sh_smtp1.split('(')[-1].split(' ')[0]
            sh_match_int1 = int(sh_match_list1)
            if sh_match_int1 <= 100:
                print(device, ' : has less then 100 match for smtp 1st line')
                with open("smtp_less_match.txt", 'a') as fe:
                    fe.write(device)
            else:
                print(device, ' : has more then 100 match for smtp 1st line')
                with open("smtp_more_match.txt", 'a') as fe:
                    fe.write(device)
        if 'matches' in sh_smtp2:
            smtp_match_list2.append(device)
        else:
            print(device, ' : has no match for SMTP second line')
            with open("smtp_no_match.txt", 'a') as fe:
                fe.write(device)
        for i in smtp_match_list2:
            sh_match_list2 = sh_smtp2.split('(')[-1].split(' ')[0]
            sh_match_int2 = int(sh_match_list2)
            if sh_match_int2 <= 100:
                print(device, ' : has less then 100 match for smtp second line')
                with open("smtp_less_match.txt", 'a') as fe:
                    fe.write(device)
            else:
                print(device, ' : has more then 100 match for smtp second line')
                with open("smtp_more_match.txt", 'a') as fe:
                    fe.write(device)



    except Exception as e:
        print("NOT CONNECTED", e)

with open("smtp_devices.txt",'r') as fe:
    for device in fe.readlines():
        smtp_match(device)
