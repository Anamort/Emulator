#!/usr/bin/python
import requests
import json
import time

CONTROLLER_URL = "http://192.168.1.10:8080/services"

nodo1 = "192.168.1.14"
nodo2 = "192.168.1.12"
interfazNodo1 = "10.0.0.2"
interfazNodo2 = "10.1.0.2"
cantidadDeVPNs = 100

json_template = {}
json_template['ingress_node'] = ""
json_template['egress_node'] = ""
json_template['ingress_interface'] = ""
json_template['egress_interface'] = ""
json_template['eth_src'] = ""
json_template['eth_dst'] = ""
json_template['eth_type'] = "0x0800"
json_template['vlan_vID'] = ""
json_template['vlanPCP'] = ""
json_template['ARP_spa'] = ""
json_template['ARP_tpa'] = ""
json_template['IPv4_src'] = ""
json_template['IPv4_dst'] = ""
json_template['IPv6_src'] = ""
json_template['IPv6_dst'] = ""
json_template['ICMPv4_type'] = ""
json_template['ICMPv4_code'] = ""
json_template['ICMPv6_type'] = ""
json_template['ICMPv6_code'] = ""
json_template['TCP_src'] = ""
json_template['TCP_dst'] = ""
json_template['UDP_src'] = ""
json_template['UDP_dst'] = ""
json_template['SCTP_src'] = ""
json_template['SCTP_dst'] = ""
json_template['service_name'] = ""
json_template['service_color'] = "RGB(60,96,122)"
json_template['ID'] = ""
json_template['IP_proto'] = ""
json_template['VPN_service_type'] = 3

for i in range(cantidadDeVPNs):
	datos = json_template
	datos['ingress_node'] = nodo1
	datos['egress_node'] = nodo2
	datos['ingress_interface'] = interfazNodo1
	datos['egress_interface'] = interfazNodo2
	datos['service_name'] = "VPN" + str(i) + "Ida"
	eth_src = "00:00:00:00:"
	eth_src += "0x{:02x}".format(i/256)[2:] + ":"
	eth_src += "0x{:02x}".format(i)[2:]
	datos['eth_src'] = eth_src
	resp = requests.post(CONTROLLER_URL,data=json.dumps(datos))
	time.sleep(0.2)
	# print json.dumps(datos)
	print resp.reason

	j = i + 1
	datos = json_template
	datos['ingress_node'] = nodo2
	datos['egress_node'] = nodo1
	datos['ingress_interface'] = interfazNodo2
	datos['egress_interface'] = interfazNodo1
	datos['service_name'] = "VPN" + str(i) + "Vuelta"
	eth_src = "00:00:00:00:"
	eth_src += "0x{:02x}".format(j/256)[2:] + ":"
	eth_src += "0x{:02x}".format(j)[2:]
	datos['eth_src'] = eth_src
	resp = requests.post(CONTROLLER_URL,data=json.dumps(datos))
	time.sleep(0.2)
	# print json.dumps(datos)
	print resp.reason
