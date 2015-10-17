"""
Topologia de ejemplo
2 routers
2 hosts
"""

from mininet.topo import Topo
from clases import QuaggaRouter, RAUHost

class CustomTopology( Topo ):
  startList = ['router1', 'router2', 'h0', 'h1']
  def __init__( self ):
    Topo.__init__( self )

    # Hosts
    h0 = self.addHost('h0', ip='10.0.0.1/24', gw='10.0.0.7', cls=RAUHost)
    h1 = self.addHost('h1', ip='10.2.0.1/24', gw='10.2.0.7', cls=RAUHost)
    
    # Galois
    router1 = self.addHost('router1', loopback="127.0.0.1",
              ips=['10.0.0.7/24','10.1.0.1/24'],
              cls=QuaggaRouter)
    # Oz
    router2 = self.addHost('router2', loopback="127.0.0.1",
              ips=['10.2.0.7/24','10.1.0.2/24'],
              cls=QuaggaRouter)

    # Enlaces
    self.addLink(h0, router1, 0, 0)
    self.addLink(router1, router2, 1, 1)
    self.addLink(h1, router2, 0, 0)


