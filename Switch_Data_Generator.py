#first get the input from the user
import Remote_Access
import os

#Path for the INPUT file to get the network topology information from the user
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "Net_topology.txt")

#Get the data from the File by reading it and assigning the variables to the Switch_data
with open(path, "r") as f:
	Data= f.readlines()
	Data = [s.rstrip() for s in Data]
	Data = list(filter(None, Data))
	number_of_switches = Data[0].split()[Data[0].split().index(":")+1].strip()
	VLAN_ID= Data[1].split()[Data[1].split().index(":")+1].strip()
	Switch_data=[]

	for k in range(int(number_of_switches)):
		Switch_data.append({"IP" : '', "Vendor" : '', "Username" : '', "Password" : '', "Enable_pass" : '', "TPort-1" : '', "TPort-2" : '', "APort" : ''})
	
	i = 2
	j = 0 
	while i<len(Data):
		Switch_data[j]['IP']=Data[i].split()[Data[i].split().index(":")+1].strip()
		Switch_data[j]['Vendor']=Data[i+1].split()[Data[i+1].split().index(":")+1].strip()
		if Switch_data[j]['Vendor'].strip().lower() == "cisco":
			Switch_data[j]['Username']=Data[i+2].split()[Data[i+2].split().index(":")+1].strip()
			Switch_data[j]['Password']=Data[i+3].split()[Data[i+3].split().index(":")+1].strip()
			Switch_data[j]['Enable_pass']=Data[i+4].split()[Data[i+4].split().index(":")+1].strip()
		else:
			Switch_data[j]['Username']=Data[i+2].split()[Data[i+2].split().index(":")+1].strip()
			Switch_data[j]['Password']=Data[i+3].split()[Data[i+3].split().index(":")+1].strip()
		if j==0 or j==int(number_of_switches)-1:
			Switch_data[j]['APort']= Data[i+5].split()[Data[i+5].split().index(":")+1].strip()
			Switch_data[j]['TPort-1']=Data[i+6].split()[Data[i+6].split().index(":")+1].strip()
		else:
			Switch_data[j]['TPort-1']= Data[i+5].split()[Data[i+5].split().index(":")+1].strip()
			Switch_data[j]['TPort-2']=Data[i+6].split()[Data[i+6].split().index(":")+1].strip()
		i = i+7
		j = j+1

#User_input is the function which remote accesses the switches and gets the configuration	
Remote_Access.User_input(Switch_data,VLAN_ID)
  
