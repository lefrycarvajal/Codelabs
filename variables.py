nombre = str (input(prompt="Escribe tu nombre: "))
ne = int (input(prompt="Inserta un numero: "))
nf = float (input(prompt="Ahora inserta un numero decimal: "))
trfls = bool (input(prompt="¿Pusiste los datos correctos? True/False "))

print(f"Hola {nombre}, Hagamos una suma...", f"La suma de {ne}", f"+ {nf}", f"= {ne+nf}" sep="\n" )

# Límites de enteros en Python
'''
entero_minimo = -2**31  # Valor mínimo para enteros con signo de 32 bits
entero_maximo = 2**31 - 1  # Valor máximo para enteros con signo de 32 bits

print("Límite mínimo de entero:", entero_minimo)
print("Límite máximo de entero:", entero_maximo)

Límites de números de punto flotante en Python
flotante_minimo = 2.2250738585072014e-308  # Valor mínimo para números de punto flotante en doble precisión
flotante_maximo = 1.7976931348623157e+308  # Valor máximo para números de punto flotante en doble precisión

print("Límite mínimo de punto flotante:", flotante_minimo)
print("Límite máximo de punto flotante:", flotante_maximo)
'''