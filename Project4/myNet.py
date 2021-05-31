#!/usr/bin/python

"""
Cs 4457 Assignment #4
NAME: Shaan Verma
Student #: 250804514
DESCRIPTION: This python script creates a network with 8 hosts, 14 switches, and 21 links. It then runs a 
simulation by getting each host to ping the other hosts. A TCPdump is run on each host. The contents of the pings
are stored in the file 'pings', and the TCPdump commands are stored in their own file corresponding to the
host name i.e. 'dumph1'. Ping errors are stored in 'errorPing' and TCPdump errors are stored in 'errorDump'.
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

    #Waiting 5 seconds to make sure all aspects of the network are configured    
    info('\n*** Wait 5 seconds for the network to configure\n')
    time.sleep(5)

    #tcpdump commands for all hosts
    info( '\n\n*** Starting tcpdumps for all hosts\n\n MAY TAKE A COUPLE OF MINUTES!!\n\n')
    for h in servers:
        c = 'h' + str(servers.index(h) + 1)
        print(c)
        h.cmdPrint('printf "Host' + c + '\n#######################\n\n" >> dump' + c ,'; tcpdump -n -i ' + c + '-eth0 >> dump' + c + ' 2> errorDump &')

    #Pings all hosts
    info( '*** Pinging all hosts from one another. Total 56 pings\n')
    for client in hosts:
        for server in servers:
            if (client != server):
               clientNum = str(hosts.index(client) + 1)
               serverNum = str(servers.index(server) + 1)
               a = hosts.index(client)
               b = servers.index(server)
               hosts[a].cmdPrint('printf "HOST' + clientNum + ' PINGING HOST' + serverNum + '\n######################\n\n" >> pings',';','ping -c 1', servers[b].IP(), '>> pings', ' 2> errorPing')
               time.sleep(0.3)

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

