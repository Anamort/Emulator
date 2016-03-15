# Este archivo contiene todas las clases necesarias para el entorno de emulacion
# Estas clases son: RAUHost, RAUController, RAUSwitch, QuaggaRouter
# Para utilizarlas se debe incluirlas y instanciarlas con todos los parametros
# necesarios

import re
import inspect
import os
import sys
import shutil
import time
import json
from subprocess import Popen,PIPE
from mininet.node import Host
from mininet.log import info, error

# Los siguientes metodos son metodos auxiliares para obtener
# direcciones IP y mascaras de red a partir del formato X.X.X.X/X
# ya que con ese formato se pasan las direcciones a los constructores

# Retorna direccion IP
def getIP(ip_address):
  return ip_address.split("/")[0]

# Retorna mask length
def getMaskLength(ip_address):
  return ip_address.split("/")[1]

# Retorna netmask
# Solo se soporta 8, 16, 24 para facilitar implementacion
# Retorna 255.255.255.255 en otros casos
def getNetmask(ip_address):
  mask_length = int(getMaskLength(ip_address))
  if (mask_length == 8):
    return "255.0.0.0"
  if (mask_length == 16):
    return "255.255.0.0"
  if (mask_length == 24):
    return "255.255.255.0"
  return "255.255.255.255"  

class RAUHost(Host):
  def __init__(self, name, ips, gw=None, ce_mac_address=None, *args, **kwargs ):
    Host.__init__(self, name, *args, **kwargs )
    self.ips = ips
    self.gw = gw
    self.ce_mac_address = ce_mac_address
		
  def start(self):
    info("%s " % self.name)
    # Configuros la ips
    i = 0
    for intf in self.intfList():
      ip = getIP(self.ips[i])
      mask = getMaskLength(self.ips[i])
      intf.setIP(ip,mask)
      i += 1

    if self.ce_mac_address is not None:
      # Se configura la MAC de la interfaz con la red backbone
      self.intfList()[0].setMAC(self.ce_mac_address)

    if self.gw is not None:
      # Configuro el default GW
      self.cmd("route add default gw %s %s" %(self.gw, self.intfList()[0]))
    
  def terminate( self ):
    Host.terminate(self)

class RAUController(Host):
  def __init__(self, name, ips, *args, **kwargs ):
    Host.__init__(self, name, *args, **kwargs )
    self.ips = ips
		
  def start(self):
    info("%s " % self.name)
    # Configuro las ips
    i = 0
    for intf in self.intfList():
      ip = getIP(self.ips[i])
      mask = getMaskLength(self.ips[i])
      intf.setIP(ip,mask)
      i += 1

    # ip = getIP(self.ip)
    # mask = getMaskLength(self.ip)
    # self.intfList()[0].setIP(ip,mask)
    # Se levanta el controlador
    self.cmd('sh utils/ryu_start.sh &')
    
  def terminate( self ):
    # Usar con cuidado
    # Parametrizar
    self.cmd("pkill -f ryu_start.sh")
    self.cmd("pkill -f gui_topology.py")
    Host.terminate(self)

