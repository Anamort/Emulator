"""
Topologia de ejemplo
Fuente: http://www.topology-zoo.org/maps/Bellcanada.jpg
45 routers SDN
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
	      ips=['192.168.1.12/24','10.10.1.2/24','10.10.2.1/24'],
	      controller_ip="192.168.1.10",
	      cls=RAUSwitch)
    

    router3 = self.addHost('router3', loopback="127.0.0.1",
		  ips=['192.168.1.13/24','10.10.3.1/24','10.10.8.1/24','10.10.9.1/24'],
		  controller_ip="192.168.1.10",
		  cls=RAUSwitch)
    

    router4 = self.addHost('router4', loopback="127.0.0.1",
		  ips=['192.168.1.14/24','10.10.2.2/24','10.10.3.2/24','10.10.4.1/24','10.10.6.1/24'],
		  controller_ip="192.168.1.10",
		  cls=RAUSwitch)

    router5 = self.addHost('router5', loopback="127.0.0.1",
        ips=['192.168.1.15/24','10.10.4.2/24','10.10.5.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router6 = self.addHost('router6', loopback="127.0.0.1",
        ips=['192.168.1.16/24','10.10.5.2/24','10.10.7.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router7 = self.addHost('router7', loopback="127.0.0.1",
        ips=['192.168.1.17/24','10.10.6.2/24','10.10.7.2/24','10.10.25.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router8 = self.addHost('router8', loopback="127.0.0.1",
        ips=['192.168.1.18/24','10.10.8.2/24','10.10.10.1/24','10.10.14.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router9 = self.addHost('router9', loopback="127.0.0.1",
        ips=['192.168.1.19/24','10.10.10.2/24','10.10.11.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router10 = self.addHost('router10', loopback="127.0.0.1",
        ips=['192.168.1.20/24','10.10.11.2/24','10.10.12.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router11 = self.addHost('router11', loopback="127.0.0.1",
        ips=['192.168.1.21/24','10.10.12.2/24','10.10.13.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router12 = self.addHost('router12', loopback="127.0.0.1",
              ips=['192.168.1.22/24','10.10.14.2/24','10.10.13.2/24','10.10.19.1/24','10.10.20.1/24','10.10.18.1/24','10.10.21.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    router13 = self.addHost('router13', loopback="127.0.0.1",
          ips=['192.168.1.23/24','10.10.19.2/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    router14 = self.addHost('router14', loopback="127.0.0.1",
              ips=['192.168.1.24/24','10.10.20.2/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    router15 = self.addHost('router15', loopback="127.0.0.1",
              ips=['192.168.1.25/24','10.10.18.2/24','10.10.17.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    router16 = self.addHost('router16', loopback="127.0.0.1",
        ips=['192.168.1.26/24','10.10.9.2/24','10.10.17.2/24','10.10.15.1/24','10.10.16.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router17 = self.addHost('router17', loopback="127.0.0.1",
        ips=['192.168.1.27/24','10.10.15.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router18 = self.addHost('router18', loopback="127.0.0.1",
        ips=['192.168.1.28/24','10.10.16.2/24','10.10.22.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router19 = self.addHost('router19', loopback="127.0.0.1",
        ips=['192.168.1.29/24','10.10.21.2/24','10.10.23.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router20 = self.addHost('router20', loopback="127.0.0.1",
        ips=['192.168.1.30/24','10.10.22.2/24','10.10.24.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router21 = self.addHost('router21', loopback="127.0.0.1",
        ips=['192.168.1.31/24','10.10.23.2/24','10.10.24.2/24','10.10.29.1/24','10.10.31.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router22 = self.addHost('router22', loopback="127.0.0.1",
        ips=['192.168.1.32/24','10.10.29.2/24','10.10.26.1/24','10.10.30.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router23 = self.addHost('router23', loopback="127.0.0.1",
              ips=['192.168.1.33/24','10.10.26.2/24','10.10.27.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    router24 = self.addHost('router24', loopback="127.0.0.1",
          ips=['192.168.1.34/24','10.10.27.2/24','10.10.28.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    router25 = self.addHost('router25', loopback="127.0.0.1",
              ips=['192.168.1.35/24','10.10.31.2/24','10.10.32.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    router26 = self.addHost('router26', loopback="127.0.0.1",
              ips=['192.168.1.36/24','10.10.32.2/24','10.10.33.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    router27 = self.addHost('router27', loopback="127.0.0.1",
        ips=['192.168.1.37/24','10.10.30.2/24','10.10.33.2/24','10.10.34.1/24','10.10.35.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router28 = self.addHost('router28', loopback="127.0.0.1",
        ips=['192.168.1.38/24','10.10.34.2/24','10.10.36.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router29 = self.addHost('router29', loopback="127.0.0.1",
        ips=['192.168.1.39/24','10.10.25.2/24','10.10.28.2/24','10.10.37.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router30 = self.addHost('router30', loopback="127.0.0.1",
        ips=['192.168.1.40/24','10.10.35.2/24','10.10.39.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router31 = self.addHost('router31', loopback="127.0.0.1",
        ips=['192.168.1.41/24','10.10.36.2/24','10.10.37.2/24','10.10.38.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router32 = self.addHost('router32', loopback="127.0.0.1",
        ips=['192.168.1.42/24','10.10.39.2/24','10.10.38.2/24','10.10.41.1/24','10.10.40.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router33 = self.addHost('router33', loopback="127.0.0.1",
        ips=['192.168.1.43/24','10.10.41.2/24','10.10.42.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router34 = self.addHost('router34', loopback="127.0.0.1",
              ips=['192.168.1.44/24','10.10.40.2/24','10.10.42.2/24','10.10.43.1/24','10.10.45.1/24','10.10.44.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    router35 = self.addHost('router35', loopback="127.0.0.1",
          ips=['192.168.1.45/24','10.10.43.2/24','10.10.46.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    router36 = self.addHost('router36', loopback="127.0.0.1",
              ips=['192.168.1.46/24','10.10.46.2/24','10.10.47.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    router37 = self.addHost('router37', loopback="127.0.0.1",
              ips=['192.168.1.47/24','10.10.47.2/24','10.10.48.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    router38 = self.addHost('router38', loopback="127.0.0.1",
        ips=['192.168.1.48/24','10.10.48.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router39 = self.addHost('router39', loopback="127.0.0.1",
        ips=['192.168.1.49/24','10.10.45.2/24','10.10.49.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router40 = self.addHost('router40', loopback="127.0.0.1",
        ips=['192.168.1.50/24','10.10.49.2/24','10.10.50.1/24','10.10.51.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router41 = self.addHost('router41', loopback="127.0.0.1",
        ips=['192.168.1.51/24','10.10.44.2/24','10.10.50.2/24','10.10.53.1/24','10.10.52.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router42 = self.addHost('router42', loopback="127.0.0.1",
        ips=['192.168.1.52/24','10.10.53.2/24','10.10.54.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router43 = self.addHost('router43', loopback="127.0.0.1",
        ips=['192.168.1.53/24','10.10.52.2/24','10.10.54.2/24','10.10.55.1/24','10.10.56.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router44 = self.addHost('router44', loopback="127.0.0.1",
        ips=['192.168.1.54/24','10.10.51.2/24','10.10.55.2/24','10.10.57.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router45 = self.addHost('router45', loopback="127.0.0.1",
        ips=['192.168.1.55/24','10.10.56.2/24','10.10.57.2/24','10.1.0.2/24'],
        controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.1.0.1', ce_mac_address='00:00:00:00:00:02',
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
    self.addLink(man_switch, router12, 13, 0)
    self.addLink(man_switch, router13, 14, 0)
    self.addLink(man_switch, router14, 15, 0)
    self.addLink(man_switch, router15, 16, 0)
    self.addLink(man_switch, router16, 17, 0)
    self.addLink(man_switch, router17, 18, 0)
    self.addLink(man_switch, router18, 19, 0)
    self.addLink(man_switch, router19, 20, 0)
    self.addLink(man_switch, router20, 21, 0)
    self.addLink(man_switch, router21, 22, 0)
    self.addLink(man_switch, router22, 23, 0)
    self.addLink(man_switch, router23, 24, 0)
    self.addLink(man_switch, router24, 25, 0)
    self.addLink(man_switch, router25, 26, 0)
    self.addLink(man_switch, router26, 27, 0)
    self.addLink(man_switch, router27, 28, 0)
    self.addLink(man_switch, router28, 29, 0)
    self.addLink(man_switch, router29, 30, 0)
    self.addLink(man_switch, router30, 31, 0)
    self.addLink(man_switch, router31, 32, 0)
    self.addLink(man_switch, router32, 33, 0)
    self.addLink(man_switch, router33, 34, 0)
    self.addLink(man_switch, router34, 35, 0)
    self.addLink(man_switch, router35, 36, 0)
    self.addLink(man_switch, router36, 37, 0)
    self.addLink(man_switch, router37, 38, 0)
    self.addLink(man_switch, router38, 39, 0)
    self.addLink(man_switch, router39, 40, 0)
    self.addLink(man_switch, router40, 41, 0)
    self.addLink(man_switch, router41, 42, 0)
    self.addLink(man_switch, router42, 43, 0)
    self.addLink(man_switch, router43, 44, 0)
    self.addLink(man_switch, router44, 45, 0)
    self.addLink(man_switch, router45, 46, 0)
    self.addLink(man_switch, root, 1, 0)
    
    self.addLink(router1, router2, 1, 1)
    self.addLink(router2, router4, 2, 1)
    self.addLink(router3, router4, 1, 2)
    self.addLink(router3, router8, 2, 1)
    self.addLink(router3, router16, 3, 1)
    self.addLink(router4, router5, 3, 1)
    self.addLink(router4, router7, 4, 1)
    self.addLink(router5, router6, 2, 1)
    self.addLink(router7, router29, 3, 1)
    self.addLink(router8, router9, 2, 1)
    self.addLink(router8, router12, 3, 1)
    self.addLink(router9, router10, 2, 1)
    self.addLink(router10, router11, 2, 1)
    self.addLink(router11, router12, 2, 2)
    self.addLink(router12, router13, 3, 1)
    self.addLink(router12, router14, 4, 1)
    self.addLink(router12, router15, 5, 1)
    self.addLink(router12, router19, 6, 1)
    self.addLink(router15, router16, 2, 2)
    self.addLink(router16, router17, 3, 1)
    self.addLink(router16, router18, 4, 1)
    self.addLink(router6, router7, 2, 2)
    self.addLink(router18, router20, 2, 1)
    self.addLink(router19, router21, 2, 1)
    self.addLink(router20, router21, 2, 2)
    self.addLink(router21, router22, 3, 1)
    self.addLink(router21, router25, 4, 1)
    self.addLink(router22, router23, 2, 1)
    self.addLink(router22, router27, 3, 1)
    self.addLink(router23, router24, 2, 1)
    self.addLink(router24, router29, 2, 2)
    self.addLink(router25, router26, 2, 1)
    self.addLink(router26, router27, 2, 2)
    self.addLink(router27, router28, 3, 1)
    self.addLink(router27, router30, 4, 1)
    self.addLink(router28, router31, 2, 1)
    self.addLink(router29, router31, 3, 2)
    self.addLink(router30, router32, 2, 1)
    self.addLink(router31, router32, 3, 2)
    self.addLink(router32, router33, 3, 1)
    self.addLink(router32, router34, 4, 1)
    self.addLink(router33, router34, 2, 2)
    self.addLink(router34, router35, 3, 1)
    self.addLink(router34, router39, 4, 1)
    self.addLink(router34, router41, 5, 1)
    self.addLink(router35, router36, 2, 1)
    self.addLink(router36, router37, 2, 1)
    self.addLink(router37, router38, 2, 1)
    self.addLink(router39, router40, 2, 1)
    self.addLink(router40, router41, 2, 2)
    self.addLink(router40, router44, 3, 1)
    self.addLink(router41, router42, 3, 1)
    self.addLink(router41, router43, 4, 1)
    self.addLink(router42, router43, 2, 2)
    self.addLink(router43, router44, 3, 2)
    self.addLink(router43, router45, 4, 1)
    self.addLink(router44, router45, 3, 2)

    ## Enlaces CE
    self.addLink(router1, routerLan1, 2, 0)
    self.addLink(router45, routerLan2, 3, 0)
    self.addLink(h0, routerLan1, 0, 1)
    self.addLink(h1, routerLan2, 0, 1)


