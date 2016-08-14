f = open("resultados/tiemposBasic.txt","r")

lines = f.readlines()

porcentajesCaminoCapa2 = []
porcentajesCaminoCapa3 = []
porcentajesMPLSCapa2 = []
porcentajesMPLSCapa3 = []
porcentajesFlujosCapa2 = []
porcentajesFlujosCapa3 = []

for line in lines:
	if "Capa2    --> Camino: " in line:
		porcentajesCaminoCapa2.append(float(line[21:-2]))

	if "Capa2    --> MPLS: " in line:
		porcentajesMPLSCapa2.append(float(line[19:-2]))

	if "Capa2    --> Flujos " in line:
		porcentajesFlujosCapa2.append(float(line[20:-2]))

	if "Capa3    --> Camino: " in line:
		porcentajesCaminoCapa3.append(float(line[21:-2]))

	if "Capa3    --> MPLS: " in line:
		porcentajesMPLSCapa3.append(float(line[19:-2]))

	if "Capa3    --> Flujos " in line:
		porcentajesFlujosCapa3.append(float(line[20:-2]))



print "VPN Capa 2 -- Promedio Camino: " + str(sum(porcentajesCaminoCapa2)/len(porcentajesCaminoCapa2))
print "VPN Capa 2 -- Promedio MPLS: " + str(sum(porcentajesMPLSCapa2)/len(porcentajesMPLSCapa2))
print "VPN Capa 2 -- Promedio Flujos: " + str(sum(porcentajesFlujosCapa2)/len(porcentajesFlujosCapa2))

print "VPN Capa 3 -- Promedio Camino: " + str(sum(porcentajesCaminoCapa3)/len(porcentajesCaminoCapa3))
print "VPN Capa 3 -- Promedio MPLS: " + str(sum(porcentajesMPLSCapa3)/len(porcentajesMPLSCapa3))
print "VPN Capa 3 -- Promedio Flujos: " + str(sum(porcentajesFlujosCapa3)/len(porcentajesFlujosCapa3))