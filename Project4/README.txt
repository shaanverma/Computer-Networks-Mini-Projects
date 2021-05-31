#######################################################
# CS 4457 ASSIGNMENT 4 README                         #
# NAME:Shaan Verma                                    #
# STUDENT #: 250804514                                #
# DESCRIPTION: Instructions to operate the assignment #
#######################################################

INSTRUCTIONS TO RUN THE PYTHON SCRIPT

########
#STEP 1#
########
The floodlight VM should be used to ensure all the ip addresses and port numbers match.
Setup the floodlight VM, and download the zip file from owl and unzip the contents.

########
#STEP 2#
########
Once the VM is set up, open a terminal and use the following commands to get the floodlight controller running:

$cd ~/floodlight
$ant
$java -jar target/floodlight.jar

########
#STEP 3#
########
The floodlight controller is now running. Open up another terminal and cd to the unzipped folder (Assignment 4).
Type the following commands:

$sudo mn -c
$sudo python myNet.py

** If prompted for a password, type 'floodlight' **
** If this does not work, you may have to update the ip address of the floodlight controller or the port number **

########
#STEP 4#
########
When finished, exit mininet by typing 'exit'
-------------------------------------------------------------------------------------------------------------------------

CONTENTS of Output folder

This folder contains output files from the myNet.py that were run on my machine. When you run myNet.py, the files will be in the Assignment 4 directory.

The 'pings' file contains the outputs from the ping commands. Each host pings the other host once. Total of 56 pings. The file is formatted with names of the participating hosts at the top.
The 'dumph1' file contains the output of the tcpdump command of host 1
The 'dumph2' file contains the output of the tcpdump command of host 2
The 'dumph3' file contains the output of the tcpdump command of host 3
The 'dumph4' file contains the output of the tcpdump command of host 4
The 'dumph5' file contains the output of the tcpdump command of host 5
The 'dumph6' file contains the output of the tcpdump command of host 6
The 'dumph7' file contains the output of the tcpdump command of host 7
The 'dumph8' file contains the output of the tcpdump command of host 8

The 'errorPing' file contains errors from any of the above ping commands
The 'errorDump' file contains errors from any of the tcpdump commands 

** To ping all the hosts quickly, use the command, mininet> pingall
 






