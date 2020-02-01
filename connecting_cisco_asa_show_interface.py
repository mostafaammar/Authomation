#!/usr/bin/env python
from netmiko import Netmiko
from netmiko import ConnectHandler
import getpass
import textfsm
import csv
#
# constants= open("con.txt",'r')
# x=constants.readlines()
# print (type(x))
# username=str(x[0]).lstrip()
# host=str(x[1]).lstrip()
# print (username,host)

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
print(net_connect.find_prompt())
output1 = net_connect.send_command_timing("enable"+"\n")
pass123 =  getpass.getpass("enter enable password: ")

if "Password:" in output1 :
    output1 = net_connect.send_command_timing(pass123, strip_prompt=False, strip_command=False)
# to generate the output without --more in cisco asa
z= net_connect.send_command_timing("terminal pager 0")
output2=net_connect.send_command_timing("show interface" , use_textfsm=True)

with open('show_interface_cisco_asa.csv', 'w') as csvfile:
     for items in output2:
        print (items['interface'],items["packets_input"],items["ip_address"])
        writer = csv.writer(csvfile)
        fieldnames=['interface',"packets_input","ip_address"]
        x = [items['interface'],items["packets_input"], items["ip_address"]]
        writer.writerow(x)
print ("type of output2 is ", type(output2))
print ("type of items is ", type(items))



print("ELHAMDOLELAH")
