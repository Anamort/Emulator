"""
Example topology of Quagga routers
"""

import inspect
import os
import sys
import shutil
import time
from subprocess import Popen,PIPE
from mininet.node import Host, OVSKernelSwitch, Node
from mininet.topo import Topo
from mininet.log import info, error

class HostController(Host):
  def __init__(self, name, ip, *args, **kwargs ):
    Host.__init__(self, name, *args, **kwargs )
    self.ip = ip
		
  def start(self):
    self.cmd('ifconfig %s-eth0 %s netmask 255.255.255.0' %(self.name, self.ip))
    self.cmd('sh ryu_start.sh &')

class HybridNode(Host):
  ovs_initd = "/etc/init.d/openvswitchd"
  baseDIR = "/tmp"
  OF_V = "OpenFlow13"
  
  def __init__(self, name, loopback, ips, *args, **kwargs ):
    dirs = ['/var/run', '/var/run/openvswitch']
    Host.__init__(self, name, privateDirs=dirs, *args, **kwargs )   
    self.loopback = loopback
    self.path_ovs = "%s/%s/ovs" %(self.baseDIR, self.name)
    self.ips = ips
		
  def start(self):
    info("%s " % self.name)
		
    shutil.rmtree("%s/%s" %(self.baseDIR, self.name), ignore_errors=True)
    os.mkdir("%s/%s" %(self.baseDIR, self.name))
    os.mkdir(self.path_ovs)
    
    # Inicializaciones de OVS
    self.cmd("ovsdb-tool create %s/conf.db" % self.path_ovs)
    self.cmd("ovsdb-server %s/conf.db --remote=punix:%s/db.sock --remote=db:Open_vSwitch,Open_vSwitch,manager_options --no-chdir --unixctl=%s/ovsdb-server.sock --detach" %(self.path_ovs, self.path_ovs, self.path_ovs))
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait init" % self.path_ovs)
    self.cmd("ovs-vswitchd unix:%s/db.sock -vinfo --log-file=%s/ovs-vswitchd.log --no-chdir --detach" %(self.path_ovs, self.path_ovs))
    
    # Creacion y configuracion del bridge
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait add-br %s" %(self.path_ovs, self.name))
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait set bridge %s protocols=%s 2> /dev/null" %(self.path_ovs, 
    self.name, self.OF_V))
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait set-fail-mode %s secure" %(self.path_ovs, self.name))
    self.cmd('ovs-vsctl --db=unix:%s/db.sock --no-wait set bridge %s datapath_type=netdev' %(self.path_ovs, self.name))
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait set controller %s connection-mode=out-of-band" %(self.path_ovs, self.name))
    
    dp = '0000000000000002'
    if self.name == 'alice':
      dp = '0000000000000003'
    if self.name == 'oz':
      dp = '0000000000000001'
    if self.name == 'possion':
      dp = '0000000000000004'
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait -- set Bridge %s other_config:datapath-id=%s" %(self.path_ovs, self.name, dp))
    
    # Agregar controlador
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait set-controller %s tcp:192.168.1.10:6633" %(self.path_ovs, self.name))
    
    # Agregar puertos
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait add-port %s %s-eth1" %(self.path_ovs, self.name, self.name))
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait add-port %s %s-eth2" %(self.path_ovs, self.name, self.name))
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait add-port %s %s-eth3" %(self.path_ovs, self.name, self.name))
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait add-port %s %s-eth4" %(self.path_ovs, self.name, self.name))
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait add-port %s %s-eth5" %(self.path_ovs, self.name, self.name))
    #self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait add-port %s %s -- set Interface %s type=internal" %(self.path_ovs, self.name, 
    #vi_name, vi_name))
      
      
    # Otras configs
    # Se numera a partir de eth3 (eth1 y eth2 no parecen funcionar del todo, investigar)
    i = 2
    for ip in self.ips:
      i = i + 1
      self.cmd('ifconfig %s-eth%s %s netmask 255.255.255.0' %(self.name, str(i), ip))
    self.cmd('sysctl -w net.ipv4.ip_forward=0')
    self.cmd('ifconfig %s-eth1 10.0.0.7 netmask 255.255.0.0' % self.name)
    self.cmd('ifconfig %s-eth2 10.1.0.7 netmask 255.255.0.0' % self.name)
    



class MyTopo( Topo ):
  def __init__( self ):
    Topo.__init__( self )

    # Hosts
    h0 = self.addHost('h0')
    h1 = self.addHost('h1')
    
    # Galois
    galois = self.addHost('galois', loopback="127.0.0.1",
			  ips=['10.10.1.1','10.10.5.1','10.10.4.1','192.168.1.11'],
			  cls=HybridNode)
    # Oz
    oz = self.addHost('oz', loopback="127.0.0.1",
		      ips=['10.10.1.2','10.10.6.2','10.10.3.1','192.168.1.12'],
		      cls=HybridNode)
    
    # Possion
    possion = self.addHost('possion', loopback="127.0.0.1",
			  ips=['10.10.2.1','10.10.6.1','10.10.4.2','192.168.1.13'],
			  cls=HybridNode)
    
    # Alice
    alice = self.addHost('alice', loopback="127.0.0.1",
			  ips=['10.10.2.2','10.10.5.2','10.10.3.2','192.168.1.14'],
			  cls=HybridNode)
    
    # Controlador
    root = self.addHost('controller', cls=HostController,
			ip='192.168.1.10')
    
    # Switch de la red de gestion
    man_switch = self.addSwitch('s1', protocols='OpenFlow13', failMode='standalone')

    # Enlaces
    self.addLink(man_switch, galois, 1, 6)
    self.addLink(man_switch, oz, 2, 6)
    self.addLink(man_switch, possion, 3, 6)
    self.addLink(man_switch, alice, 4, 6)
    self.addLink(man_switch, root, 0, 0)
    
    self.addLink(galois, alice, 4, 4)
    self.addLink(galois, possion, 5, 5)
    self.addLink(galois, oz, 3, 3)
    self.addLink(alice, possion, 3, 3)
    self.addLink(alice, oz, 5, 5)
    self.addLink(oz, possion, 4, 4)
    
    self.addLink(alice, h0, 1, 0)
    self.addLink(alice, h1, 2, 0)








