#!/usr/bin/python

"""
Script para levantar el entorno
"""

import os
import sys
import atexit

import mininet.util
sys.modules['mininet.util'] = mininet.util

from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info

from mininet.cli import CLI
from mininet.net import Mininet

from topoBasica import CustomTopology

net = None

def startNetwork():
  # Se levanta la topologia

  info('** Creating test topology\n')
  topo = CustomTopology()

  info('** Starting the network\n')
  global net
  net = Mininet(topo, controller=None)
  
  net.start()

  # Se borra el archivo json de inicializacion viejo
  if os.path.exists('utils/init_json.json'):
    os.remove('utils/init_json.json')
  
  # Invocar el metodo start en cada nodo en 'startList'
  info('** Starting RAU nodes\n')
  for node in topo.startList:
    n = net.get(node)
    n.start()

  # info('** Dumping host connections\n')
  # dumpNodeConnections(net.hosts)

  info('\n** Running CLI\n')
  CLI(net)


def stopNetwork():
  # Se detiene el entorno y se terminan todos los procesos
  if net is not None:
      info('** Tearing down network\n')
      net.stop()

if __name__ == '__main__':
  # Force cleanup on exit by registering a cleanup function
  atexit.register(stopNetwork)

  # Tell mininet to print useful information
  setLogLevel('info')
  startNetwork()
