val1 = bool(True)
val2=False
print (type(val1))
print (val1)
print("tipos de datos booleanos")
print(True)
print(False)
print(True + True) # detalles extrañas en python  //2
print(True * True) # detalles extrañas en python //1
print(True * False)
print(False + False)
print(False * False)

print("datos de tipos ")
var_booleana=bool(1)
print(var_booleana)
# 
var_boolean=bool(0)
print(var_boolean)

print("OPERADORES DE COMPARACION  CON PUNTO FLOTANTE")
comparar = int(10)
flotante = float(10.0)
print(comparar < flotante)
print(comparar > flotante)
print(comparar == flotante)
print(comparar <= flotante)
print(comparar >= flotante)
print(comparar != flotante)
print(comparar is flotante)
print(comparar is not flotante)

print("operadores logicos")
print(True and True)
print(True and False)
print(False or True)
print(False or False)
print(not True)
print(not False)

print("operadores logicos y de prioridad")
print(False and False or True)
print(False and (False or True))
print(not True and False or True)
print(not(True and False or False))
print(not True and (False or False))
print(not True and False or False)