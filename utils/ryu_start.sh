#!/bin/bash

cd /home/santiago/LiveCode/ryu-master
# ./bin/ryu run --observe-links ryu/app/gui_topology/gui_topology.py
PYTHONPATH=. ./bin/ryu run --observe-links ryu/app/proyecto/businessLogic/gui_topology.py