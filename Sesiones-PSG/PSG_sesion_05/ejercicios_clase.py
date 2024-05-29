#un contador tiene  300 minutos y sele suman 3600 segundso, cuantas horas en total son?
minutos =  int (300)
tiempo_extra_segundos = int(3600)
horas = (minutos + tiempo_extra_segundos / 60) / 60
print(horas)