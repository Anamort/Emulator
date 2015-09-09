#!/bin/bash

cd /home/santiago/LiveCode-master/ryu-master
PYTHONPATH=. ./bin/ryu run --observe-links ryu/app/proyecto/businessLogic/rauflowapp.py