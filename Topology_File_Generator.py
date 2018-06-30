import os

#Path for the INPUT file to get the network topology information from the user
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "Net_topology.txt")

#Get the data from the user to create the topology document by writing the file
with open(path, "w") as f:
  number_of_switches=input("Enter the number of switches ")
  f.write("The NUMBER of switches is : "+ number_of_switches+ "\n")
  VLAN_ID=input("Enter the VLAN ID to troubleshoot ")
  f.write("The Vlan_ID you have entered is : "+ VLAN_ID+ "\n")
  f.write("\n")
  for i in range(0,int(number_of_switches)):
	  f.write("Enter the IP of Switch-"+str(i+1)+" : \n")
	  f.write("Enter the VENDOR of Switch- "+str(i+1)+" : \n")
	  f.write("Enter the USERAME of Switch- "+str(i+1)+" for SSH : \n")
	  f.write("Enter the PASSWORD of Switch- "+str(i+1)+" for SSH : \n")
	  f.write("Enter the ENABLE PASSWORD of Switch - "+str(i+1)+"(for Running Config if the vendor is CISCO else TYPE 'NA' in this field) : \n")
	  if i==0 or i==int(number_of_switches)-1:
		  f.write("Enter the ACCESS port : \n")
		  f.write("Enter the FIRST TRUNK port : \n")
	  else:
		  f.write("Enter the FIRST TRUNK port : \n")
		  f.write("Enter the SECOND TRUNK port : \n")
	  f.write("\n")
