#Loading python modules
from netmiko import ConnectHandler
from getpass import getpass

#Cisco SSH connection
cisco_netconnect = ConnectHandler(
    host = "cisco4.lasthop.io",
    username = input("Username:"),
    password = getpass(),
    device_type = "cisco_ios",
    session_log = "Cisco_SSH_Log.txt",
    )

output = cisco_netconnect.send_command_timing(
    "ping", strip_prompt=False, strip_command=False
)
output += cisco_netconnect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += cisco_netconnect.send_command_timing(
    "8.8.8.8", strip_prompt=False, strip_command=False
)
output += cisco_netconnect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += cisco_netconnect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += cisco_netconnect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += cisco_netconnect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += cisco_netconnect.send_command_timing("\n", strip_prompt=False, strip_command=False)
cisco_netconnect.disconnect()

print()
print(output)
print()
