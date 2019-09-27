#Loading python modules
from netmiko import ConnectHandler
from getpass import getpass

#Cisco SSH connection
cisco_netconnect = ConnectHandler(
    host = "example.host",
    username = input("Username:"),
    password = getpass(),
    device_type = "cisco_ios",
    session_log = "Cisco_SSH_Log.txt",
    )

print (cisco_netconnect.find_prompt())
cisco_netconnect.disconnect()
