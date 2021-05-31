#!/usr/bin/python

"""
Cs 4457 Assignment #5
NAME: Shaan Verma
Student #: 250804514
DESCRIPTION: This python script creates a network with 8 hosts, 14 switches, and 21 links. It then runs a 
two flows f1 and f2. From f1 ping is used to calculate latency and jitter. From f2, iperf is used to get throughput
and packet loss. All errors are stored in the 'error' file.
"""

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import time
import math

#Function definition
def myNetwork():
    net = Mininet( topo=None, build=False, ipBase='10.0.0.0/8')
    
    #Adding floodlight controller
    info( '*** Adding controller\n' )
    c0=net.addController(name='c0', controller=RemoteController,ip="127.0.0.1",protocol='tcp',port=6653)
    
    #Adding 14 switches to network
    info( '*** Adding switches\n' )
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch)

    #Adding 8 Hosts to network
    info( '*** Adding hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None) 

    #Adding 21 links to create given topology
    info( '*** Creating links\n' )
    net.addLink(h1,s1,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s1,s2,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s1,s4,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s2,s3,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s3,s5,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s5,s6,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s6,h2,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s2,s7,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s7,s8,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s8,h3,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s7,s9,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s9,s10,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s10,s11,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s11,s12,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s12,h4,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s10,h5,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s9,s13,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s13,s14,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s14,h7,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s14,h8,cls=TCLink,bw=15,delay='1ms',loss=1)
    net.addLink(s13,h6,cls=TCLink,bw=15,delay='1ms',loss=1)
    
    #Building the network topology
    info( '*** Starting network\n')
    net.build()
   
    #Starting the floodlight controller
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()  

    #Starting floodlight switches
    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0]) 
    net.get('s3').start([c0]) 
    net.get('s4').start([c0]) 
    net.get('s5').start([c0]) 
    net.get('s6').start([c0]) 
    net.get('s7').start([c0]) 
    net.get('s8').start([c0]) 
    net.get('s9').start([c0])
    net.get('s10').start([c0]) 
    net.get('s11').start([c0]) 
    net.get('s12').start([c0]) 
    net.get('s13').start([c0]) 
    net.get('s14').start([c0])

    info( '*** Post configure switches and hosts\n')
    hosts = net.hosts
    servers = net.hosts

    #Gives time to the network. Without this it does not always work
    info( '*** Wait 5 seconds for the network to be set up\n')
    time.sleep(5)

    #Flow 1 command
    hosts[0].cmdPrint('ping -c100 ', servers[6].IP(), ' >> pingOutput', ' 2> error')
    
    time.sleep(5)
    
    #Flow 2 client and server commands for 100 seconds
    hosts[6].cmdPrint('iperf -s -u -t100 2> error &')
    hosts[0].cmdPrint('iperf -c 10.0.0.7 -u -b 6000000 -t100 >> F2output 2> error')
 
    #Waits for flows to finish up
    time.sleep(5)
    

    #Opening ping files and placing rtt values from ping into list
    f = open("pingOutput", "r")
    Lines = f.readlines()
    rttValues = []
    latency = 0.0
    jitter = 0.0
    for line in Lines:
        holder = line.strip().split()
        if (line.split() and holder[3] == '10.0.0.7:'):
           x = float(holder[6][5:])
           rttValues.append(x)
    f.close()

    #Opening iperf file and placing bandwidth and packetloss data into list
    f2 = open("F2output", "r")
    rows = f2.readlines()
    values = []

    for j in rows:
       holder2 = j.split()
 
       for z in holder2:
           if (z == 'Mbits/sec'):
              values.append(holder2)
    f2.close()
        
    #Calculating average RTT latency
    for i in rttValues:
        latency = latency + i
    latency = str(latency/len(rttValues))

    #Calculating Jitter
    first = rttValues[0]
    for i in range(0, len(rttValues)-1):
        jitter = jitter + abs(rttValues[i+1] - rttValues[i])
    jitter = str(jitter/(len(rttValues)-1))

    #Grabbing Throughput from both client and server, and packet loss
    clientThroughput = values[0][6] + ' ' + values[0][7]
    serverThroughput = values[1][6] + ' ' + values[1][7]
    packetLoss = values[1][11][1:5]
    
    #Outputing metrics to 'final' file
    myFile = open("final", "w")
    myFile.write("FLOW 1 METRICS:\n")
    myFile.write("Average RTT latency = " + latency + " ms" + "\n")
    myFile.write("Jitter = " + jitter + " ms" + "\n\n")
    myFile.write("FLOW 2 METRICS:\n")
    myFile.write("Throughput from client: " + clientThroughput + "\n")
    myFile.write("Throughput from server: " + serverThroughput + "\n")
    myFile.write("PacketLoss: " + packetLoss + "\n")
    myFile.close()
    

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

