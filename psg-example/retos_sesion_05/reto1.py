# Practicar los siguientes ejercicios para 
#el uso de numeros enteros y con punto flotante
# Escribe un programa en python que calcule el salario
# si la cantidad de horas trabjadas es 160 
#y la tarifa por hora de trabajo es de5.5 USD / hora
horas_trabajadas = int(input("ingrese la cantidad de sus horas trabajadas:\n"))
tarifa_hora = 5.5
if horas_trabajadas > 160:
    print("Total ganados en USD es :")
    print (horas_trabajadas*tarifa_hora)
else:
    print ("cantidad de hora trabajadas insuficientes")