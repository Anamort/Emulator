"""
Topologia de ejemplo
Fuente: http://www.topology-zoo.org/maps/HiberniaCanada.jpg
12 routers SDN
2 routers Quagga
2 hosts
1 controlador
"""

from mininet.topo import Topo
from rau_nodes import RAUSwitch, QuaggaRouter, RAUController, RAUHost

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
    

    router1 = self.addHost('router1', loopback="127.0.0.1",
			  ips=['192.168.1.11/24','10.10.1.1/24','10.0.0.2/24'],
			  controller_ip="192.168.1.10",
              border=1, ce_ip_address='10.0.0.1', ce_mac_address='00:00:00:00:00:01',
			  cls=RAUSwitch)

    router2 = self.addHost('router2', loopback="127.0.0.1",
	      ips=['192.168.1.12/24','10.10.4.1/24','10.10.5.1/24'],
	      controller_ip="192.168.1.10",
	      cls=RAUSwitch)
    

    router3 = self.addHost('router3', loopback="127.0.0.1",
			  ips=['192.168.1.13/24','10.10.1.2/24','10.10.3.1/24','10.10.2.1/24','10.1.0.2/24'],
			  controller_ip="192.168.1.10",
               border=1, ce_ip_address='10.1.0.1', ce_mac_address='00:00:00:00:00:02',
			  cls=RAUSwitch)
    

    router4 = self.addHost('router4', loopback="127.0.0.1",
			  ips=['192.168.1.14/24','10.10.3.2/24','10.10.6.1/24'],
			  controller_ip="192.168.1.10",
			  cls=RAUSwitch)

    router5 = self.addHost('router5', loopback="127.0.0.1",
        ips=['192.168.1.15/24','10.10.4.2/24','10.10.7.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router6 = self.addHost('router6', loopback="127.0.0.1",
        ips=['192.168.1.16/24','10.10.7.2/24','10.10.8.1/24','10.10.9.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router7 = self.addHost('router7', loopback="127.0.0.1",
        ips=['192.168.1.17/24','10.10.8.2/24','10.10.10.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router8 = self.addHost('router8', loopback="127.0.0.1",
        ips=['192.168.1.18/24','10.10.10.2/24','10.10.11.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router9 = self.addHost('router9', loopback="127.0.0.1",
        ips=['192.168.1.19/24','10.10.6.2/24','10.10.11.2/24','10.10.12.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router10 = self.addHost('router10', loopback="127.0.0.1",
        ips=['192.168.1.20/24','10.10.5.2/24','10.10.9.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router11 = self.addHost('router11', loopback="127.0.0.1",
        ips=['192.168.1.21/24','10.10.2.2/24','10.10.12.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    # Controlador
    root = self.addHost('controller', cls=RAUController,
      ip='192.168.1.10/24')
    
    # Switch de la red de gestion
    man_switch = self.addSwitch('s1', protocols='OpenFlow13', failMode='standalone')

    # Enlaces
    self.addLink(man_switch, router1, 2, 0)
    self.addLink(man_switch, router2, 3, 0)
    self.addLink(man_switch, router3, 4, 0)
    self.addLink(man_switch, router4, 5, 0)
    self.addLink(man_switch, router5, 6, 0)
    self.addLink(man_switch, router6, 7, 0)
    self.addLink(man_switch, router7, 8, 0)
    self.addLink(man_switch, router8, 9, 0)
    self.addLink(man_switch, router9, 10, 0)
    self.addLink(man_switch, router10, 11, 0)
    self.addLink(man_switch, router11, 12, 0)
    self.addLink(man_switch, root, 1, 0)
    
    self.addLink(router1, router3, 1, 1)
    self.addLink(router3, router4, 2, 1)
    self.addLink(router2, router5, 1, 1)
    self.addLink(router2, router10, 2, 1)
    self.addLink(router3, router11, 3, 1)
    self.addLink(router4, router9, 2, 1)
    self.addLink(router5, router6, 2, 1)
    self.addLink(router6, router7, 2, 1)
    self.addLink(router6, router10, 3, 2)
    self.addLink(router7, router8, 2, 1)
    self.addLink(router8, router9, 2, 2)
    self.addLink(router9, router11, 3, 2)

    ## Enlaces CE
    self.addLink(router1, routerLan1, 2, 0)
    self.addLink(router3, routerLan2, 4, 0)
    self.addLink(h0, routerLan1, 0, 1)
    self.addLink(h1, routerLan2, 0, 1)


