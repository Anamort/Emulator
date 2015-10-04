# P2015_44-MininetExtensions

Aquí se encontrará todo el código necesario para levantar el entorno de emulación del prototipo.

A continuación se explican los componentes principales:

  **/utils**: Contiene scripts auxiliares

  **clases.py**: Archivo Python que contiene las clases del entorno, estas son:
    -RAUHost
    -RAUSwitch
    -RAUController
    -QuaggaRouter
  **topo.py**: Archivo Python que declara una topología ejemplo.
  **start.py**: Script que incluye la topología que desea levantar y la inicia.
 
 
Acerca de las clases, a continuación se detallan algunas consideraciones para levantar con éxito el entorno.

Parámetros necesarios para instanciar los objetos:
  **RAUHost**
    -ip: Dirección IP
    -gw: Default gateway

  **RAUSwitch**
    -loopback: Dirección de loopback
    -ips: Direcciones IP de todas las interfaces (formato A.B.C.D/E)
    -dpid: Datapath ID
    -controller_ip: Dirección IP del controlador
    
  **RAUController**
    -ip: Dirección IP
    
    
IMPORTANTE: En el caso de RAUSwitch, donde se debe indicar conjunto de direcciones IP, se debe pasarlas como un arreglo
y el orden de dicho arreglo debe cumplir las siguientes restricciones:

  -La primera dirección IP debe ser la de la red de gestión
  -El orden debe ser coherente con la numeración de las interfaces al agregar los links (ver en topo.py como se agregan los links)