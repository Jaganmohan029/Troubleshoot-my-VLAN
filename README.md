# Troubleshoot-my-VLAN
A collection of python codes to automate the hectic job of troubleshooting misconfigured VLAN-IDs in the L-2 Network devices and to report the errors caused due to improperly passing the VLANs through the interfaces.
Once the recommended modifications as per the report are done,the end to end connectivity will be restored. However, this project has its own limitations and recommendations.


Coming to the software requirements part, To make the modules to execute on your system, you have to have 
* Python3
* Netmiko library (for automating SSH access)
installed on the system. The programs run on all Windows and Linux based platforms when they have the aforementioned softwares installed.


Limitations with the codes:
* The codes should be run on a server or a PC which has direct reachability (One Hop connectivity) to all the switches that you want to troubleshoot.
* All the switches must be configured with SSH protocol for remote access which is safe and secure. I am working to develop for Telnet access too and will be done sooner.


Recommendations:
* Make sure all the interfaces involved in the troubleshooting process are in UP state. Currently the tool is not capable of checking the port status.
* To make the code to crawl through the network you have to give the necessary access and port level information of the network devices.
* Please fill all the fields in the Net_topology.txt file without fail else the troubleshooter will not execute and ends up throwing errors. As of now, the code is not mature to validate the User input but I am working on it. If you have any doubts kindly go through the Sample_Net_topology.txt file with the sample network information.


Steps to Run the troubleshooter:

Step-1: Run the Topology_File_Generator.py and input the Number of Switches and the VLAN Id to troubleshoot. Once these are entered by the user the code generates the Net_topoloy.txt file with the required fields to understand the network and access the network devices.

Step-2: Run the Switch_Data_Generator.py. It will get the data as given by the user in the Net_topology.py file and access the switches and take the configuration of the interfaces entered and check if or not they are configured as the trunk or access ports and passed the VLANs and finally report the results.

[OR]

Please Run the Run_Time_Input.py file skipping the above steps and input the topology information sequentially when prompted and get the job done.
