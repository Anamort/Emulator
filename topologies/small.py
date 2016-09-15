"""
Topologia de ejemplo
Fuente: http://www.topology-zoo.org/maps/HiberniaCanada.jpg
11 RAUSwitch
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
    h0 = self.addHost('h0', ips=['10.0.1.2/24'], gw='10.0.1.1', cls=RAUHost)
    h1 = self.addHost('h1', ips=['10.1.1.2/24'], gw='10.1.1.1', cls=RAUHost)

    routerLan1 = self.addHost('routerLan1', ips=['10.0.0.1/24', '10.0.1.1/24'],
                                ce_mac_address='00:00:00:00:00:01',
                                gw='10.0.0.2', cls=QuaggaRouter)

    routerLan2 = self.addHost('routerLan2', ips=['10.1.0.1/24', '10.1.1.1/24'],
                                ce_mac_address='00:00:00:00:00:02',
                                gw='10.1.0.2', cls=QuaggaRouter)
    

    switch1 = self.addHost('switch1', ips=['192.168.1.11/24','10.10.1.1/24','10.0.0.2/24'],
			  controller_ip="192.168.1.10",
              border=1, ce_ip_address='10.0.0.1', ce_mac_address='00:00:00:00:00:01',
			  cls=RAUSwitch)

    switch2 = self.addHost('switch2', ips=['192.168.1.12/24','10.10.4.1/24','10.10.5.1/24','10.1.0.2/24'],
	      controller_ip="192.168.1.10",
          border=1, ce_ip_address='10.1.0.1', ce_mac_address='00:00:00:00:00:02',
	      cls=RAUSwitch)
    

    switch3 = self.addHost('switch3', ips=['192.168.1.13/24','10.10.1.2/24','10.10.3.1/24','10.10.2.1/24'],
			  controller_ip="192.168.1.10",
			  cls=RAUSwitch)
    

    switch4 = self.addHost('switch4', ips=['192.168.1.14/24','10.10.3.2/24','10.10.6.1/24'],
			  controller_ip="192.168.1.10",
			  cls=RAUSwitch)

    switch5 = self.addHost('switch5', ips=['192.168.1.15/24','10.10.4.2/24','10.10.7.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch6 = self.addHost('switch6', ips=['192.168.1.16/24','10.10.7.2/24','10.10.8.1/24','10.10.9.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch7 = self.addHost('switch7', ips=['192.168.1.17/24','10.10.8.2/24','10.10.10.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch8 = self.addHost('switch8', ips=['192.168.1.18/24','10.10.10.2/24','10.10.11.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch9 = self.addHost('switch9', ips=['192.168.1.19/24','10.10.6.2/24','10.10.11.2/24','10.10.12.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch10 = self.addHost('switch10', ips=['192.168.1.20/24','10.10.5.2/24','10.10.9.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch11 = self.addHost('switch11', ips=['192.168.1.21/24','10.10.2.2/24','10.10.12.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    # Controlador
    controller = self.addHost('controller', cls=RAUController, ips=['192.168.1.10/24'])
    
    # Switch de la red de gestion
    man_switch = self.addSwitch('s1', protocols='OpenFlow13', failMode='standalone')

    # Enlaces
    self.addLink(man_switch, switch1, 2, 0)
    self.addLink(man_switch, switch2, 3, 0)
    self.addLink(man_switch, switch3, 4, 0)
    self.addLink(man_switch, switch4, 5, 0)
    self.addLink(man_switch, switch5, 6, 0)
    self.addLink(man_switch, switch6, 7, 0)
    self.addLink(man_switch, switch7, 8, 0)
    self.addLink(man_switch, switch8, 9, 0)
    self.addLink(man_switch, switch9, 10, 0)
    self.addLink(man_switch, switch10, 11, 0)
    self.addLink(man_switch, switch11, 12, 0)
    self.addLink(man_switch, controller, 1, 0)
    
    self.addLink(switch1, switch3, 1, 1)
    self.addLink(switch3, switch4, 2, 1)
    self.addLink(switch2, switch5, 1, 1)
    self.addLink(switch2, switch10, 2, 1)
    self.addLink(switch3, switch11, 3, 1)
    self.addLink(switch4, switch9, 2, 1)
    self.addLink(switch5, switch6, 2, 1)
    self.addLink(switch6, switch7, 2, 1)
    self.addLink(switch6, switch10, 3, 2)
    self.addLink(switch7, switch8, 2, 1)
    self.addLink(switch8, switch9, 2, 2)
    self.addLink(switch9, switch11, 3, 2)

    ## Enlaces CE
    self.addLink(switch1, routerLan1, 2, 0)
    self.addLink(switch2, routerLan2, 3, 0)
    self.addLink(h0, routerLan1, 0, 1)
    self.addLink(h1, routerLan2, 0, 1)


