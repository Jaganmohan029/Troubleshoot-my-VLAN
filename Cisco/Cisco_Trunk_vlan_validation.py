#Cisco Switch
#Trunk and Vlan Data validation after the extraction from the Cisco switches.
#Main Login Function will call the cisco_trunk_validation function with the data that it has collected after logging in the switch from the interface.

#Second check definition---- Check whether or not the vlan id is passed.
def second_check(vlan_id_Data1,ID):
	temp_arr1=[]
	final_series = []
	if len(vlan_id_Data1) == 0:
		final_series = list(range(1,4096))
	else:
		for j in range(len(vlan_id_Data1)):
			new_series=vlan_id_Data1[j].split(',')
			for k in range(0,len(new_series)):
				temp=[]
				temp_arr2=[]
				if new_series[k].find('-')!=-1:
					temp=new_series[k].split('-')
					lb=int(temp[0])
					ub=int(temp[1])
					for l in range(lb,ub+1):
						temp_arr2.append(str(lb))
						lb=lb+1
					temp_arr1=temp_arr1+temp_arr2
				else:
					temp_arr1.append(new_series[k])
					final_series=temp_arr1
					final_series= list(map(int, final_series))
			final_series.sort()
	return ID in final_series

def cisco_trunk_validation(IP_address,Data_from_interface,Vlan_id):
	Data_from_interface=Data_from_interface.split()
	#This gives the indices in the array which has the allowed as value in them
	indices = [i for i, x in enumerate(Data_from_interface) if x == "allowed"]
	vlan_id_Data=[]
	for i in range(len(indices)):
		if Data_from_interface[indices[i]+2]=='add':
		#switchport commands with add in it
			vlan_id_Data.append(Data_from_interface[indices[i]+3])
		else:
		#switchport commands without add in it
			vlan_id_Data.append(Data_from_interface[indices[i]+2])

	#First Check ---- to see if the interface is configured as trunk or Not
	if "trunk" in Data_from_interface and not "access" in Data_from_interface and Data_from_interface[Data_from_interface.index("mode")+1].lower()== "trunk":
	#if the trunk is passed then it will call the second_check function and get the result
		print()
		print("For the switch IP",IP_address)
		print("Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"IS configured as a TRUNK port")
		check=second_check(vlan_id_Data,Vlan_id)
		if check:
			print("And Vlan",Vlan_id,"IS passed through the Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper())
		else:
			print("But Vlan",Vlan_id,"IS NOT passed through the Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"kindly configure the port by passing the vlan",Vlan_id)
	else:
	#if it is not configured as trunk (access or both trunk and access)
		print()
		print("For the switch IP",IP_address)
		print("Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"IS NOT properly configured as a TRUNK port")
		print("Please MODIFY the configuration")
