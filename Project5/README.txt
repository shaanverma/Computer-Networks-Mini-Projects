#######################################################
# CS 4457 ASSIGNMENT 5 README                         #
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
The floodlight controller is now running. Open up another terminal and cd to the unzipped folder (Assignment5).
Type the following commands:

$sudo mn -c
$sudo python script.py

** If prompted for a password, type 'floodlight' **
** If this does not work, you may have to update the ip address of the floodlight controller or the port number **
** This will take some time **

########
#STEP 4#
########
When finished, exit mininet by typing 'exit'
-------------------------------------------------------------------------------------------------------------------------

CONTENTS of Output folder

This folder contains output files from the script.py that were run on my machine. When you run script.py, the files will be in the Assignment5 directory.

The 'pingOutput' file contains the outputs from the ping command for flow 1.
The 'F2output' file contains the output from the iperf command for the client of flow 2
The 'error' file contains any errors
The 'final' file contains the 4 QoS metrics






