"""
Escribir un programa que pregunte el nombre del usuario en la consola y 
un número entero e imprima por pantalla en líneas 
distintas el nombre del usuario tantas veces como el número introducido.
"""

name = input("Como te llamas? ")
number = int(input("Dime un numero: "))

print((name + "\n") * number)

""" for i in range(0,number):
    print(name) """
    
"""Escribir un programa que pregunte el nombre completo del usuario en la consola 
y después muestre por pantalla el nombre completo del usuario tres veces, una con 
todas las letras minúsculas, 
otra con todas las letras mayúsculas y otra solo con la primera letra del 
nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera."""

full_name = input("Como te llamas? ")

print(full_name.upper())
print(full_name.lower())
print(full_name.title())


"""Escribir un programa que pregunte el nombre del usuario en la consola
y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre."""

print(name.upper(), "tiene", len(name), "letras")


"""Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos 
(por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número 
de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión."""

# +34-913724710-56 Formato
telefono = input("Dame tu numero de telefono: ")

print('El numero de teléfono es',telefono.split('-')[1])
print('El número de teléfono es', telefono[4:-3])

"""Escribir un programa que pida al usuario que introduzca una frase
en la consola y muestre por pantalla la frase invertida."""

frase = input("Introduzca una frase: ")

print(frase[::-1])

"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla 
otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es."""

email= input("Introduce tu email: ")

print(email[:email.find('@')] + '@ceu.es')

email = email.split('@')[0] + '@ceu.es'


print(email)


"""Escribir un programa que pregunte al usuario la fecha de su nacimiento 
en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
Adaptar el programa anterior para que también funcione cuando el día o
el mes se introduzcan con un solo carácter."""

fecha = input("Introduce la fecha de nacimiento (dd/mm/aaaa)")

#basica
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])

# media
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)

# Favorita
nacimiento=fecha.split('/')
print("Naciste el dia",nacimiento[0],"del mes", nacimiento[1], 'del año', nacimiento[2])

"""Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta."""

cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')

print(cesta.replace(',', '\n'))

# alternativa
cesta=cesta.split(',')
for c in cesta:
    print(c.strip())


"""Escribir un programa que pregunte el nombre el un producto,
su precio y un número de unidades y muestre por pantalla una cadena 
con el nombre del producto seguido de su precio unitario con 6 dígitos enteros 
y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales."""


producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))