class RAUSwitch(Host):
  zebra_exec = '/usr/lib/quagga/zebra'
  ospfd_exec = '/usr/lib/quagga/ospfd'
  quaggaPath = '/usr/lib/quagga/'
  ovs_initd = "/etc/init.d/openvswitchd"
  baseDIR = "/tmp"
  OF_V = "OpenFlow13"
  OVS_MANAGEMENT_PORT = "6640"
  
  def __init__(self, name, controller_ip, ips, dpid=None, border=0, ce_ip_address=None, ce_mac_address=None, *args, **kwargs ):
    dirs = ['/var/log/', '/var/log/quagga', '/var/run', '/var/run/quagga', '/var/run/openvswitch', '/usr/local/var/run/openvswitch']
    Host.__init__(self, name, privateDirs=dirs, *args, **kwargs )
    self.path_ovs = "%s/%s/ovs" %(self.baseDIR, self.name)
    self.ips = ips

    if dpid is None:
      dpid = format((int(re.search(r'\d+', name).group())), '#018x')[2:]

    self.dpid = dpid
    self.controller_ip = controller_ip
    self.border = border
    self.ce_ip_address = ce_ip_address
    self.ce_mac_address = ce_mac_address
    self.path_quagga = "%s/%s/quagga" %(self.baseDIR, self.name)
		
  def start(self):
    info("%s " % self.name)
    # if_names: lista que contiene los nombres de las interfaces del router
    if_names = []
    for intf in self.intfList():
      if_names.append(intf.name)
    
    # vif_names: lista con los nombres interfaces virtuales del router
    vif_names = []
    for intf in self.intfList()[1:]:
      vif_names.append('v'+intf.name)
		
    shutil.rmtree("%s/%s" %(self.baseDIR, self.name), ignore_errors=True)
    os.mkdir("%s/%s" %(self.baseDIR, self.name))
    os.mkdir(self.path_ovs)
    
    # Inicializaciones de OVS
    self.cmd("ovsdb-tool create %s/conf.db" % self.path_ovs)
    self.cmd("ovsdb-server %s/conf.db --remote=punix:%s/db.sock --remote=db:Open_vSwitch,Open_vSwitch,manager_options --no-chdir --unixctl=%s/ovsdb-server.sock --detach" %(self.path_ovs, self.path_ovs, self.path_ovs))
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait init" % self.path_ovs)
    self.cmd("ovs-vswitchd unix:%s/db.sock --unixctl=%s/ovs-vswitchd.9999.ctl -vinfo --log-file=%s/ovs-vswitchd.log --pidfile=%s/ovs-vswitchd.pid --no-chdir --detach" %(self.path_ovs, self.path_ovs, self.path_ovs, self.path_ovs))

    # Creacion y configuracion del bridge
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait add-br %s" %(self.path_ovs, self.name))
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait set bridge %s protocols=%s 2> /dev/null" %(self.path_ovs, 
    self.name, self.OF_V))
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait set-fail-mode %s secure" %(self.path_ovs, self.name))
    self.cmd('ovs-vsctl --db=unix:%s/db.sock --no-wait set bridge %s datapath_type=netdev' %(self.path_ovs, self.name))
    # self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait set controller %s connection-mode=out-of-band" %(self.path_ovs, self.name))
    
    # Configuracion de sFlow
    # self.cmd("sudo ovs-vsctl --db=unix:%s/db.sock --no-wait -- --id=@sflow create sflow agent=%s  target=\"%s\" sampling=10 polling=10 -- -- set bridge %s sflow=@sflow" %(self.path_ovs, if_names[0], self.controller_ip, self.name))
    
    # Se asignan las direcciones IP a las interfaces fisicas
    # Esto es provisorio solo para facilitar la implementacion de "ports_info"
    i = 0
    for intf in self.intfList():
      ip = getIP(self.ips[i])
      mask = getMaskLength(self.ips[i])
      intf.setIP(ip,mask)
      i = i + 1
   
    # Configurar other_config, que va a incluir datos de los puertos
    ip_addr_config_field = "other_config:ports_info="
    for interface in self.intfList()[:-1]:
      ip_addr_config_field += interface.name
      ip_addr_config_field += "_"
      ip_addr_config_field += interface.ip
      ip_addr_config_field += "_"
      ip_addr_config_field += interface.mac
      ip_addr_config_field += "/"
    ult_intf = self.intfList()[-1]
    ip_addr_config_field += ult_intf.name
    ip_addr_config_field += "_"
    ip_addr_config_field += ult_intf.ip
    ip_addr_config_field += "_"
    ip_addr_config_field += ult_intf.mac
    
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait -- set Bridge %s other_config:datapath-id=%s %s" %(self.path_ovs, self.name, self.dpid, ip_addr_config_field))
    
    # Agregar controlador
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait set-controller %s tcp:%s:6633" %(self.path_ovs, self.name, self.controller_ip))
    
    # Gestion remota
    self.cmd("ovs-vsctl --db=unix:%s/db.sock --no-wait set-manager ptcp:%s" %(self.path_ovs, self.OVS_MANAGEMENT_PORT))
    
    # Agregar puertos
    port_number = 0
    for interfaceName in if_names[1:]:
      port_number = port_number + 1
      self.cmd("ovs-vsctl --db=unix:%s/db.sock add-port %s %s -- set Interface %s ofport_request=%s" %(self.path_ovs, self.name, interfaceName, interfaceName, str(port_number)))
      
    # Agregar puertos virtuales
    for interfaceName in vif_names:
      port_number = port_number + 1
      self.cmd("ovs-vsctl --db=unix:%s/db.sock add-port %s %s -- set Interface %s type=internal ofport_request=%s" %(self.path_ovs, self.name, interfaceName, interfaceName, str(port_number)))
    
    # Prueba con 1 segundo de espera antes de agregar flujos
    # time.sleep(5)

    # Instala flujos para las interfaces virtuales
    i = 1
    for interfaceName in vif_names:
      nro_puerto_virtual = i + len(vif_names)
      if self.border == 1 and i == len(vif_names):
        # Si es un router de borde y es la ultima interfaz, entonces es la interfaz con el CE
        # Por lo tanto le agrego dl_type=0x0806
        self.cmd('ovs-ofctl -O %s add-flow "%s" table=0,priority=0,hard_timeout=0,idle_timeout=0,in_port=%s,dl_type=0x0806,actions=output:%s' %(self.OF_V, self.name, str(i), str(nro_puerto_virtual)))
        self.cmd('ovs-ofctl -O %s add-flow "%s" table=0,priority=0,hard_timeout=0,idle_timeout=0,in_port=%s,dl_type=0x0806,actions=output:%s' %(self.OF_V, self.name, str(nro_puerto_virtual), str(i)))
      else:        
        self.cmd('ovs-ofctl -O %s add-flow "%s" table=0,priority=0,hard_timeout=0,idle_timeout=0,in_port=%s,actions=output:%s' %(self.OF_V, self.name, str(i), str(nro_puerto_virtual)))
        self.cmd('ovs-ofctl -O %s add-flow "%s" table=0,priority=0,hard_timeout=0,idle_timeout=0,in_port=%s,actions=output:%s' %(self.OF_V, self.name, str(nro_puerto_virtual), str(i)))
        
      i = i + 1
      

    # Asignacion de direcciones IP
    # se asigna 0.0.0.0 a las interfaces fisicas exceptuando la de gestion 
    for interfaceName in if_names[1:]:
      self.cmd("ifconfig %s 0.0.0.0 up" % interfaceName)
      
    # Se asignan las direcciones IP reales a las interfaces virtuales
    i = 1
    for interfaceName in vif_names:
      ip = getIP(self.ips[i])
      mask = getNetmask(self.ips[i])
      self.cmd("ifconfig %s %s netmask %s up" %(interfaceName, ip, mask))
      i = i + 1
      
    
    
    # Configuracion de Quagga
    os.mkdir(self.path_quagga)
    zebra_conf = open(self.path_quagga + "/zebra.conf","w")
    ospfd_conf = open(self.path_quagga + "/ospfd.conf","w")
    
    ospfd_conf.write("hostname ospfd\n")
    ospfd_conf.write("password zebra\n")
    ospfd_conf.write("log file /var/log/quagga/ospfd.log\n\n")
    ospfd_conf.write("interface %s \n" % if_names[0])
    ospfd_conf.write("ip ospf cost 65535 \n")
    for interfaceName in vif_names:
      ospfd_conf.write("interface %s \n" % interfaceName)
    ospfd_conf.write("router ospf\n")
    ip = getIP(self.ips[0])
    ospfd_conf.write("ospf router-id %s\n" % ip)
    for full_ip in self.ips:
      ip = getIP(full_ip)
      mask = getMaskLength(full_ip)
      ospfd_conf.write("network %s/%s area 0\n" % (ip, mask))
    
    zebra_conf.write("hostname zebra\n")
    zebra_conf.write("password zebra\n")
    zebra_conf.write("enable password zebra\n")
    zebra_conf.write("log file /var/log/quagga/zebra.log\n\n")
    
    zebra_conf.write("interface %s \n" % if_names[0])
    zebra_conf.write("ipv6 nd suppress-ra \n")
    for interfaceName in vif_names:
      zebra_conf.write("interface %s \n" % interfaceName)
      zebra_conf.write("ipv6 nd suppress-ra \n")
    
    ospfd_conf.close()
    zebra_conf.close()
    
    shutil.copy("utils/daemons","%s/daemons" % self.path_quagga)
    
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
    
    #zserv = open(self.path_quagga + "/zserv.api","w")
    #zserv.close()
    #self.cmd("chmod -R 777 %s/zserv.api" % self.path_quagga)
    #self.cmd("chown quagga.quagga %s/zserv.api" % self.path_quagga)
    #

    self.cmd("%s -f %s/zebra.conf -A 127.0.0.1 -i %s/zebra.pid &" %(self.zebra_exec, self.path_quagga, self.path_quagga))
    self.cmd("%s -f %s/ospfd.conf -A 127.0.0.1 -i %s/ospfd.pid &" %(self.ospfd_exec, self.path_quagga, self.path_quagga))
    self.cmd('sysctl -w net.ipv4.ip_forward=1')


    # A continuacion se agrega la informacion de este router al json de inicializacion
    init_json = open('utils/init_json.json','a')
    datos = {}
    datos['node_name'] = self.name
    datos['node_top_type'] = self.border
    datos['router_id'] = getIP(self.ips[0])
    json_data = json.dumps(datos)
    init_json.write(json_data + '\n')

    if self.border == 1 and self.ce_ip_address is not None and self.ce_mac_address is not None:
      datos = {}
      datos['iface_top_type'] = 1
      datos['ip_address'] = getIP(self.ips[-1])
      datos['router_id'] = getIP(self.ips[0])
      datos['ce_mac_address'] = self.ce_mac_address
      datos['ce_ip_address'] = self.ce_ip_address
      json_data = json.dumps(datos)
      init_json.write(json_data + '\n')

    # El router con la ip 192.168.1.12 levanta el WS con la informacion de los routers
    if (self.ips[0] == '192.168.1.12/24'):
      self.cmd('python utils/wsOVS.py &')

  def terminate( self ):
    # Cuidado con este comando
    self.cmd("pkill -f %s/%s/" %(self.baseDIR, self.name))
    self.cmd("pkill -f wsOVS.py")
    Host.terminate(self)
    shutil.rmtree("%s/%s" %(self.baseDIR, self.name), ignore_errors=True)
    
