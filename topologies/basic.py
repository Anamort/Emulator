"""
Topologia basica
4 routers SDN
2 routers Quagga
2 hosts
1 controlador
"""

from mininet.topo import Topo
from clases import RAUSwitch, QuaggaRouter, RAUController, RAUHost

class CustomTopology( Topo ):
  def __init__( self ):
    Topo.__init__( self )

    # Hosts
    h0 = self.addHost('h0', ip='10.0.1.2/24', gw='10.0.1.1', cls=RAUHost)
    h1 = self.addHost('h1', ip='10.1.1.2/24', gw='10.1.1.1', cls=RAUHost)

    routerLan1 = self.addHost('routerLan1', ips=['10.0.0.1/24', '10.0.1.1/24'],
                                loopback='127.0.0.1', ce_mac_address='00:00:00:00:00:01',
                                gw='10.0.0.2', cls=QuaggaRouter)

    routerLan2 = self.addHost('routerLan2', ips=['10.1.0.1/24', '10.1.1.1/24'],
                                loopback='127.0.0.1', ce_mac_address='00:00:00:00:00:02',
                                gw='10.1.0.2', cls=QuaggaRouter)
    
    # Galois
    galois = self.addHost('galois', loopback="127.0.0.1",
			  ips=['192.168.1.11/24','10.10.1.1/24','10.10.5.1/24','10.10.4.1/24'],
			  dpid='0000000000000001', controller_ip="192.168.1.10",
			  cls=RAUSwitch)
    # Oz
    oz = self.addHost('oz', loopback="127.0.0.1",
		      ips=['192.168.1.12/24','10.10.1.2/24','10.10.6.2/24','10.10.3.1/24', '10.1.0.2/24'],
		      dpid='0000000000000002', controller_ip="192.168.1.10",
              border=1, ce_ip_address='10.1.0.1', ce_mac_address='00:00:00:00:00:02',
		      cls=RAUSwitch)
    
    # Possion
    possion = self.addHost('possion', loopback="127.0.0.1",
			  ips=['192.168.1.13/24','10.10.2.1/24','10.10.6.1/24','10.10.4.2/24'],
			  dpid='0000000000000003', controller_ip="192.168.1.10",
			  cls=RAUSwitch)
    
    # Alice
    alice = self.addHost('alice', loopback="127.0.0.1",
			  ips=['192.168.1.14/24','10.10.2.2/24','10.10.5.2/24','10.10.3.2/24', '10.0.0.2/24'],
			  dpid='0000000000000004', controller_ip="192.168.1.10",
              border=1, ce_ip_address='10.0.0.1', ce_mac_address='00:00:00:00:00:01',
			  cls=RAUSwitch)
    
    # Controlador
    root = self.addHost('controller', cls=RAUController,
			ip='192.168.1.10/24')
    
    # Switch de la red de gestion
    man_switch = self.addSwitch('s1', protocols='OpenFlow13', failMode='standalone')

    # Enlaces
    self.addLink(man_switch, galois, 2, 0)
    self.addLink(man_switch, oz, 3, 0)
    self.addLink(man_switch, possion, 4, 0)
    self.addLink(man_switch, alice, 5, 0)
    self.addLink(man_switch, root, 1, 0)
    
    self.addLink(galois, alice, 2, 2)
    self.addLink(galois, possion, 3, 3)
    self.addLink(galois, oz, 1, 1)
    self.addLink(alice, possion, 1, 1)
    self.addLink(alice, oz, 3, 3)
    self.addLink(oz, possion, 2, 2)
    
    self.addLink(alice, routerLan1, 4, 0)
    
    self.addLink(oz, routerLan2, 4, 0)

    self.addLink(h0, routerLan1, 0, 1)
    
    self.addLink(h1, routerLan2, 0, 1)




