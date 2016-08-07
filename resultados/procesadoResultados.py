f = open("resultados/tiemposMedium4.txt","r")

lines = f.readlines()

porcentajesCamino = []
porcentajesMPLS = []
porcentajesFlujos = []

for line in lines:
	if "    --> Camino: " in line:
		porcentajesCamino.append(float(line[16:-2]))

	if "    --> MPLS: " in line:
		porcentajesMPLS.append(float(line[14:-2]))

	if "    --> Flujos " in line:
		porcentajesFlujos.append(float(line[15:-2]))

	if (len(porcentajesFlujos) == 8) and (len(porcentajesCamino) == 8) and (len(porcentajesMPLS) == 8):
		print "VPN Capa 2 -- Promedio Camino: " + str(sum(porcentajesCamino)/len(porcentajesCamino))
		print "VPN Capa 2 -- Promedio MPLS: " + str(sum(porcentajesMPLS)/len(porcentajesMPLS))
		print "VPN Capa 2 -- Promedio Flujos: " + str(sum(porcentajesFlujos)/len(porcentajesFlujos))
		porcentajesCamino = []
		porcentajesFlujos = []
		porcentajesMPLS = []

print "VPN Capa 3 -- Promedio Camino: " + str(sum(porcentajesCamino)/len(porcentajesCamino))
print "VPN Capa 3 -- Promedio MPLS: " + str(sum(porcentajesMPLS)/len(porcentajesMPLS))
print "VPN Capa 3 -- Promedio Flujos: " + str(sum(porcentajesFlujos)/len(porcentajesFlujos))