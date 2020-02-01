#!/usr/bin/env python
from netmiko import Netmiko
from netmiko import ConnectHandler
import getpass
import textfsm
import csv


username=getpass.getpass('please enter username: ')
host=getpass.getpass('please enter host ip address: ')
password=getpass.getpass('please enter password: ')

cisco1 = {
    "host": host,
    "username":username,
    "password":password,
    "device_type": "cisco_asa",
}
file = open( "show interface.txt" ,"w")
file.write("besmellah \n")
net_connect = ConnectHandler(**cisco1)
net_connect.find_prompt()
#Enter enable password
output1 = net_connect.send_command_timing("enable"+"\n")
pass123 =  getpass.getpass("enter enable password: ")

if "Password:" in output1 :
    output1 = net_connect.send_command_timing(pass123, strip_prompt=False, strip_command=False)
# to generate the output without --more in cisco asa
z= net_connect.send_command_timing("terminal pager 0")
#send the show interface command to asa and get the command output parsed used textfsm library
#the output is a list of dictionaries
#each dictionary represents an interface output parsed 
output2=net_connect.send_command_timing("show interface" , use_textfsm=True)

#transform output to Comma separated file to open with excel
with open('show_interface_cisco_asa.csv', 'w') as csvfile:
     for items in output2:
        print (items['interface'],items["packets_input"],items["ip_address"])
        writer = csv.writer(csvfile)
        fieldnames=['interface',"packets_input","ip_address"]
        x = [items['interface'],items["packets_input"], items["ip_address"]]
        writer.writerow(x)



print("ELHAMDOLELAH")
