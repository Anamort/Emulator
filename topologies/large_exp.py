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
    h0 = self.addHost('h0', ips=['10.0.1.2/24'], gw='10.0.1.1', cls=RAUHost)
    h1 = self.addHost('h1', ips=['10.1.1.2/24'], gw='10.1.1.1', cls=RAUHost)

    routerLan1 = self.addHost('routerLan1', ips=['10.0.0.1/24', '10.0.1.1/24'],
                                ce_mac_address='00:00:00:00:00:01',
                                gw='10.0.0.2', cls=QuaggaRouter)

    routerLan2 = self.addHost('routerLan2', ips=['10.1.0.1/24', '10.1.1.1/24'],
                                ce_mac_address='00:00:00:00:00:02',
                                gw='10.1.0.2', cls=QuaggaRouter)
    

    router1 = self.addHost('router1', ips=['192.168.1.11/24','10.10.1.1/24','10.10.2.1/24'],
    		  controller_ip="192.168.1.10",
		      cls=RAUSwitch)

    router2 = self.addHost('router2', ips=['192.168.1.12/24','10.10.1.2/24','10.10.3.1/24','10.10.4.1/24'],
	      controller_ip="192.168.1.10",
	      cls=RAUSwitch)
    

    router3 = self.addHost('router3', ips=['192.168.1.13/24','10.10.2.2/24','10.10.5.1/24','10.10.6.1/24'],
		  controller_ip="192.168.1.10",
		  cls=RAUSwitch)
    

    router4 = self.addHost('router4', ips=['192.168.1.14/24','10.10.3.2/24','10.10.7.1/24','10.10.8.1/24'],
		  controller_ip="192.168.1.10",
		  cls=RAUSwitch)

    router5 = self.addHost('router5', ips=['192.168.1.15/24','10.10.4.2/24','10.10.9.1/24','10.10.10.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router6 = self.addHost('router6', ips=['192.168.1.16/24','10.10.5.2/24','10.10.11.1/24','10.10.12.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router7 = self.addHost('router7', ips=['192.168.1.17/24','10.10.6.2/24','10.10.13.1/24','10.10.14.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router8 = self.addHost('router8', ips=['192.168.1.18/24','10.10.7.2/24','10.10.15.1/24','10.10.16.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router9 = self.addHost('router9', ips=['192.168.1.19/24','10.10.8.2/24','10.10.17.1/24','10.10.18.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router10 = self.addHost('router10', ips=['192.168.1.20/24','10.10.9.2/24','10.10.19.1/24','10.10.20.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router11 = self.addHost('router11', ips=['192.168.1.21/24','10.10.10.2/24','10.10.21.1/24','10.10.22.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router12 = self.addHost('router12', ips=['192.168.1.22/24','10.10.11.2/24','10.10.23.1/24','10.10.24.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    router13 = self.addHost('router13', ips=['192.168.1.23/24','10.10.12.2/24','10.10.25.1/24','10.10.26.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    router14 = self.addHost('router14', ips=['192.168.1.24/24','10.10.13.2/24','10.10.27.1/24','10.10.28.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    router15 = self.addHost('router15', ips=['192.168.1.25/24','10.10.14.2/24','10.10.29.1/24','10.10.30.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    router16 = self.addHost('router16', ips=['192.168.1.26/24','10.10.15.2/24','10.10.31.1/24','10.10.32.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router17 = self.addHost('router17', ips=['192.168.1.27/24','10.10.16.2/24','10.10.33.1/24','10.10.34.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router18 = self.addHost('router18', ips=['192.168.1.28/24','10.10.17.2/24','10.10.35.1/24','10.10.36.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router19 = self.addHost('router19', ips=['192.168.1.29/24','10.10.18.2/24','10.10.37.1/24','10.10.38.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router20 = self.addHost('router20', ips=['192.168.1.30/24','10.10.19.2/24','10.10.39.1/24','10.10.40.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router21 = self.addHost('router21', ips=['192.168.1.31/24','10.10.20.2/24','10.10.41.1/24','10.10.42.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router22 = self.addHost('router22', ips=['192.168.1.32/24','10.10.21.2/24','10.10.43.1/24','10.10.44.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router23 = self.addHost('router23', ips=['192.168.1.33/24','10.10.22.2/24','10.10.45.1/24','10.10.46.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    router24 = self.addHost('router24', ips=['192.168.1.34/24','10.10.23.2/24','10.10.47.1/24','10.10.48.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    router25 = self.addHost('router25', ips=['192.168.1.35/24','10.10.24.2/24','10.10.49.1/24','10.10.50.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    router26 = self.addHost('router26', ips=['192.168.1.36/24','10.10.25.2/24','10.10.51.1/24','10.10.52.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    router27 = self.addHost('router27', ips=['192.168.1.37/24','10.10.26.2/24','10.10.53.1/24','10.10.54.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router28 = self.addHost('router28', ips=['192.168.1.38/24','10.10.27.2/24','10.10.55.1/24','10.10.56.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router29 = self.addHost('router29', ips=['192.168.1.39/24','10.10.28.2/24','10.10.57.1/24','10.10.58.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router30 = self.addHost('router30', ips=['192.168.1.40/24','10.10.29.2/24','10.10.59.1/24','10.10.60.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router31 = self.addHost('router31', ips=['192.168.1.41/24','10.10.30.2/24','10.10.61.1/24','10.10.62.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router32 = self.addHost('router32', ips=['192.168.1.42/24','10.10.31.2/24','10.10.63.1/24','10.10.64.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    router33 = self.addHost('router33', ips=['192.168.1.43/24','10.10.32.2/24','10.10.65.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    router34 = self.addHost('router34', ips=['192.168.1.44/24','10.10.33.2/24','10.10.66.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    router35 = self.addHost('router35', ips=['192.168.1.45/24','10.10.34.2/24','10.10.67.1/24','10.10.68.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    router36 = self.addHost('router36', ips=['192.168.2.11/24','10.10.35.2/24','10.10.69.1/24','10.10.70.1/24'],
              controller_ip="192.168.2.10",
              cls=RAUSwitch)
    

    router37 = self.addHost('router37', ips=['192.168.2.12/24','10.10.36.2/24','10.10.71.1/24'],
              controller_ip="192.168.2.10",
              cls=RAUSwitch)

    router38 = self.addHost('router38', ips=['192.168.2.13/24','10.10.37.2/24','10.10.72.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)

    router39 = self.addHost('router39', ips=['192.168.2.14/24','10.10.38.2/24','10.10.73.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)
    

    router40 = self.addHost('router40', ips=['192.168.2.15/24','10.10.39.2/24','10.10.74.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)
    

    router41 = self.addHost('router41', ips=['192.168.2.16/24','10.10.40.2/24','10.10.75.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)

    router42 = self.addHost('router42', ips=['192.168.2.17/24','10.10.41.2/24','10.10.76.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)

    router43 = self.addHost('router43', ips=['192.168.2.18/24','10.10.42.2/24','10.10.77.1/24','10.10.78.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)
    

    router44 = self.addHost('router44', ips=['192.168.2.19/24','10.10.43.2/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)

    router45 = self.addHost('router45', ips=['192.168.2.20/24','10.10.44.2/24','10.10.79.1/24','10.10.80.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)

    router46 = self.addHost('router46', ips=['192.168.2.21/24','10.10.45.2/24','10.10.81.1/24'],
          controller_ip="192.168.2.10",
          cls=RAUSwitch)

    router47 = self.addHost('router47', ips=['192.168.2.22/24','10.10.46.2/24','10.10.82.1/24'],
          controller_ip="192.168.2.10",
          cls=RAUSwitch)
    

    router48 = self.addHost('router48', ips=['192.168.2.23/24','10.10.47.2/24','10.10.83.1/24'],
          controller_ip="192.168.2.10",
          cls=RAUSwitch)
    

    router49 = self.addHost('router49', ips=['192.168.2.24/24','10.10.48.2/24'],
          controller_ip="192.168.2.10",
          cls=RAUSwitch)

    router50 = self.addHost('router50', ips=['192.168.2.25/24','10.10.49.2/24','10.10.84.1/24','10.10.85.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)

    router51 = self.addHost('router51', ips=['192.168.2.26/24','10.10.50.2/24','10.10.86.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)
    

    router52 = self.addHost('router52', ips=['192.168.2.27/24','10.10.51.2/24','10.10.87.1/24','10.10.88.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)
    

    router53 = self.addHost('router53', ips=['192.168.2.28/24','10.10.52.2/24','10.10.89.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)

    router54 = self.addHost('router54', ips=['192.168.2.29/24','10.10.53.2/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)

    router55 = self.addHost('router55', ips=['192.168.2.30/24','10.10.54.2/24','10.10.90.1/24','10.10.91.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)
    

    router56 = self.addHost('router56', ips=['192.168.2.31/24','10.10.55.2/24','10.10.92.1/24','10.10.93.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)

    router57 = self.addHost('router57', ips=['192.168.2.32/24','10.10.56.2/24','10.10.94.1/24'],
              controller_ip="192.168.2.10",
              cls=RAUSwitch)

    router58 = self.addHost('router58', ips=['192.168.2.33/24','10.10.57.2/24','10.10.95.1/24','10.10.96.1/24'],
          controller_ip="192.168.2.10",
          cls=RAUSwitch)
    

    router59 = self.addHost('router59', ips=['192.168.2.34/24','10.10.58.2/24'],
              controller_ip="192.168.2.10",
              cls=RAUSwitch)
    

    router60 = self.addHost('router60', ips=['192.168.2.35/24','10.10.59.2/24','10.10.97.1/24','10.10.98.1/24'],
              controller_ip="192.168.2.10",
              cls=RAUSwitch)

    router61 = self.addHost('router61', ips=['192.168.2.36/24','10.10.60.2/24','10.10.99.1/24','10.10.100.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)

    router62 = self.addHost('router62', ips=['192.168.2.37/24','10.10.61.2/24','10.10.101.1/24','10.10.102.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)
    

    router63 = self.addHost('router63', ips=['192.168.2.38/24','10.10.62.2/24','10.10.103.1/24','10.10.104.1/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)
    

    router64 = self.addHost('router64', ips=['192.168.2.39/24','10.10.63.2/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)

    router65 = self.addHost('router65', ips=['192.168.2.40/24','10.10.64.2/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)

    router66 = self.addHost('router66', ips=['192.168.2.41/24','10.10.65.2/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)
    

    router67 = self.addHost('router67', ips=['192.168.2.42/24','10.10.66.2/24'],
        controller_ip="192.168.2.10",
        cls=RAUSwitch)

    router68 = self.addHost('router68', ips=['192.168.2.43/24','10.10.67.2/24'],
              controller_ip="192.168.2.10",
              cls=RAUSwitch)

    router69 = self.addHost('router69', ips=['192.168.2.44/24','10.10.68.2/24'],
          controller_ip="192.168.2.10",
          cls=RAUSwitch)
    

    router70 = self.addHost('router70', ips=['192.168.2.45/24','10.10.69.2/24'],
              controller_ip="192.168.2.10",
              cls=RAUSwitch)
    

    router71 = self.addHost('router71', ips=['192.168.3.11/24','10.10.70.2/24'],
              controller_ip="192.168.3.10",
              cls=RAUSwitch)

    router72 = self.addHost('router72', ips=['192.168.3.12/24','10.10.71.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router73 = self.addHost('router73', ips=['192.168.3.13/24','10.10.72.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)
    

    router74 = self.addHost('router74', ips=['192.168.3.14/24','10.10.73.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)
    

    router75 = self.addHost('router75', ips=['192.168.3.15/24','10.10.74.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router76 = self.addHost('router76', ips=['192.168.3.16/24','10.10.75.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router77 = self.addHost('router77', ips=['192.168.3.17/24','10.10.76.2/24','10.0.0.2/24'],
        controller_ip="192.168.3.10",
        border=1, ce_ip_address='10.0.0.1', ce_mac_address='00:00:00:00:00:01',
        cls=RAUSwitch)
    

    router78 = self.addHost('router78', ips=['192.168.3.18/24','10.10.77.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router79 = self.addHost('router79', ips=['192.168.3.19/24','10.10.78.2/24'],
              controller_ip="192.168.3.10",
              cls=RAUSwitch)

    router80 = self.addHost('router80', ips=['192.168.3.20/24','10.10.79.2/24'],
          controller_ip="192.168.3.10",
          cls=RAUSwitch)
    

    router81 = self.addHost('router81', ips=['192.168.3.21/24','10.10.80.2/24'],
              controller_ip="192.168.3.10",
              cls=RAUSwitch)
    

    router82 = self.addHost('router82', ips=['192.168.3.22/24','10.10.81.2/24'],
              controller_ip="192.168.3.10",
              cls=RAUSwitch)

    router83 = self.addHost('router83', ips=['192.168.3.23/24','10.10.82.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router84 = self.addHost('router84', ips=['192.168.3.24/24','10.10.83.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)
    

    router85 = self.addHost('router85', ips=['192.168.3.25/24','10.10.84.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)
    

    router86 = self.addHost('router86', ips=['192.168.3.26/24','10.10.85.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router87 = self.addHost('router87', ips=['192.168.3.27/24','10.10.86.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router88 = self.addHost('router88', ips=['192.168.3.28/24','10.10.87.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)
    

    router89 = self.addHost('router89', ips=['192.168.3.29/24','10.10.88.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router90 = self.addHost('router90', ips=['192.168.3.30/24','10.10.89.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router91 = self.addHost('router91', ips=['192.168.3.31/24','10.10.90.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router92 = self.addHost('router92', ips=['192.168.3.32/24','10.10.91.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router93 = self.addHost('router93', ips=['192.168.3.33/24','10.10.92.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router94 = self.addHost('router94', ips=['192.168.3.34/24','10.10.93.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router95 = self.addHost('router95', ips=['192.168.3.35/24','10.10.94.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router96 = self.addHost('router96', ips=['192.168.3.36/24','10.10.95.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router97 = self.addHost('router97', ips=['192.168.3.37/24','10.10.96.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router98 = self.addHost('router98', ips=['192.168.3.38/24','10.10.97.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router99 = self.addHost('router99', ips=['192.168.3.39/24','10.10.98.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router100 = self.addHost('router100', ips=['192.168.3.40/24','10.10.99.2/24','10.1.0.2/24'],
        controller_ip="192.168.3.10",
        border=1, ce_ip_address='10.1.0.1', ce_mac_address='00:00:00:00:00:02',
        cls=RAUSwitch)

    router101 = self.addHost('router101', ips=['192.168.3.41/24','10.10.100.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router102 = self.addHost('router102', ips=['192.168.3.42/24','10.10.101.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router103 = self.addHost('router103', ips=['192.168.3.43/24','10.10.102.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router104 = self.addHost('router104', ips=['192.168.3.44/24','10.10.103.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)

    router105 = self.addHost('router105', ips=['192.168.3.45/24','10.10.104.2/24'],
        controller_ip="192.168.3.10",
        cls=RAUSwitch)
    

    # Controlador
    root = self.addHost('controller', cls=RAUController, ips=['192.168.1.10/24','192.168.2.10/24','192.168.3.10/24'])
    
    # Switch de la red de gestion
    man_switch1 = self.addSwitch('s1', protocols='OpenFlow13', failMode='standalone')
    man_switch2 = self.addSwitch('s2', protocols='OpenFlow13', failMode='standalone')
    man_switch3 = self.addSwitch('s3', protocols='OpenFlow13', failMode='standalone')

    # Enlaces
    self.addLink(man_switch1, router1, 2, 0)
    self.addLink(man_switch1, router2, 3, 0)
    self.addLink(man_switch1, router3, 4, 0)
    self.addLink(man_switch1, router4, 5, 0)
    self.addLink(man_switch1, router5, 6, 0)
    self.addLink(man_switch1, router6, 7, 0)
    self.addLink(man_switch1, router7, 8, 0)
    self.addLink(man_switch1, router8, 9, 0)
    self.addLink(man_switch1, router9, 10, 0)
    self.addLink(man_switch1, router10, 11, 0)
    self.addLink(man_switch1, router11, 12, 0)
    self.addLink(man_switch1, router12, 13, 0)
    self.addLink(man_switch1, router13, 14, 0)
    self.addLink(man_switch1, router14, 15, 0)
    self.addLink(man_switch1, router15, 16, 0)
    self.addLink(man_switch1, router16, 17, 0)
    self.addLink(man_switch1, router17, 18, 0)
    self.addLink(man_switch1, router18, 19, 0)
    self.addLink(man_switch1, router19, 20, 0)
    self.addLink(man_switch1, router20, 21, 0)
    self.addLink(man_switch1, router21, 22, 0)
    self.addLink(man_switch1, router22, 23, 0)
    self.addLink(man_switch1, router23, 24, 0)
    self.addLink(man_switch1, router24, 25, 0)
    self.addLink(man_switch1, router25, 26, 0)
    self.addLink(man_switch1, router26, 27, 0)
    self.addLink(man_switch1, router27, 28, 0)
    self.addLink(man_switch1, router28, 29, 0)
    self.addLink(man_switch1, router29, 30, 0)
    self.addLink(man_switch1, router30, 31, 0)
    self.addLink(man_switch1, router31, 32, 0)
    self.addLink(man_switch1, router32, 33, 0)
    self.addLink(man_switch1, router33, 34, 0)
    self.addLink(man_switch1, router34, 35, 0)
    self.addLink(man_switch1, router35, 36, 0)
    self.addLink(man_switch2, router36, 2, 0)
    self.addLink(man_switch2, router37, 3, 0)
    self.addLink(man_switch2, router38, 4, 0)
    self.addLink(man_switch2, router39, 5, 0)
    self.addLink(man_switch2, router40, 6, 0)
    self.addLink(man_switch2, router41, 7, 0)
    self.addLink(man_switch2, router42, 8, 0)
    self.addLink(man_switch2, router43, 9, 0)
    self.addLink(man_switch2, router44, 10, 0)
    self.addLink(man_switch2, router45, 11, 0)
    self.addLink(man_switch2, router46, 12, 0)
    self.addLink(man_switch2, router47, 13, 0)
    self.addLink(man_switch2, router48, 14, 0)
    self.addLink(man_switch2, router49, 15, 0)
    self.addLink(man_switch2, router50, 16, 0)
    self.addLink(man_switch2, router51, 17, 0)
    self.addLink(man_switch2, router52, 18, 0)
    self.addLink(man_switch2, router53, 19, 0)
    self.addLink(man_switch2, router54, 20, 0)
    self.addLink(man_switch2, router55, 21, 0)
    self.addLink(man_switch2, router56, 22, 0)
    self.addLink(man_switch2, router57, 23, 0)
    self.addLink(man_switch2, router58, 24, 0)
    self.addLink(man_switch2, router59, 25, 0)
    self.addLink(man_switch2, router60, 26, 0)
    self.addLink(man_switch2, router61, 27, 0)
    self.addLink(man_switch2, router62, 28, 0)
    self.addLink(man_switch2, router63, 29, 0)
    self.addLink(man_switch2, router64, 30, 0)
    self.addLink(man_switch2, router65, 31, 0)
    self.addLink(man_switch2, router66, 32, 0)
    self.addLink(man_switch2, router67, 33, 0)
    self.addLink(man_switch2, router68, 34, 0)
    self.addLink(man_switch2, router69, 35, 0)
    self.addLink(man_switch2, router70, 36, 0)
    self.addLink(man_switch3, router71, 2, 0)
    self.addLink(man_switch3, router72, 3, 0)
    self.addLink(man_switch3, router73, 4, 0)
    self.addLink(man_switch3, router74, 5, 0)
    self.addLink(man_switch3, router75, 6, 0)
    self.addLink(man_switch3, router76, 7, 0)
    self.addLink(man_switch3, router77, 8, 0)
    self.addLink(man_switch3, router78, 9, 0)
    self.addLink(man_switch3, router79, 10, 0)
    self.addLink(man_switch3, router80, 11, 0)
    self.addLink(man_switch3, router81, 12, 0)
    self.addLink(man_switch3, router82, 13, 0)
    self.addLink(man_switch3, router83, 14, 0)
    self.addLink(man_switch3, router84, 15, 0)
    self.addLink(man_switch3, router85, 16, 0)
    self.addLink(man_switch3, router86, 17, 0)
    self.addLink(man_switch3, router87, 18, 0)
    self.addLink(man_switch3, router88, 19, 0)
    self.addLink(man_switch3, router89, 20, 0)
    self.addLink(man_switch3, router90, 21, 0)
    self.addLink(man_switch3, router91, 22, 0)
    self.addLink(man_switch3, router92, 23, 0)
    self.addLink(man_switch3, router93, 24, 0)
    self.addLink(man_switch3, router94, 25, 0)
    self.addLink(man_switch3, router95, 26, 0)
    self.addLink(man_switch3, router96, 27, 0)
    self.addLink(man_switch3, router97, 28, 0)
    self.addLink(man_switch3, router98, 29, 0)
    self.addLink(man_switch3, router99, 30, 0)
    self.addLink(man_switch3, router100, 31, 0)
    self.addLink(man_switch3, router101, 32, 0)
    self.addLink(man_switch3, router102, 33, 0)
    self.addLink(man_switch3, router103, 34, 0)
    self.addLink(man_switch3, router104, 35, 0)
    self.addLink(man_switch3, router105, 36, 0)
    self.addLink(man_switch1, root, 1, 0)
    self.addLink(man_switch2, root, 1, 1)
    self.addLink(man_switch3, root, 1, 2)
    
    self.addLink(router1, router2, 1, 1)
    self.addLink(router1, router3, 2, 1)
    self.addLink(router2, router4, 2, 1)
    self.addLink(router2, router5, 3, 1)
    self.addLink(router3, router6, 2, 1)
    self.addLink(router3, router7, 3, 1)
    self.addLink(router4, router8, 2, 1)
    self.addLink(router4, router9, 3, 1)
    self.addLink(router5, router10, 2, 1)
    self.addLink(router5, router11, 3, 1)
    self.addLink(router6, router12, 2, 1)
    self.addLink(router6, router13, 3, 1)
    self.addLink(router7, router14, 2, 1)
    self.addLink(router7, router15, 3, 1)
    self.addLink(router8, router16, 2, 1)
    self.addLink(router8, router17, 3, 1)
    self.addLink(router9, router18, 2, 1)
    self.addLink(router9, router19, 3, 1)
    self.addLink(router10, router20, 2, 1)
    self.addLink(router10, router21, 3, 1)
    self.addLink(router11, router22, 2, 1)
    self.addLink(router11, router23, 3, 1)
    self.addLink(router12, router24, 2, 1)
    self.addLink(router12, router25, 3, 1)
    self.addLink(router13, router26, 2, 1)
    self.addLink(router13, router27, 3, 1)
    self.addLink(router14, router28, 2, 1)
    self.addLink(router14, router29, 3, 1)
    self.addLink(router15, router30, 2, 1)
    self.addLink(router15, router31, 3, 1)
    self.addLink(router16, router32, 2, 1)
    self.addLink(router16, router33, 3, 1)
    self.addLink(router17, router34, 2, 1)
    self.addLink(router17, router35, 3, 1)
    self.addLink(router18, router36, 2, 1)
    self.addLink(router18, router37, 3, 1)
    self.addLink(router19, router38, 2, 1)
    self.addLink(router19, router39, 3, 1)
    self.addLink(router20, router40, 2, 1)
    self.addLink(router20, router41, 3, 1)
    self.addLink(router21, router42, 2, 1)
    self.addLink(router21, router43, 3, 1)
    self.addLink(router22, router44, 2, 1)
    self.addLink(router22, router45, 3, 1)
    self.addLink(router23, router46, 2, 1)
    self.addLink(router23, router47, 3, 1)
    self.addLink(router24, router48, 2, 1)
    self.addLink(router24, router49, 3, 1)
    self.addLink(router25, router50, 2, 1)
    self.addLink(router25, router51, 3, 1)
    self.addLink(router26, router52, 2, 1)
    self.addLink(router26, router53, 3, 1)
    self.addLink(router27, router54, 2, 1)
    self.addLink(router27, router55, 3, 1)
    self.addLink(router28, router56, 2, 1)
    self.addLink(router28, router57, 3, 1)
    self.addLink(router29, router58, 2, 1)
    self.addLink(router29, router59, 3, 1)
    self.addLink(router30, router60, 2, 1)
    self.addLink(router30, router61, 3, 1)
    self.addLink(router31, router62, 2, 1)
    self.addLink(router31, router63, 3, 1)
    self.addLink(router32, router64, 2, 1)
    self.addLink(router32, router65, 3, 1)
    self.addLink(router33, router66, 2, 1)
    self.addLink(router34, router67, 2, 1)
    self.addLink(router35, router68, 2, 1)
    self.addLink(router35, router69, 3, 1)
    self.addLink(router36, router70, 2, 1)
    self.addLink(router36, router71, 3, 1)
    self.addLink(router37, router72, 2, 1)
    self.addLink(router38, router73, 2, 1)
    self.addLink(router39, router74, 2, 1)
    self.addLink(router40, router75, 2, 1)
    self.addLink(router41, router76, 2, 1)
    self.addLink(router42, router77, 2, 1)
    self.addLink(router43, router78, 2, 1)
    self.addLink(router43, router79, 3, 1)
    self.addLink(router45, router80, 2, 1)
    self.addLink(router45, router81, 3, 1)
    self.addLink(router46, router82, 2, 1)
    self.addLink(router47, router83, 2, 1)
    self.addLink(router48, router84, 2, 1)
    self.addLink(router50, router85, 2, 1)
    self.addLink(router50, router86, 3, 1)
    self.addLink(router51, router87, 2, 1)
    self.addLink(router52, router88, 2, 1)
    self.addLink(router52, router89, 3, 1)
    self.addLink(router53, router90, 2, 1)
    self.addLink(router55, router91, 2, 1)
    self.addLink(router55, router92, 3, 1)
    self.addLink(router56, router93, 2, 1)
    self.addLink(router56, router94, 3, 1)
    self.addLink(router57, router95, 2, 1)
    self.addLink(router58, router96, 2, 1)
    self.addLink(router58, router97, 3, 1)
    self.addLink(router60, router98, 2, 1)
    self.addLink(router60, router99, 3, 1)
    self.addLink(router61, router100, 2, 1)
    self.addLink(router61, router101, 3, 1)
    self.addLink(router62, router102, 2, 1)
    self.addLink(router62, router103, 3, 1)
    self.addLink(router63, router104, 2, 1)
    self.addLink(router63, router105, 3, 1)

    ## Enlaces CE
    self.addLink(router77, routerLan1, 2, 0)
    self.addLink(router100, routerLan2, 2, 0)
    self.addLink(h0, routerLan1, 0, 1)
    self.addLink(h1, routerLan2, 0, 1)


