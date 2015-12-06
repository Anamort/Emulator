#!/usr/bin/python
from flask import Flask
import commands
import re
import json

class Router:
  def __init__(self, dpid, routerId ,puertos,bridgeName):
    self.dpid = dpid
    self.routerId = routerId
    self.puertos = puertos
    self.bridgeName = bridgeName

  def to_JSON(self):
    puertos_json=[]
    for i in self.puertos.values():
      if not i.nombreInterfaz.startswith('v'):			
	puertos_json.append({'numeroOVS':i.numeroOVS, 'mac': i.mac,'nombreInterfaz': i.nombreInterfaz, 'ip': i.ip })
    return json.dumps({'dpid': self.dpid, 'routerId' : self.routerId, 'puertos': puertos_json, 'bridge': self.bridgeName}, separators=(',',':'))     


class Puerto:
  def __init__(self, numeroOVS, mac ,nombreInterfaz, ip):
    self.mac = mac
    self.numeroOVS = numeroOVS
    self.nombreInterfaz = nombreInterfaz
    self.ip = ip

app = Flask(__name__)

@app.route('/snmp/atp/<address>')
def getInfo(address):
  print address
  tempArray = commands.getstatusoutput('ovs-vsctl --db=tcp:%s:6640 list bridge' % address)
  salidaOVS = tempArray[1]
  
  regexp = re.compile('.*ports_info="(.*)"}', re.DOTALL)
  ports_info = regexp.match(salidaOVS).group(1)
  ports = ports_info.split("/")

  puertos = {}
  numeroPuerto = 0
  # Empezamos desde el segundo porque el primero es la interfaz
  # con el controlador
  for portString in ports[1:]:
    splitArray = portString.split("_")
    numeroPuerto = numeroPuerto + 1
    mac = splitArray[2]
    nombreInterfaz = splitArray[0]
    ip = splitArray[1]
    port = Puerto(numeroPuerto,mac,nombreInterfaz,ip)
    puertos[nombreInterfaz] = port
    # El numero de puerto se deriva con el orden de los puertos
    # CUIDADO!!

  # Se obtiene el datapath_id
  regexp = re.compile('.*datapath_id\s*:\s*"(\w+)', re.DOTALL)
  dpid = regexp.match(salidaOVS).group(1)
  
  # Se obtiene el nombre del bridge
  regexp = re.compile('.*name\s*:\s*\"?(\w+)', re.DOTALL)
  bridgeName = regexp.match(salidaOVS).group(1)

  router = Router(dpid,"", puertos,bridgeName)
  
  print router.to_JSON()
  return router.to_JSON()

if __name__ == '__main__':
  # getInfo("192.168.1.14")
    app.run(host='0.0.0.0', port=5000)
	#default port: 5000
	
