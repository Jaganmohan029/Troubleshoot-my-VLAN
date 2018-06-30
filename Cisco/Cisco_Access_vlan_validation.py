#Cisco Switch
#Access and VLan Data validation after the extraction from the Cisco switches.
#Main Login Function will call the cisco_access_validation function with the data that it has collected after logging in the switch from the interface.

#Second check definition---- Check whether or not the vlan id is passed.
def second_check(vlan_id_Data1,ID):
	vlan_id_Data1= list(map(int, vlan_id_Data1))
	vlan_id_Data1.sort()
	return ID in vlan_id_Data1
 

def cisco_access_validation(IP_address,Data_from_interface,Vlan_id):
	Data_from_interface=Data_from_interface.split()
	#This gives the indices in the array which has the access as value in them
	indices = [i for i, x in enumerate(Data_from_interface) if x == "access"]
	vlan_id_Data=[]
	for i in range(len(indices)):
		if Data_from_interface[indices[i]+1]=='vlan':
		#switchport commands with vlan in it
			vlan_id_Data.append(Data_from_interface[indices[i]+2])

	#First Check ---- to see if the interface is configured as Access or Not
	if "access" in Data_from_interface and not "trunk" in Data_from_interface: #and Data_from_interface[Data_from_interface.index("mode")+1].lower()== "access":
	#if the Access is there in the configuration then it will call the second_check function and get the result
		print()
		print("For the switch IP",IP_address)
		print("Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"is configured as an ACCESS Port")
		check=second_check(vlan_id_Data,Vlan_id)
		if check:
			print("And Vlan",Vlan_id,"IS passed through the Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper())
		else:
			print("But Vlan",Vlan_id,"IS NOT passed through the Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"kindly configure the port by passing the vlan", Vlan_id)
	else:
	#if it is not configured as Access (access or both trunk and access)
		print()
		print("For the switch IP",IP_address)
		print("Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"IS NOT properly configured as an ACCESS port")
		print("Please MODIFY the configuration")
