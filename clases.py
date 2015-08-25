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
    #self.cmd('sh ryu_start.sh &')
    
  def terminate( self ):
    # Usar con cuidado
    # Parametrizar
    self.cmd("pkill -f ryu_start.sh")
    self.cmd("pkill -f simple_switch_13.py")
    Host.terminate(self)

class OVSQuaggaRouter(Host):
  zebra_exec = '/usr/lib/quagga/zebra'
  ospfd_exec = '/usr/lib/quagga/ospfd'
  snmpd_exec = '/usr/sbin/snmpd'
  quaggaPath = '/usr/lib/quagga/'
  ovs_initd = "/etc/init.d/openvswitchd"
  baseDIR = "/tmp"
  OF_V = "OpenFlow13"
  OVS_MANAGEMENT_PORT = "6640"
  
  def __init__(self, name, loopback, ips, dpid, *args, **kwargs ):
    dirs = ['/var/log/', '/var/log/quagga', '/var/run', '/var/run/quagga', '/var/run/openvswitch']
    Host.__init__(self, name, privateDirs=dirs, *args, **kwargs )   
    self.loopback = loopback
    self.path_ovs = "%s/%s/ovs" %(self.baseDIR, self.name)
    self.ips = ips
    self.dpid = dpid
    self.path_quagga = "%s/%s/quagga" %(self.baseDIR, self.name)
    self.path_snmpd = "%s/%s/snmpd" %(self.baseDIR, self.name)
		
  def start(self):
    info("%s " % self.name)
    # Se numera a partir de eth3 (eth1 y eth2 no parecen funcionar del todo, investigar)
    START_INTERFACE = 0
    # if_names: arreglo que contiene los nombres de las interfaces del router
    if_names = []
    for x in range(START_INTERFACE, START_INTERFACE + len(self.ips)):
      if_names.append("%s-eth%s" %(self.name, str(x)))
		
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
   
    # Configurar other_config, que va a incluir las IP
    ip_addr_config_field = "other_config:ip_addresses="
    for ip_addr in self.ips[:-1]:
      ip_addr_config_field += ip_addr
      ip_addr_config_field += "/"
    ip_addr_config_field += self.ips[-1] 
    
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait -- set Bridge %s other_config:datapath-id=%s %s" %(self.path_ovs, self.name, self.dpid, ip_addr_config_field))
    
    # Agregar controlador
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait set-controller %s tcp:192.168.1.10:6633" %(self.path_ovs, self.name))
    
    # Gestion remota
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait set-manager ptcp:%s" %(self.path_ovs, self.OVS_MANAGEMENT_PORT))
    
    # Agregar puertos
    for interfaceName in if_names[1:]:
      self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait add-port %s %s" %(self.path_ovs, self.name, interfaceName))
    #self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait add-port %s %s -- set Interface %s type=internal" %(self.path_ovs, self.name, 
    #vi_name, vi_name))
    
    # Configuracion de Quagga
    os.mkdir(self.path_quagga)
    zebra_conf = open(self.path_quagga + "/zebra.conf","w")
    ospfd_conf = open(self.path_quagga + "/ospfd.conf","w")
    
    ospfd_conf.write("hostname ospfd\n")
    ospfd_conf.write("password zebra\n")
    ospfd_conf.write("log file /var/log/quagga/ospfd.log\n\n")
    for interfaceName in if_names:
      ospfd_conf.write("interface %s \n" % interfaceName)
    ospfd_conf.write("router ospf\n")
    ospfd_conf.write("ospf router-id %s\n" % self.ips[0])
    for ip in self.ips:
       ospfd_conf.write("network %s/24 area 0\n" % ip)
    
    zebra_conf.write("hostname zebra\n")
    zebra_conf.write("password zebra\n")
    zebra_conf.write("enable password zebra\n")
    zebra_conf.write("log file /var/log/quagga/zebra.log\n\n")
    
    ospfd_conf.close()
    zebra_conf.close()
    
    self.cmd("chmod -R 777 /var/log/quagga")
    self.cmd("chmod -R 777 /var/run/quagga")
    self.cmd("chmod -R 777 %s" %(self.path_quagga))
    self.cmd("chown quagga.quaggavty %s/zebra.conf" % self.path_quagga)
    self.cmd("chown quagga.quaggavty %s/ospfd.conf" % self.path_quagga)
    
    #
    zebra_pid = open(self.path_quagga + "/zebra.pid","w")
    ospfd_pid = open(self.path_quagga + "/ospfd.pid","w")
    zebra_pid.close()
    ospfd_pid.close()
    self.cmd("chmod -R 777 %s/zebra.pid" % self.path_quagga)
    self.cmd("chmod -R 777 %s/ospfd.pid" % self.path_quagga)
    self.cmd("chown quagga.quaggavty %s/zebra.pid" % self.path_quagga)
    self.cmd("chown quagga.quaggavty %s/ospfd.pid" % self.path_quagga)
    #

    self.cmd("%s -f %s/zebra.conf -A 127.0.0.1 -i %s/zebra.pid &" %(self.zebra_exec, self.path_quagga, self.path_quagga))
    self.cmd("%s -f %s/ospfd.conf -A 127.0.0.1 -i %s/ospfd.pid &" %(self.ospfd_exec, self.path_quagga, self.path_quagga))
    self.cmd('sysctl -w net.ipv4.ip_forward=1')
    
    
    # Configuracion de SNMP
    #os.mkdir(self.path_snmpd)
    #shutil.copyfile("snmpd.conf", self.path_snmpd + "/snmpd.conf")
    #snmpd_conf = open(self.path_snmpd + "/snmpd.conf", "a")
    #snmpd_conf.write("sysLocation	%s\n" % self.name)
    #snmpd_conf.write("sysContact	svidal91@hotmail.com\n")
    #snmpd_conf.write("sysName	%s\n" % self.name)
    #snmpd_conf.write("config agent\n")
    #snmpd_conf.write("	option agentaddress %s:161\n" % self.ips[0])
    #snmpd_conf.close()
    #self.cmd("chmod -R 777 %s/snmpd.pid" % self.path_snmpd)
    #self.cmd("%s -Lsd -Lf /dev/null -p /var/run/snmpd.pid -C -c %s/snmpd.conf -a" %(self.snmpd_exec, self.path_snmpd))
      
    # Otras configs
    i = 0
    for ip in self.ips:
      self.cmd('ifconfig %s %s netmask 255.255.255.0' %(if_names[i], ip))
      i = i + 1

  def terminate( self ):
    # Cuidado con este comando
    self.cmd("pkill -f %s/%s/" %(self.baseDIR, self.name))
    Host.terminate(self)
    shutil.rmtree("%s/%s" %(self.baseDIR, self.name), ignore_errors=True)
    
    
    
    
    
    