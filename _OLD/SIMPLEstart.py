#!/usr/bin/python

"""
Example network of Quagga routers
(QuaggaTopo + QuaggaService)
"""

import os
import sys
import atexit

# patch isShellBuiltin
import mininet.util
import mininext.util
mininet.util.isShellBuiltin = mininext.util.isShellBuiltin
sys.modules['mininet.util'] = mininet.util

from mininet.util import dumpNodeConnections
from mininet.node import OVSController, RemoteController, Node
from mininet.log import setLogLevel, info

from mininet.cli import CLI
from mininet.net import Mininet

from SIMPLEtopo import MyTopo

net = None

def setupSwitch(name):
  # Setup interfaces for OVS-Host (the ones not set by default)
  switch = net.get(name)
  switch.cmd('sudo ln -s /etc/openvswitch/conf.db /var/run/openvswitch/conf.db')
  switch.cmd('sudo ovs-vsctl add-br '+name)
  switch.cmd('sudo ovs-vsctl set bridge '+name+' protocols=OpenFlow13')
  switch.cmd('sudo ovs-vsctl set-controller '+name+' tcp:10.2.0.2:6633')
  switch.cmd('sudo ovs-vsctl add-port '+name+' s1-eth1')
  switch.cmd('sudo ovs-vsctl add-port '+name+' s1-eth2')
  #switch.cmd('sudo ovs-vsctl add-port '+name+' s1-eth2')
  switch.cmd('sudo ovs-vsctl set bridge '+name+' datapath_type=netdev')
  #switch.cmd('sudo ovs-vsctl set-fail-mode '+name+' secure')
  switch.cmd('sudo ovs-vsctl set bridge '+name+' datapath_id=0000000000000001')
  switch.cmd('sudo ovs-vsctl set bridge '+name+' other-config:datapath-id="0000000000000001"')
  switch.cmd('ifconfig s1-eth1 10.0.0.7 netmask 255.255.0.0')
  switch.cmd('ifconfig s1-eth2 10.1.0.7 netmask 255.255.0.0')
  switch.cmd('ifconfig s1-eth3 10.2.0.7 netmask 255.255.0.0')
  switch.cmd('route add 192.168.0.109/32 gw 10.2.0.2')
  switch.cmd('sysctl -w net.ipv4.ip_forward=0')

def startNetwork():
    "instantiates a topo, then starts the network and prints debug information"

    info('** Creating test topology\n')
    topo = MyTopo()

    info('** Starting the network\n')
    global net
    net = Mininet(topo, build=False)
    net.addController( 'c0' , controller=RemoteController, ip= "192.168.0.109", port=6633)
    
    net.start()
    h0 = net.get('h0')
    h0.cmd('ifconfig h0-eth0 10.0.0.1 netmask 255.255.0.0')
    h0.cmd('route add -net 10.1.0.0 netmask 255.255.0.0 dev h0-eth0')
    h1 = net.get('h1')
    h1.cmd('ifconfig h1-eth0 10.1.0.1 netmask 255.255.0.0')
    h1.cmd('route add -net 10.0.0.0 netmask 255.255.0.0 dev h1-eth0')
    
    s1 = net.get('s1')
    cont = net.get('controller')
    s1.start()
    cont.start()
    

    info('** Dumping host connections\n')
    dumpNodeConnections(net.hosts)

    #info('** Testing network connectivity\n')
    #net.ping(net.hosts)

    #info('** Dumping host processes\n')
    #for host in net.hosts:
        #host.cmdPrint("ps aux")

    info('** Running CLI\n')
    CLI(net)


def stopNetwork():
    "stops a network (only called on a forced cleanup)"

    if net is not None:
        info('** Tearing down Quagga network\n')
        net.stop()

if __name__ == '__main__':
    # Force cleanup on exit by registering a cleanup function
    atexit.register(stopNetwork)

    # Tell mininet to print useful information
    setLogLevel('info')
    startNetwork()
