#Huawei Switch
#Access and VLan Data validation after the extraction from the Huawei switches.
#Real_netmik Function will call the Huawei_access_validation function with the data that it has collected after logging in the switch from the interface.

#Second check definition---- Check whether or not the vlan id is passed.
def second_check(vlan_id_Data1,ID):
	vlan_id_Data1= list(map(int, vlan_id_Data1))
	vlan_id_Data1.sort()
	return ID in vlan_id_Data1
 
def huawei_access_validation(IP_address,Data_from_interface,Vlan_id):
	Data_from_interface= Data_from_interface.split()  
	#first check---- Check whether it is access or not.
	index=Data_from_interface.index("link-type")
	if "link-type" in Data_from_interface : 
		index=Data_from_interface.index("link-type")
		if Data_from_interface[index+1].lower()== "access" and Data_from_interface[index+3].lower()=="default":
			print()
			print("For the switch IP",IP_address)
			print("Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"is configured as an ACCESS Port")
			#Vlan Data extraction from huawei switches
			vlan_index= Data_from_interface.index("default")+2
			vlan_id_Data=[]
			for i in range(vlan_index,len(Data_from_interface)):
				vlan_id_Data.append(Data_from_interface[i])
			#Second check function call
			check=second_check(vlan_id_Data,Vlan_id)
			if check:
				print("And Vlan",Vlan_id,"IS passed through the Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper()," and checked successfully")
			else:
				print("But Vlan",Vlan_id,"IS NOT passed through the Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"kindly configure the port by passing the vlan", Vlan_id)
		else:
			if "trunk" in Data_from_interface:
				print()
				print("For the switch IP",IP_address)
				print("Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"is configured as a TRUNK port and should be changed to ACCESS")
			else:
				print()
				print("For the switch IP",IP_address)
				print("Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"IS NOT properly configured as an ACCESS port")
				print("Please MODIFY the configuration")
	else:
		print("For the switch IP",IP_address)
		print("The Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"IS NOT configured as an ACCESS port")
		print("Please MODIFY the configuration")		