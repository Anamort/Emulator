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

from topo import MyTopo

net = None

def startNetwork():
  "instantiates a topo, then starts the network and prints debug information"

  info('** Creating test topology\n')
  topo = MyTopo()

  info('** Starting the network\n')
  global net
  net = Mininet(topo, controller=None)
  
  net.start()
  
  h0 = net.get('h0')
  h0.cmd('ifconfig h0-eth0 10.0.0.1 netmask 255.255.0.0')
  h0.cmd('route add -net 10.0.0.0 netmask 255.0.0.0 dev h0-eth0')
  h1 = net.get('h1')
  h1.cmd('ifconfig h1-eth0 10.1.0.1 netmask 255.255.0.0')
  h1.cmd('route add -net 10.0.0.0 netmask 255.0.0.0 dev h1-eth0')
  
  h2 = net.get('h2')
  h2.cmd('ifconfig h2-eth0 10.2.0.1 netmask 255.255.0.0')
  h2.cmd('route add -net 10.0.0.0 netmask 255.0.0.0 dev h2-eth0')
  h3 = net.get('h3')
  h3.cmd('ifconfig h3-eth0 10.3.0.1 netmask 255.255.0.0')
  h3.cmd('route add -net 10.0.0.0 netmask 255.0.0.0 dev h3-eth0')
  
  for node in ['alice','oz','galois','possion','controller']:
    n = net.get(node)
    n.start()

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
