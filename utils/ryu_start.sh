#!/bin/bash

cd /home/santiago/P2015_44-Controlador/LiveCode/ryu-master
# ./bin/ryu run --observe-links ryu/app/gui_topology/gui_topology.py
PYTHONPATH=. ./bin/ryu run --observe-links ryu/app/proyecto/businessLogic/gui_topology.py >> /home/santiago/P2015_44/logControlador.txt 2>&1