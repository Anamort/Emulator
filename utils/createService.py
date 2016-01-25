#!/usr/bin/python
import requests
import json

CONTROLLER_URL = "http://192.168.1.10:8080/services"
filename = 'utils/service.json'

init_json = open(filename,'r')
lineas = init_json.readlines()

for linea in lineas:
	datos = json.loads(linea)
	resp = requests.post(CONTROLLER_URL,data=linea)