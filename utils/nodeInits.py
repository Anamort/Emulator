#!/usr/bin/python
import requests
import json

CONTROLLER = "http://192.168.1.10:8080/topology/node/"
filename = 'utils/init_json.json'

init_json = open(filename,'r')
lineas = init_json.readlines()

for linea in lineas:
	# linea = linea.replace('\n',"")
	datos = json.loads(linea)
	if 'node_top_type' in datos:
		# Es el mensaje con la informacion del nodo
		resp = requests.post(CONTROLLER + datos['router_id'],data=linea)
	else:
		resp = requests.post(CONTROLLER + 'interfaces/' + datos['router_id'],data=linea)