from netmiko import Netmiko
from netmiko import ConnectHandler

#password=getpass.getpass('please enter password: ')


def router_backup(router_ip,router_username,router_password):
    router_cisco = {
        "ip": router_ip,
        "username": router_username,
        "password": router_password,
        "device_type": "cisco_ios",
    }

    net_connect = ConnectHandler(**router_cisco)
    net_connect.find_prompt()
    z = net_connect.send_command_timing("terminal length 0")
    output2 = net_connect.send_command_timing("show run")
    file=open(router_ip,"w")
    file.write(output2)
    print (output2)
    net_connect.disconnect()

router_backup("172.20.5.254","username_router_entered","password_router_entered")

for ip in range(1,254):
    x="10.0.0"+str(ip)
    router_backup(x,"username_router_or_switch_entered","password_router_or_switch_entered")
