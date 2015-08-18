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

class RootController(Host):
  def __init__(self, name, *args, **kwargs ):
    Host.__init__(self, name, inNamespace=False, *args, **kwargs )
		
  def start(self):
    self.cmd('ifconfig %s-eth0 10.2.0.2 netmask 255.255.0.0' % self.name)

class HybridNode(Host):
  ovs_initd = "/etc/init.d/openvswitchd"
  baseDIR = "/tmp"
  OF_V = "OpenFlow13"
  
  def __init__(self, name, loopback, *args, **kwargs ):
    dirs = ['/var/run', '/var/run/openvswitch']
    Host.__init__(self, name, privateDirs=dirs, *args, **kwargs )   
    self.loopback = loopback
    self.path_ovs = "%s/%s/ovs" %(self.baseDIR, self.name)
		
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
    
    # Configuracion del datapath, puede ser importante
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait -- set Bridge %s other_config:datapath-id=0000000000000001" %(self.path_ovs, self.name))
    
    # Agregar controlador
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait set-controller %s tcp:10.2.0.2:6633" %(self.path_ovs, self.name))
    
    # Agregar puertos
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait add-port %s %s-eth1" %(self.path_ovs, self.name, self.name))
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait add-port %s %s-eth2" %(self.path_ovs, self.name, self.name))
    #self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait add-port %s %s -- set Interface %s type=internal" %(self.path_ovs, self.name, 
    #vi_name, vi_name))
    
    #uids = self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait find controller | grep _uuid |awk -F':' '{print $2}' | awk '{ gsub (\" \", \"\", $0); print}'" % self.path_ovs)
    #uids = uids[:-1]
    #uid_set = uids.split("\n")
    #for uid in uid_set:
      #uid = uid.strip(' \t\n\r')
      #self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait set controller %s connection-mode=out-of-band" %(self.path_ovs, uid))
      
    # Otras configs
    self.cmd('ifconfig %s-eth1 10.0.0.7 netmask 255.255.0.0' % self.name)
    self.cmd('ifconfig %s-eth2 10.1.0.7 netmask 255.255.0.0' % self.name)
    self.cmd('ifconfig %s-eth3 10.2.0.7 netmask 255.255.0.0' % self.name)
    self.cmd('sysctl -w net.ipv4.ip_forward=0')
    #self.cmd('route add 192.168.0.109/32 gw 10.2.0.2')



class MyTopo( Topo ):
  def __init__( self ):
    Topo.__init__( self )

    # Hosts y Switches
    h0 = self.addHost('h0')
    h1 = self.addHost('h1')
    switch = self.addHost('s1', loopback="127.0.0.1", cls=HybridNode)
    
    # Controlador
    root = self.addHost('controller', cls=RootController)

    # Enlaces
    self.addLink(h0, switch, 0, 1)
    self.addLink(h1, switch, 0, 2)
    self.addLink(root, switch, 0, 3)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	