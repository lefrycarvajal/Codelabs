nombre = str (input(prompt="Escribe tu nombre: "))
ne = int (input(prompt="Inserta un numero: "))
nf = float (input(prompt="Ahora inserta un numero decimal: "))
trfls = bool (input(prompt="¿Pusiste los datos correctos? True/False "))

print(f"Hola {nombre}, Hagamos una suma...", f"La suma de {ne}", f"+ {nf}", f"= {ne+nf}" sep="\n" )

# Límites de enteros en Python
'''
El valor mínimo para enteros con signo de 32 bits es igual a -2*31, mientras que el valor máximo es igual a 2*31 - 1.

Para obtener estos límites, podemos utilizar las siguientes asignaciones:
entero_minimo = -2**31
entero_maximo = 2**31 - 1

Y luego, podemos imprimir estos valores de la siguiente manera:
print("Límite mínimo de entero:", entero_minimo)
print("Límite máximo de entero:", entero_maximo)

Límites de números de punto flotante en Python
En cuanto a los números de punto flotante en doble precisión, el valor mínimo es aproximadamente 2.2250738585072014e-308, mientras que el valor máximo es aproximadamente 1.7976931348623157e+308.

Podemos representar estos límites de la siguiente manera:
flotante_minimo = 2.2250738585072014e-308
flotante_maximo = 1.7976931348623157e+308

Y luego, para mostrarlos en pantalla, utilizamos las siguientes impresiones:
print("Límite mínimo de punto flotante:", flotante_minimo)
print("Límite máximo de punto flotante:", flotante_maximo)
'''