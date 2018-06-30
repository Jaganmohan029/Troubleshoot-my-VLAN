#first get the input from the user
import Remote_Access

#Get the Data from the User about the number of switches, Vlan ID to troubleshoot and the switch topology information
number_of_switches=input("enter the number of switches ")
VLAN_ID=input("enter the VLAN ID to troubleshoot ")
Switch_data=[]

for k in range(int(number_of_switches)):
    Switch_data.append({"IP" : '', "Vendor" : '', "Username" : '', "Password" : '', "Enable_pass" : '', "TPort-1" : '', "TPort-2" : '', "APort" : ''})

for i in range(0,int(number_of_switches)):
  Switch_data[i]['IP']=input("enter the IP of switch-"+str(i+1)+" ")
  Switch_data[i]['Vendor']=input("enter the Vendor of switch- "+str(i+1)+" ")
  if Switch_data[i]['Vendor'].strip().lower() == "cisco":
   Switch_data[i]['Username']=input("enter the Username of switch- "+str(i+1)+" for SSH ")
   Switch_data[i]['Password']=input("enter the Password of switch- "+str(i+1)+" for SSH ")
   Switch_data[i]['Enable_pass']=input("enter the Enable Password of switch- "+str(i+1)+" for Running Config  ")
  else:
   Switch_data[i]['Username']=input("enter the Username of switch- "+str(i+1)+" for SSH ")
   Switch_data[i]['Password']=input("enter the Password of switch- "+str(i+1)+" for SSH ")

  if i==0 or i==int(number_of_switches)-1:
   Switch_data[i]['APort']=input("enter the Access port ")
   Switch_data[i]['TPort-1']=input("enter the First Trunk port ")
  else:
   Switch_data[i]['TPort-1']=input("enter the First Trunk port ")
   Switch_data[i]['TPort-2']=input("enter the Second Trunk port ")

#Calls the User_input function with the Switch_data which has been populated earlier and the VLAN_ID as the arguments   
Remote_Access.User_input(Switch_data,VLAN_ID)
