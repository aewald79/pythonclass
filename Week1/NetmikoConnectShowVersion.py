#loading python modules
from netmiko import ConnectHandler
from getpass import getpass

#Variables
cisco_devices = [ "Example1", "Example2"] #Replace with your cisco device hostnames
ssh_username = input("Username:")
ssh_pass = getpass()

#Cisco SSH Connection
for device_host in cisco_devices:
    cisco_netconnect = ConnectHandler(
        host = device_host,
        username = ssh_username,
        password = ssh_pass,
        device_type = "cisco_ios",
        session_log = "Cisco_SSH_Log.txt",
    )
    print (cisco_netconnect.find_prompt())
    with open(device_host + "_show_version.txt","a") as f:
        print (cisco_netconnect.send_command("show version"),file=f)
