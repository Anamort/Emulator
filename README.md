# P2015_44

En este repositorio se encuentra la documentación y el código desarrollado para el proyecto "Escalabilidad de Redes Definidas por Software en la Red Académica"

Su estructura es:
  * **Documentacion**: contiene toda la documentación del proyecto.
  * **topologies**: contiene las topologias de prueba utilizadas en el proyecto.
  * **utils**: Contiene archivos y scripts utilizados por el entorno.

  * **rau_nodes.py**: Archivo Python que contiene las clases del entorno, estas son:
    - RAUHost
    - RAUSwitch
    - RAUController
    - QuaggaRouter
  * **graphml_loader.py**: Archivo Python que procesa archivos de tipo graphml y genera topologias listas para utilizar.
  * **start.py**: Script que inicia el emulador.
 
Por instrucciones sobre cómo utilizar el entorno, leer Apéndice 1 del informe (Documentacion/thesis.pdf)

El repositorio con el código de RAUFlow con las últimas modifcaciones se encuentra en https://github.com/santiagovidal/LiveCode
