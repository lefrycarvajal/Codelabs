nombre = str (input(prompt="Escribe tu nombre: "))
ne = int (input(prompt="Inserta un numero: "))
nf = float (input(prompt="Ahora inserta un numero decimal: "))
trfls = bool (input(prompt="¿Pusiste los datos correctos? True/False "))

print(f"Hola {nombre}, Hagamos una suma...", f"La suma de {ne}", f"+ {nf}", f"= {ne+nf}" sep="\n" )