# P2015_44

Aquí se encontrará todo el código necesario para levantar el entorno de emulación del prototipo.

A continuación se explican los componentes principales:

  * **/utils**: Contiene scripts auxiliares

  * **clases.py**: Archivo Python que contiene las clases del entorno, estas son:
    - RAUHost
    - RAUSwitch
    - RAUController
    - QuaggaRouter
  * **topoVPN2.py**: Archivo Python que declara una topología ejemplo.
  * **start.py**: Script que incluye la topología que desea levantar y la inicia.
 
 
Acerca de las clases, a continuación se detallan algunas consideraciones para levantar con éxito el entorno.

Parámetros necesarios para instanciar los objetos:
  * **RAUHost**
    - ip: Dirección IP
    - gw: Default gateway

  * **RAUSwitch**
    - loopback: Dirección de loopback
    - ips: Direcciones IP de todas las interfaces (formato A.B.C.D/E)
      - La primera direccion IP debe ser la de la red de gestion
      - La ultima direccion IP debe ser la de la interfaz que lo conecta con el router CE (en caso que sea borde)
      - El orden debe ser coherente con la numeración de las interfaces al agregar los links (ver en topo.py como se agregan los links)
    - dpid: Datapath ID
    - controller_ip: Dirección IP del controlador
    - border: 0 o 1 dependiendo de si es router de borde o no
    - ce_ip_addresss: Direccion IP del router CE (aplica solo si es de borde)
    - ce_mac_address: Direccion MAC del router CE (aplica solo si es de borde)
    
  * **RAUController**
    - ip: Dirección IP

  * **QuaggaRouter**
    - loopback: Dirección de loopback
    - ips: Direcciones IP de todas las interfaces (formato A.B.C.D/E)
      - La primera direccion IP debe ser la de la interfaz que lo conecta con el backbone
    - ce_mac_address: Direccion MAC de la interfaz que lo conecta con el backbone
