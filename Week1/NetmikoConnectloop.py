#loading python modules
from netmiko import ConnectHandler
from getpass import getpass

#Variables
cisco_devices = [ "example1", "example2"] #replace with your cisco devices
ssh_username = input("Username:")
ssh_pass = getpass()

#Cisco SSH Connection
for device_host in cisco_devices:
    cisco_netconnect = ConnectHandler(
        host = device_host,
        username = ssh_username,
        password = ssh_pass,
        device_type = "cisco_ios",
        session_log ="Cisco_SSH_Log.txt",
    )
    print (cisco_netconnect.find_prompt())