class QuaggaRouter(Host):
  zebra_exec = '/usr/lib/quagga/zebra'
  ospfd_exec = '/usr/lib/quagga/ospfd'
  quaggaPath = '/usr/lib/quagga/'
  baseDIR = "/tmp"
  
  def __init__(self, name, ips, ce_mac_address, gw=None, *args, **kwargs ):
    dirs = ['/var/log/', '/var/log/quagga', '/var/run', '/var/run/quagga']
    Host.__init__(self, name, privateDirs=dirs, *args, **kwargs )
    self.ips = ips
    self.ce_mac_address = ce_mac_address
    self.gw = gw
    self.path_quagga = "%s/%s/quagga" %(self.baseDIR, self.name)
		
  def start(self):
    info("%s " % self.name)

    # Se configura la MAC de la interfaz con la red backbone
    self.intfList()[0].setMAC(self.ce_mac_address)
    
    # Se asignan las direcciones IP a las interfaces
    i = 0
    for intf in self.intfList():
      ip = getIP(self.ips[i])
      mask = getMaskLength(self.ips[i])
      intf.setIP(ip,mask)
      i = i + 1      
    
    # Configuracion de Quagga
    shutil.rmtree("%s/%s" %(self.baseDIR, self.name), ignore_errors=True)
    os.mkdir("%s/%s" %(self.baseDIR, self.name))
    os.mkdir(self.path_quagga)
    zebra_conf = open(self.path_quagga + "/zebra.conf","w")
    ospfd_conf = open(self.path_quagga + "/ospfd.conf","w")
    
    ospfd_conf.write("hostname ospfd\n")
    ospfd_conf.write("password zebra\n")
    ospfd_conf.write("log file /var/log/quagga/ospfd.log\n\n")
    ospfd_conf.write("interface %s \n" % self.intfList()[0].name)
    ospfd_conf.write("router ospf\n")
    ip = getIP(self.ips[0])
    ospfd_conf.write("ospf router-id %s\n" % ip)
    ospfd_conf.write("network %s area 0\n" % self.ips[0])
    
    zebra_conf.write("hostname zebra\n")
    zebra_conf.write("password zebra\n")
    zebra_conf.write("enable password zebra\n")
    zebra_conf.write("log file /var/log/quagga/zebra.log\n\n")

    zebra_conf.write("interface %s \n" % self.intfList()[0].name)
    zebra_conf.write("ipv6 nd suppress-ra \n")
    
    ospfd_conf.close()
    zebra_conf.close()
    
    shutil.copy("utils/daemons","%s/daemons" % self.path_quagga)
    
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
    
    #zserv = open(self.path_quagga + "/zserv.api","w")
    #zserv.close()
    #self.cmd("chmod -R 777 %s/zserv.api" % self.path_quagga)
    #self.cmd("chown quagga.quagga %s/zserv.api" % self.path_quagga)
    #

    # self.cmd("%s -f %s/zebra.conf -A 127.0.0.1 -i %s/zebra.pid &" %(self.zebra_exec, self.path_quagga, self.path_quagga))
    # self.cmd("%s -f %s/ospfd.conf -A 127.0.0.1 -i %s/ospfd.pid &" %(self.ospfd_exec, self.path_quagga, self.path_quagga))
    self.cmd('sysctl -w net.ipv4.ip_forward=1')

    if self.gw is not None:
      # Configuro el default GW
      self.cmd("route add default gw %s %s" %(self.gw, self.intfList()[0]))

  def terminate( self ):
    # Cuidado con este comando
    self.cmd("pkill -f %s/%s/" %(self.baseDIR, self.name))
    Host.terminate(self)
    shutil.rmtree("%s/%s" %(self.baseDIR, self.name), ignore_errors=True)

