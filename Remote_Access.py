import netmiko
from netmiko import ConnectHandler
import time
import Cisco.Cisco_Trunk_vlan_validation as Cisco_Trunk_vlan_validation
import Cisco.Cisco_Access_vlan_validation as Cisco_Access_vlan_validation
import Huawei.Huawei_Trunk_vlan_validation as Huawei_Trunk_vlan_validation
import Huawei.Huawei_Access_vlan_validation as Huawei_Access_vlan_validation


#show running configuration command is executed on the cisco device via cisco_send_command_function which takes the Port and Netmiko Connection as the arguments
def cisco_send_command_function(port, connection):
	show_command = "show runn inter "+ port
	result = connection.send_command(show_command)
	result = result.splitlines()
	result = result[(result.index("!")+1):(len(result))]
	for i in range(len(result)):
		result[i] = result[i].strip()
	result = ' '.join(result)
	return result

#display current configuration command is executed on the huawei device via huawei_send_command_function which takes the Port and Netmiko Connection as the arguments	
def huawei_send_command_function(port, connection):
	show_command = "display curr inter "+ port
	result = connection.send_command(show_command)
	return result
  
#SSH_connection remotely accesses the devices using netmiko library and gets the configuration and passes the output to the respective access or trunk validation functions  
def SSH_connection(device,address,name,password,secret,trunk_port_1,trunk_port_2,access_port,vlan):
	print("-"*100)
	print("Data in the SSH Connection ", device, " ", address, " ", name, " ", password, " ", secret, " ", "T-port1: ", trunk_port_1, " ", "T-port2: ", trunk_port_2, " ", "A-port3: ", access_port)
	try:
		net_connect = ConnectHandler(device_type = device, ip = address, username = name, password = password, secret = secret)
		print("Connected to ", address)
		if device == 'cisco_ios':
			#Go the Enable mode using the enable password obtained from "secret" as given by the user, in the cisco switch to get the running configuration
			net_connect.enable()
			output = cisco_send_command_function(trunk_port_1, net_connect)
			Cisco_Trunk_vlan_validation.cisco_trunk_validation(address, output, int(vlan))
			if len(trunk_port_2) != 0 and len(access_port) == 0:
				output = cisco_send_command_function(trunk_port_2, net_connect)
				Cisco_Trunk_vlan_validation.cisco_trunk_validation(address, output, int(vlan))
			elif len(trunk_port_2) == 0 and len(access_port) != 0:
				output = cisco_send_command_function(access_port, net_connect)
				Cisco_Access_vlan_validation.cisco_access_validation(address, output, int(vlan))

		elif device == 'huawei':
			output = huawei_send_command_function(trunk_port_1, net_connect)
			Huawei_Trunk_vlan_validation.huawei_trunk_validation(address, output, vlan)
			if len(trunk_port_2) != 0 and len(access_port) == 0:
				output = huawei_send_command_function(trunk_port_2, net_connect)
				Huawei_Trunk_vlan_validation.huawei_trunk_validation(address, output, int(vlan))
			elif len(trunk_port_2) == 0 and len(access_port) != 0:
				output = huawei_send_command_function(access_port, net_connect)
				Huawei_Access_vlan_validation.huawei_access_validation(address, output, int(vlan))

		net_connect.disconnect()
		time.sleep(1)
		print()
	except netmiko.ssh_exception.NetMikoTimeoutException:
		print("Connection Timeout to ", address)
	except netmiko.ssh_exception.NetMikoAuthenticationException:
		print("Authentication Failed to ", address)
		print("Please check the credentials and run the code again")
 
 
Device_vendor = ''
Ip_address = ''
User_name = ''
Pass_word = ''
#Enable password only for cisco devices
Secret = ''

#The User_input function assigns the data coming from the Switch_Data_Generator.py to the respective variables and passes it to the SSH_connection function which does the remote access.
def User_input(Switches_Data, vlan):
	for i in range(len(Switches_Data)):
		#netmiko requires cisco devices to be passed as cisco_ios.
		if Switches_Data[i]['Vendor'].lower() == 'cisco':
			Device_vendor = Switches_Data[i]['Vendor']+"_ios"
		elif Switches_Data[i]['Vendor'].lower() == 'huawei':
			Device_vendor = Switches_Data[i]['Vendor']
		Ip_address = Switches_Data[i]['IP']
		User_name = Switches_Data[i]['Username']
		Pass_word = Switches_Data[i]['Password']
		Secret = Switches_Data[i]['Enable_pass']
		Trunk_Interface_1 = Switches_Data[i]['TPort-1']
		if Switches_Data[i]['TPort-2'] != '':
			Trunk_Interface_2 = Switches_Data[i]['TPort-2']
			Access_Interface = ''
		elif Switches_Data[i]['APort'] !='':
			Access_Interface = Switches_Data[i]['APort']
			Trunk_Interface_2 = ''
		SSH_connection(Device_vendor, Ip_address, User_name, Pass_word, Secret, Trunk_Interface_1, Trunk_Interface_2, Access_Interface, vlan)


