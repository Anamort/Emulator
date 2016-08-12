"""
Precaucion para usar este script:
	No se toma en cuenta la hora en el logeo de los tiempos asi que para que los calculos sean correctos
	el experimento se debe llevar a cabo en un periodo de tiempo que no cambie la hora
"""

from datetime import datetime

f = open("salida.txt","r")

ls = f.readlines()
j = 0

def getNextService(ls, current_index):
	i = current_index
	while "Servicio invocado" not in ls[i]:
		i += 1

	minutes = ls[i][19:].split(":")[1]
	seconds = ls[i][19:].split(":")[2].split(".")[0]
	microseconds1 = int(minutes)*60*1000000 + int(seconds)*1000000 + int(ls[i][19:].split(":")[2].split(".")[1])
	# print microseconds1

	while "Antes de calcular el camino" not in ls[i]:
		i += 1

	minutes = ls[i][29:].split(":")[1]
	seconds = ls[i][29:].split(":")[2].split(".")[0]
	microseconds2 = int(minutes)*60*1000000 + int(seconds)*1000000 + int(ls[i][29:].split(":")[2].split(".")[1])
	# print microseconds2

	while "Despues de calcular el camino y antes de calcular etiquetas MPLS" not in ls[i]:
		i += 1

	minutes = ls[i][66:].split(":")[1]
	seconds = ls[i][66:].split(":")[2].split(".")[0]
	microseconds3 = int(minutes)*60*1000000 + int(seconds)*1000000 + int(ls[i][66:].split(":")[2].split(".")[1])
	# print microseconds3

	while "Despues de calcular etiquetas MPLS y antes de instalar flujos" not in ls[i]:
		i += 1

	minutes = ls[i][63:].split(":")[1]
	seconds = ls[i][63:].split(":")[2].split(".")[0]
	microseconds4 = int(minutes)*60*1000000 + int(seconds)*1000000 + int(ls[i][63:].split(":")[2].split(".")[1])
	# print microseconds4

	while "Despues de instalar flujos" not in ls[i]:
		i += 1

	minutes = ls[i][28:].split(":")[1]
	seconds = ls[i][28:].split(":")[2].split(".")[0]
	microseconds5 = int(minutes)*60*1000000 + int(seconds)*1000000 + int(ls[i][28:].split(":")[2].split(".")[1])
	# print microseconds5

	while "Servicio creado" not in ls[i]:
		i += 1

	minutes = ls[i][17:].split(":")[1]
	seconds = ls[i][17:].split(":")[2].split(".")[0]
	microseconds6 = int(minutes)*60*1000000 + int(seconds)*1000000 + int(ls[i][17:].split(":")[2].split(".")[1])
	# print microseconds6

	tiempo_total = microseconds6 - microseconds1
	tiempo_camino = microseconds3 - microseconds2
	tiempo_mpls = microseconds4 - microseconds3
	tiempo_flujos = microseconds5 - microseconds4

	print "***" * 100
	print "Tiempo total: " + str(tiempo_total)
	print "Tiempo camino: " + str(tiempo_camino)
	print "Tiempo MPLS: " + str(tiempo_mpls)
	print "Tiempo flujos: " + str(tiempo_flujos)
	# print "[AUX] Comparacion: " + str(tiempo_total) + " - " + str(tiempo_flujos + tiempo_mpls + tiempo_camino)
	print "Porcentajes:"
	print "    --> Camino: " + str((float(tiempo_camino)/float(tiempo_total))*100) + "%"
	print "    --> MPLS: " + str((float(tiempo_mpls)/float(tiempo_total))*100) + "%"
	print "    --> Flujos " + str((float(tiempo_flujos)/float(tiempo_total))*100) + "%"

	return i


while j < len(ls):
	new_index = getNextService(ls, j)
	j = new_index



