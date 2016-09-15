"""
Topologia de ejemplo
Fuente: http://www.topology-zoo.org/maps/Bellcanada.jpg
45 RAUSwitch
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
    

    switch1 = self.addHost('switch1', ips=['192.168.1.11/24','10.10.1.1/24','10.10.2.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)

    switch2 = self.addHost('switch2', ips=['192.168.1.12/24','10.10.1.2/24','10.10.3.1/24','10.10.4.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch3 = self.addHost('switch3', ips=['192.168.1.13/24','10.10.2.2/24','10.10.5.1/24','10.10.6.1/24'],
      controller_ip="192.168.1.10",
      cls=RAUSwitch)
    

    switch4 = self.addHost('switch4', ips=['192.168.1.14/24','10.10.3.2/24','10.10.7.1/24','10.10.8.1/24'],
      controller_ip="192.168.1.10",
      cls=RAUSwitch)

    switch5 = self.addHost('switch5', ips=['192.168.1.15/24','10.10.4.2/24','10.10.9.1/24','10.10.10.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch6 = self.addHost('switch6', ips=['192.168.1.16/24','10.10.5.2/24','10.10.11.1/24','10.10.12.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch7 = self.addHost('switch7', ips=['192.168.1.17/24','10.10.6.2/24','10.10.13.1/24','10.10.14.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch8 = self.addHost('switch8', ips=['192.168.1.18/24','10.10.7.2/24','10.10.15.1/24','10.10.16.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch9 = self.addHost('switch9', ips=['192.168.1.19/24','10.10.8.2/24','10.10.17.1/24','10.10.18.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch10 = self.addHost('switch10', ips=['192.168.1.20/24','10.10.9.2/24','10.10.19.1/24','10.10.20.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch11 = self.addHost('switch11', ips=['192.168.1.21/24','10.10.10.2/24','10.10.21.1/24','10.10.22.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch12 = self.addHost('switch12', ips=['192.168.1.22/24','10.10.11.2/24','10.10.23.1/24','10.10.24.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch13 = self.addHost('switch13', ips=['192.168.1.23/24','10.10.12.2/24','10.10.25.1/24','10.10.26.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    switch14 = self.addHost('switch14', ips=['192.168.1.24/24','10.10.13.2/24','10.10.27.1/24','10.10.28.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    switch15 = self.addHost('switch15', ips=['192.168.1.25/24','10.10.14.2/24','10.10.29.1/24','10.10.30.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch16 = self.addHost('switch16', ips=['192.168.1.26/24','10.10.15.2/24','10.10.31.1/24','10.10.32.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch17 = self.addHost('switch17', ips=['192.168.1.27/24','10.10.16.2/24','10.10.33.1/24','10.10.34.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch18 = self.addHost('switch18', ips=['192.168.1.28/24','10.10.17.2/24','10.10.35.1/24','10.10.36.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch19 = self.addHost('switch19', ips=['192.168.1.29/24','10.10.18.2/24','10.10.37.1/24','10.10.38.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch20 = self.addHost('switch20', ips=['192.168.1.30/24','10.10.19.2/24','10.10.39.1/24','10.10.40.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch21 = self.addHost('switch21', ips=['192.168.1.31/24','10.10.20.2/24','10.10.41.1/24','10.10.42.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch22 = self.addHost('switch22', ips=['192.168.1.32/24','10.10.21.2/24','10.10.43.1/24','10.10.44.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch23 = self.addHost('switch23', ips=['192.168.1.33/24','10.10.22.2/24','10.10.45.1/24','10.10.46.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch24 = self.addHost('switch24', ips=['192.168.1.34/24','10.10.23.2/24','10.10.47.1/24','10.10.48.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    switch25 = self.addHost('switch25', ips=['192.168.1.35/24','10.10.24.2/24','10.10.49.1/24','10.10.50.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    switch26 = self.addHost('switch26', ips=['192.168.1.36/24','10.10.25.2/24','10.10.51.1/24','10.10.52.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch27 = self.addHost('switch27', ips=['192.168.1.37/24','10.10.26.2/24','10.10.53.1/24','10.10.54.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch28 = self.addHost('switch28', ips=['192.168.1.38/24','10.10.27.2/24','10.10.55.1/24','10.10.56.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch29 = self.addHost('switch29', ips=['192.168.1.39/24','10.10.28.2/24','10.10.57.1/24','10.10.58.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch30 = self.addHost('switch30', ips=['192.168.1.40/24','10.10.29.2/24','10.10.59.1/24','10.10.60.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch31 = self.addHost('switch31', ips=['192.168.1.41/24','10.10.30.2/24','10.10.61.1/24','10.10.62.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch32 = self.addHost('switch32', ips=['192.168.1.42/24','10.10.31.2/24','10.10.63.1/24','10.10.64.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch33 = self.addHost('switch33', ips=['192.168.1.43/24','10.10.32.2/24','10.10.65.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch34 = self.addHost('switch34', ips=['192.168.1.44/24','10.10.33.2/24','10.10.66.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch35 = self.addHost('switch35', ips=['192.168.1.45/24','10.10.34.2/24','10.10.67.1/24','10.10.68.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    switch36 = self.addHost('switch36', ips=['192.168.1.46/24','10.10.35.2/24','10.10.69.1/24','10.10.70.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    switch37 = self.addHost('switch37', ips=['192.168.1.47/24','10.10.36.2/24','10.10.71.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch38 = self.addHost('switch38', ips=['192.168.1.48/24','10.10.37.2/24','10.10.72.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch39 = self.addHost('switch39', ips=['192.168.1.49/24','10.10.38.2/24','10.10.73.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch40 = self.addHost('switch40', ips=['192.168.1.50/24','10.10.39.2/24','10.10.74.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch41 = self.addHost('switch41', ips=['192.168.1.51/24','10.10.40.2/24','10.10.75.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch42 = self.addHost('switch42', ips=['192.168.1.52/24','10.10.41.2/24','10.10.76.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch43 = self.addHost('switch43', ips=['192.168.1.53/24','10.10.42.2/24','10.10.77.1/24','10.10.78.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch44 = self.addHost('switch44', ips=['192.168.1.54/24','10.10.43.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch45 = self.addHost('switch45', ips=['192.168.1.55/24','10.10.44.2/24','10.10.79.1/24','10.10.80.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch46 = self.addHost('switch46', ips=['192.168.1.56/24','10.10.45.2/24','10.10.81.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)

    switch47 = self.addHost('switch47', ips=['192.168.1.57/24','10.10.46.2/24','10.10.82.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    switch48 = self.addHost('switch48', ips=['192.168.1.58/24','10.10.47.2/24','10.10.83.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    switch49 = self.addHost('switch49', ips=['192.168.1.59/24','10.10.48.2/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)

    switch50 = self.addHost('switch50', ips=['192.168.1.60/24','10.10.49.2/24','10.10.84.1/24','10.10.85.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch51 = self.addHost('switch51', ips=['192.168.1.61/24','10.10.50.2/24','10.10.86.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch52 = self.addHost('switch52', ips=['192.168.1.62/24','10.10.51.2/24','10.10.87.1/24','10.10.88.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch53 = self.addHost('switch53', ips=['192.168.1.63/24','10.10.52.2/24','10.10.89.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch54 = self.addHost('switch54', ips=['192.168.1.64/24','10.10.53.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch55 = self.addHost('switch55', ips=['192.168.1.65/24','10.10.54.2/24','10.10.90.1/24','10.10.91.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch56 = self.addHost('switch56', ips=['192.168.1.66/24','10.10.55.2/24','10.10.92.1/24','10.10.93.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch57 = self.addHost('switch57', ips=['192.168.1.67/24','10.10.56.2/24','10.10.94.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch58 = self.addHost('switch58', ips=['192.168.1.68/24','10.10.57.2/24','10.10.95.1/24','10.10.96.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    switch59 = self.addHost('switch59', ips=['192.168.1.69/24','10.10.58.2/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    switch60 = self.addHost('switch60', ips=['192.168.1.70/24','10.10.59.2/24','10.10.97.1/24','10.10.98.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch61 = self.addHost('switch61', ips=['192.168.1.71/24','10.10.60.2/24','10.10.99.1/24','10.10.100.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch62 = self.addHost('switch62', ips=['192.168.1.72/24','10.10.61.2/24','10.10.101.1/24','10.10.102.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch63 = self.addHost('switch63', ips=['192.168.1.73/24','10.10.62.2/24','10.10.103.1/24','10.10.104.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch64 = self.addHost('switch64', ips=['192.168.1.74/24','10.10.63.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch65 = self.addHost('switch65', ips=['192.168.1.75/24','10.10.64.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch66 = self.addHost('switch66', ips=['192.168.1.76/24','10.10.65.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch67 = self.addHost('switch67', ips=['192.168.1.77/24','10.10.66.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch68 = self.addHost('switch68', ips=['192.168.1.78/24','10.10.67.2/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch69 = self.addHost('switch69', ips=['192.168.1.79/24','10.10.68.2/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    switch70 = self.addHost('switch70', ips=['192.168.1.80/24','10.10.69.2/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    switch71 = self.addHost('switch71', ips=['192.168.1.81/24','10.10.70.2/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch72 = self.addHost('switch72', ips=['192.168.1.82/24','10.10.71.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch73 = self.addHost('switch73', ips=['192.168.1.83/24','10.10.72.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch74 = self.addHost('switch74', ips=['192.168.1.84/24','10.10.73.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch75 = self.addHost('switch75', ips=['192.168.1.85/24','10.10.74.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch76 = self.addHost('switch76', ips=['192.168.1.86/24','10.10.75.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch77 = self.addHost('switch77', ips=['192.168.1.87/24','10.10.76.2/24','10.0.0.2/24'],
        controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.0.0.1', ce_mac_address='00:00:00:00:00:01',
        cls=RAUSwitch)
    

    switch78 = self.addHost('switch78', ips=['192.168.1.88/24','10.10.77.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch79 = self.addHost('switch79', ips=['192.168.1.89/24','10.10.78.2/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch80 = self.addHost('switch80', ips=['192.168.1.90/24','10.10.79.2/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    switch81 = self.addHost('switch81', ips=['192.168.1.91/24','10.10.80.2/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    switch82 = self.addHost('switch82', ips=['192.168.1.92/24','10.10.81.2/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch83 = self.addHost('switch83', ips=['192.168.1.93/24','10.10.82.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch84 = self.addHost('switch84', ips=['192.168.1.94/24','10.10.83.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch85 = self.addHost('switch85', ips=['192.168.1.95/24','10.10.84.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch86 = self.addHost('switch86', ips=['192.168.1.96/24','10.10.85.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch87 = self.addHost('switch87', ips=['192.168.1.97/24','10.10.86.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch88 = self.addHost('switch88', ips=['192.168.1.98/24','10.10.87.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch89 = self.addHost('switch89', ips=['192.168.1.99/24','10.10.88.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch90 = self.addHost('switch90', ips=['192.168.1.100/24','10.10.89.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch91 = self.addHost('switch91', ips=['192.168.1.101/24','10.10.90.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch92 = self.addHost('switch92', ips=['192.168.1.102/24','10.10.91.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch93 = self.addHost('switch93', ips=['192.168.1.103/24','10.10.92.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch94 = self.addHost('switch94', ips=['192.168.1.104/24','10.10.93.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch95 = self.addHost('switch95', ips=['192.168.1.105/24','10.10.94.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch96 = self.addHost('switch96', ips=['192.168.1.106/24','10.10.95.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch97 = self.addHost('switch97', ips=['192.168.1.107/24','10.10.96.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch98 = self.addHost('switch98', ips=['192.168.1.108/24','10.10.97.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch99 = self.addHost('switch99', ips=['192.168.1.109/24','10.10.98.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch100 = self.addHost('switch100', ips=['192.168.1.110/24','10.10.99.2/24','10.1.0.2/24'],
        controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.1.0.1', ce_mac_address='00:00:00:00:00:02',
        cls=RAUSwitch)

    switch101 = self.addHost('switch101', ips=['192.168.1.111/24','10.10.100.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch102 = self.addHost('switch102', ips=['192.168.1.112/24','10.10.101.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch103 = self.addHost('switch103', ips=['192.168.1.113/24','10.10.102.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch104 = self.addHost('switch104', ips=['192.168.1.114/24','10.10.103.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch105 = self.addHost('switch105', ips=['192.168.1.115/24','10.10.104.2/24'],
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
    self.addLink(man_switch, switch12, 13, 0)
    self.addLink(man_switch, switch13, 14, 0)
    self.addLink(man_switch, switch14, 15, 0)
    self.addLink(man_switch, switch15, 16, 0)
    self.addLink(man_switch, switch16, 17, 0)
    self.addLink(man_switch, switch17, 18, 0)
    self.addLink(man_switch, switch18, 19, 0)
    self.addLink(man_switch, switch19, 20, 0)
    self.addLink(man_switch, switch20, 21, 0)
    self.addLink(man_switch, switch21, 22, 0)
    self.addLink(man_switch, switch22, 23, 0)
    self.addLink(man_switch, switch23, 24, 0)
    self.addLink(man_switch, switch24, 25, 0)
    self.addLink(man_switch, switch25, 26, 0)
    self.addLink(man_switch, switch26, 27, 0)
    self.addLink(man_switch, switch27, 28, 0)
    self.addLink(man_switch, switch28, 29, 0)
    self.addLink(man_switch, switch29, 30, 0)
    self.addLink(man_switch, switch30, 31, 0)
    self.addLink(man_switch, switch31, 32, 0)
    self.addLink(man_switch, switch32, 33, 0)
    self.addLink(man_switch, switch33, 34, 0)
    self.addLink(man_switch, switch34, 35, 0)
    self.addLink(man_switch, switch35, 36, 0)
    self.addLink(man_switch, switch36, 37, 0)
    self.addLink(man_switch, switch37, 38, 0)
    self.addLink(man_switch, switch38, 39, 0)
    self.addLink(man_switch, switch39, 40, 0)
    self.addLink(man_switch, switch40, 41, 0)
    self.addLink(man_switch, switch41, 42, 0)
    self.addLink(man_switch, switch42, 43, 0)
    self.addLink(man_switch, switch43, 44, 0)
    self.addLink(man_switch, switch44, 45, 0)
    self.addLink(man_switch, switch45, 46, 0)
    self.addLink(man_switch, switch46, 47, 0)
    self.addLink(man_switch, switch47, 48, 0)
    self.addLink(man_switch, switch48, 49, 0)
    self.addLink(man_switch, switch49, 50, 0)
    self.addLink(man_switch, switch50, 51, 0)
    self.addLink(man_switch, switch51, 52, 0)
    self.addLink(man_switch, switch52, 53, 0)
    self.addLink(man_switch, switch53, 54, 0)
    self.addLink(man_switch, switch54, 55, 0)
    self.addLink(man_switch, switch55, 56, 0)
    self.addLink(man_switch, switch56, 57, 0)
    self.addLink(man_switch, switch57, 58, 0)
    self.addLink(man_switch, switch58, 59, 0)
    self.addLink(man_switch, switch59, 60, 0)
    self.addLink(man_switch, switch60, 61, 0)
    self.addLink(man_switch, switch61, 62, 0)
    self.addLink(man_switch, switch62, 63, 0)
    self.addLink(man_switch, switch63, 64, 0)
    self.addLink(man_switch, switch64, 65, 0)
    self.addLink(man_switch, switch65, 66, 0)
    self.addLink(man_switch, switch66, 67, 0)
    self.addLink(man_switch, switch67, 68, 0)
    self.addLink(man_switch, switch68, 69, 0)
    self.addLink(man_switch, switch69, 70, 0)
    self.addLink(man_switch, switch70, 71, 0)
    self.addLink(man_switch, switch71, 72, 0)
    self.addLink(man_switch, switch72, 73, 0)
    self.addLink(man_switch, switch73, 74, 0)
    self.addLink(man_switch, switch74, 75, 0)
    self.addLink(man_switch, switch75, 76, 0)
    self.addLink(man_switch, switch76, 77, 0)
    self.addLink(man_switch, switch77, 78, 0)
    self.addLink(man_switch, switch78, 79, 0)
    self.addLink(man_switch, switch79, 80, 0)
    self.addLink(man_switch, switch80, 81, 0)
    self.addLink(man_switch, switch81, 82, 0)
    self.addLink(man_switch, switch82, 83, 0)
    self.addLink(man_switch, switch83, 84, 0)
    self.addLink(man_switch, switch84, 85, 0)
    self.addLink(man_switch, switch85, 86, 0)
    self.addLink(man_switch, switch86, 87, 0)
    self.addLink(man_switch, switch87, 88, 0)
    self.addLink(man_switch, switch88, 89, 0)
    self.addLink(man_switch, switch89, 90, 0)
    self.addLink(man_switch, switch90, 91, 0)
    self.addLink(man_switch, switch91, 92, 0)
    self.addLink(man_switch, switch92, 93, 0)
    self.addLink(man_switch, switch93, 94, 0)
    self.addLink(man_switch, switch94, 95, 0)
    self.addLink(man_switch, switch95, 96, 0)
    self.addLink(man_switch, switch96, 97, 0)
    self.addLink(man_switch, switch97, 98, 0)
    self.addLink(man_switch, switch98, 99, 0)
    self.addLink(man_switch, switch99, 100, 0)
    self.addLink(man_switch, switch100, 101, 0)
    self.addLink(man_switch, switch101, 102, 0)
    self.addLink(man_switch, switch102, 103, 0)
    self.addLink(man_switch, switch103, 104, 0)
    self.addLink(man_switch, switch104, 105, 0)
    self.addLink(man_switch, switch105, 106, 0)
    self.addLink(man_switch, controller, 1, 0)
    
    self.addLink(switch1, switch2, 1, 1)
    self.addLink(switch1, switch3, 2, 1)
    self.addLink(switch2, switch4, 2, 1)
    self.addLink(switch2, switch5, 3, 1)
    self.addLink(switch3, switch6, 2, 1)
    self.addLink(switch3, switch7, 3, 1)
    self.addLink(switch4, switch8, 2, 1)
    self.addLink(switch4, switch9, 3, 1)
    self.addLink(switch5, switch10, 2, 1)
    self.addLink(switch5, switch11, 3, 1)
    self.addLink(switch6, switch12, 2, 1)
    self.addLink(switch6, switch13, 3, 1)
    self.addLink(switch7, switch14, 2, 1)
    self.addLink(switch7, switch15, 3, 1)
    self.addLink(switch8, switch16, 2, 1)
    self.addLink(switch8, switch17, 3, 1)
    self.addLink(switch9, switch18, 2, 1)
    self.addLink(switch9, switch19, 3, 1)
    self.addLink(switch10, switch20, 2, 1)
    self.addLink(switch10, switch21, 3, 1)
    self.addLink(switch11, switch22, 2, 1)
    self.addLink(switch11, switch23, 3, 1)
    self.addLink(switch12, switch24, 2, 1)
    self.addLink(switch12, switch25, 3, 1)
    self.addLink(switch13, switch26, 2, 1)
    self.addLink(switch13, switch27, 3, 1)
    self.addLink(switch14, switch28, 2, 1)
    self.addLink(switch14, switch29, 3, 1)
    self.addLink(switch15, switch30, 2, 1)
    self.addLink(switch15, switch31, 3, 1)
    self.addLink(switch16, switch32, 2, 1)
    self.addLink(switch16, switch33, 3, 1)
    self.addLink(switch17, switch34, 2, 1)
    self.addLink(switch17, switch35, 3, 1)
    self.addLink(switch18, switch36, 2, 1)
    self.addLink(switch18, switch37, 3, 1)
    self.addLink(switch19, switch38, 2, 1)
    self.addLink(switch19, switch39, 3, 1)
    self.addLink(switch20, switch40, 2, 1)
    self.addLink(switch20, switch41, 3, 1)
    self.addLink(switch21, switch42, 2, 1)
    self.addLink(switch21, switch43, 3, 1)
    self.addLink(switch22, switch44, 2, 1)
    self.addLink(switch22, switch45, 3, 1)
    self.addLink(switch23, switch46, 2, 1)
    self.addLink(switch23, switch47, 3, 1)
    self.addLink(switch24, switch48, 2, 1)
    self.addLink(switch24, switch49, 3, 1)
    self.addLink(switch25, switch50, 2, 1)
    self.addLink(switch25, switch51, 3, 1)
    self.addLink(switch26, switch52, 2, 1)
    self.addLink(switch26, switch53, 3, 1)
    self.addLink(switch27, switch54, 2, 1)
    self.addLink(switch27, switch55, 3, 1)
    self.addLink(switch28, switch56, 2, 1)
    self.addLink(switch28, switch57, 3, 1)
    self.addLink(switch29, switch58, 2, 1)
    self.addLink(switch29, switch59, 3, 1)
    self.addLink(switch30, switch60, 2, 1)
    self.addLink(switch30, switch61, 3, 1)
    self.addLink(switch31, switch62, 2, 1)
    self.addLink(switch31, switch63, 3, 1)
    self.addLink(switch32, switch64, 2, 1)
    self.addLink(switch32, switch65, 3, 1)
    self.addLink(switch33, switch66, 2, 1)
    self.addLink(switch34, switch67, 2, 1)
    self.addLink(switch35, switch68, 2, 1)
    self.addLink(switch35, switch69, 3, 1)
    self.addLink(switch36, switch70, 2, 1)
    self.addLink(switch36, switch71, 3, 1)
    self.addLink(switch37, switch72, 2, 1)
    self.addLink(switch38, switch73, 2, 1)
    self.addLink(switch39, switch74, 2, 1)
    self.addLink(switch40, switch75, 2, 1)
    self.addLink(switch41, switch76, 2, 1)
    self.addLink(switch42, switch77, 2, 1)
    self.addLink(switch43, switch78, 2, 1)
    self.addLink(switch43, switch79, 3, 1)
    self.addLink(switch45, switch80, 2, 1)
    self.addLink(switch45, switch81, 3, 1)
    self.addLink(switch46, switch82, 2, 1)
    self.addLink(switch47, switch83, 2, 1)
    self.addLink(switch48, switch84, 2, 1)
    self.addLink(switch50, switch85, 2, 1)
    self.addLink(switch50, switch86, 3, 1)
    self.addLink(switch51, switch87, 2, 1)
    self.addLink(switch52, switch88, 2, 1)
    self.addLink(switch52, switch89, 3, 1)
    self.addLink(switch53, switch90, 2, 1)
    self.addLink(switch55, switch91, 2, 1)
    self.addLink(switch55, switch92, 3, 1)
    self.addLink(switch56, switch93, 2, 1)
    self.addLink(switch56, switch94, 3, 1)
    self.addLink(switch57, switch95, 2, 1)
    self.addLink(switch58, switch96, 2, 1)
    self.addLink(switch58, switch97, 3, 1)
    self.addLink(switch60, switch98, 2, 1)
    self.addLink(switch60, switch99, 3, 1)
    self.addLink(switch61, switch100, 2, 1)
    self.addLink(switch61, switch101, 3, 1)
    self.addLink(switch62, switch102, 2, 1)
    self.addLink(switch62, switch103, 3, 1)
    self.addLink(switch63, switch104, 2, 1)
    self.addLink(switch63, switch105, 3, 1)

    ## Enlaces CE
    self.addLink(switch77, routerLan1, 2, 0)
    self.addLink(switch100, routerLan2, 2, 0)
    self.addLink(h0, routerLan1, 0, 1)
    self.addLink(h1, routerLan2, 0, 1)


