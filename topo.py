"""
Topologia de ejemplo
4 routers
4 hosts
1 controlador
"""

from mininet.topo import Topo
from clases import OVSQuaggaRouter, HostController

class MyTopo( Topo ):
  def __init__( self ):
    Topo.__init__( self )

    # Hosts
    h0 = self.addHost('h0')
    h1 = self.addHost('h1')
    h2 = self.addHost('h2')
    h3 = self.addHost('h3')
    
    # Galois
    galois = self.addHost('galois', loopback="127.0.0.1",
			  ips=['192.168.1.11','10.10.1.1','10.10.5.1','10.10.4.1'],
			  dpid='0000000000000001', cls=OVSQuaggaRouter)
    # Oz
    oz = self.addHost('oz', loopback="127.0.0.1",
		      ips=['192.168.1.12','10.10.1.2','10.10.6.2','10.10.3.1', '10.2.0.7', '10.3.0.7'],
		      dpid='0000000000000002', cls=OVSQuaggaRouter)
    
    # Possion
    possion = self.addHost('possion', loopback="127.0.0.1",
			  ips=['192.168.1.13','10.10.2.1','10.10.6.1','10.10.4.2'],
			  dpid='0000000000000003', cls=OVSQuaggaRouter)
    
    # Alice
    alice = self.addHost('alice', loopback="127.0.0.1",
			  ips=['192.168.1.14','10.10.2.2','10.10.5.2','10.10.3.2', '10.0.0.7', '10.1.0.7'],
			  dpid='0000000000000004', cls=OVSQuaggaRouter)
    
    # Controlador
    root = self.addHost('controller', cls=HostController,
			ip='192.168.1.10')
    
    # Switch de la red de gestion
    man_switch = self.addSwitch('s1', protocols='OpenFlow13', failMode='standalone')

    # Enlaces
    self.addLink(man_switch, galois, 1, 0)
    self.addLink(man_switch, oz, 2, 0)
    self.addLink(man_switch, possion, 3, 0)
    self.addLink(man_switch, alice, 4, 0)
    self.addLink(man_switch, root, 0, 0)
    
    self.addLink(galois, alice, 2, 2)
    self.addLink(galois, possion, 3, 3)
    self.addLink(galois, oz, 1, 1)
    self.addLink(alice, possion, 1, 1)
    self.addLink(alice, oz, 3, 3)
    self.addLink(oz, possion, 2, 2)
    
    self.addLink(alice, h0, 4, 0)
    self.addLink(alice, h1, 5, 0)
    
    self.addLink(oz, h2, 4, 0)
    self.addLink(oz, h3, 5, 0)








