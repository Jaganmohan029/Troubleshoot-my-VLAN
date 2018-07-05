#Huawei Switch
#Trunk and Vlan Data validation after the extraction from the huawei switches.
#Real_Netmik Function will call the huawei_trunk_validation function with the data that it has collected after logging in the switch from the interface.

#Second check definition---- Check whether or not the vlan id is passed.

def second_check(vlan_id_Data1,ID):
	new_series=vlan_id_Data1
	matchers=['to']
	temp_arr1=[]
	for s in range(len(new_series)):
		temp_arr2=[]
		temp=[] 
		if new_series[s]!=matchers[0]:
			temp.append(new_series[s])
			temp_arr1=temp_arr1+temp
		if new_series[s]==matchers[0]:
			temp_arr2=temp_arr2+new_series[s-1::s+1]
			lb=int(new_series[s-1])
			ub=int(new_series[s+1])
			for c in range(lb,ub):
				temp_arr2.append(str(lb+1))
				lb=lb+1 
			temp_arr1=temp_arr1+temp_arr2 
	final_series=list(set(temp_arr1)-set(matchers))
	final_series= list(map(int, final_series))
	final_series.sort()
	return ID in final_series

def huawei_trunk_validation(IP_address,Data_from_interface,Vlan_id):
	Data_from_interface= Data_from_interface.split()  
	#first check---- Check whether it is trunk or not.
	if "link-type" in Data_from_interface : 
		index=Data_from_interface.index("link-type")
		if Data_from_interface[index+1].lower()== "trunk" and Data_from_interface[index+3].lower()=="trunk":
			print()
			print("For the switch IP",IP_address)
			print("Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"IS configured as a TRUNK port")
			#Vlan Data extraction from huawei switches
			vlan_index= Data_from_interface.index("allow-pass")+2
			vlan_id_Data=[]
			for i in range(vlan_index,len(Data_from_interface)):
				vlan_id_Data.append(Data_from_interface[i])
			#Second check function call
			check=second_check(vlan_id_Data,Vlan_id)
			if check:
				print("And Vlan",Vlan_id,"IS passed through the Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper())
			else:
				print("But Vlan",Vlan_id,"IS NOT passed through the Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"kindly configure the port by passing the vlan",Vlan_id)
		else:
			if "access" in Data_from_interface:
				print()
				print("For the switch IP",IP_address)
				print("Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"IS configured as an ACCESS port and should be changed to TRUNK")
			else:
				print()
				print("For the switch IP",IP_address)
				print("The Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"IS NOT properly configured as a TRUNK port")
				print("Please MODIFY the configuration")
	else:
		print("For the switch IP",IP_address)
		print("The Interface",Data_from_interface[Data_from_interface.index("interface")+1].upper(),"IS NOT configured as a TRUNK port")
		print("Please MODIFY the configuration")
