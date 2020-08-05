import telnetlib
import getpass
import sys


Host = "localhost"
username = raw_input("Enter username: ")
password = getpass.getpass("Enter password: ")
nl = "\n"
a = open("C:\\Users\\koenig\\Desktop\\Abhishek\\IPs.txt")

for ip in a:
    print ip
    ip = ip.strip()
    Host = ip
    print "Configuring Switch " + Host
    tn = telnetlib.Telnet(Host)

    tn.read_until("Username: " )
    tn.write(username + nl)
    if password:
        tn.read_until("Password: ")
        tn.write(password + nl)


    tn.write("enable\n")
    tn.write("cisco\n")
    tn.write("conf t \n")

    for i in range(2,11):
        tn.write("vlan " + str(i) + nl)
        tn.write("name Python_vlan_" + str(i) + nl)

    tn.write("end \n")
    tn.write("exit\n")

    print tn.read_all()