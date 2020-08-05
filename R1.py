import telnetlib
import getpass


Host = "192.168.146.139"
Username = raw_input("Enter your user name:")
password = getpass.getpass("Enter your password:")
tn = telnetlib.Telnet(Host)


tn.read_until("Username: ")
tn.write(Username + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("int loopback 1\n")
tn.write("ip address 10.1.1.1 255.255.255.0\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()

print "Task Completed"
