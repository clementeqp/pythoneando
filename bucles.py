
# Escribir un programa que pida al usuario un número entero positivo
# y muestre por pantalla todos los números impares desde 1 hasta ese 
# número separados por comas.
""" 
num = int(input('Introduce un entero + : '))
impares=[]

for i in range(1, num + 1):
    if i%2==1:
        impares.append(i)
print(impares)

for i in range(1, num+1, 2):
    print(i, end=", ") """
    
    
# Escribir un programa que pida al usuario un número entero positivo y muestre
# por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

""" num = int(input('Introduce un entero + : '))

for i in range(0, num+1):
    print(num-i, end=',')
    
for i in range(num, -1, -1):
    print(i, end=", ") """
    
# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.

""" cantidad= float(input("Introduce la cantiad: "))
interes = float(input('Introduce el interes: '))
anios = int(input('Introduce el número de años: '))

for i in range(1, anios+1):
    rentabilidad=cantidad*(interes/100)
    cantidad = cantidad + rentabilidad
    print("Año", i, 'Rentabilidad: ',round(rentabilidad,2))
"""
    
# Escribir un programa que pida al usuario un número entero y muestre 
# por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

""" 
*
**
***
****
***** 
"""

""" num = int(input('Introduce un entero + : '))
for i in range(1, num+1):
    print('*'*i)
    
for i in range(num):
    for j in range(i+1):
        print("*", end="")
    print("") """

# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo como el de más abajo.

""" 
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1 
"""

""" num = int(input('Introduce un entero + : '))
for i in range(1, num+1,2):
    for j in range(i,0,-2):
        print(j,end=' ')
    print('') """
    
# Escribir un programa que almacene la cadena de caracteres contraseña 
# en una variable, pregunte al usuario por la contraseña hasta que introduzca 
# la contraseña correcta.
""" 
contraseña='Hola33'

user=''
while(user!=contraseña):
    user = input('Introduce la contraseña: ')
    
print('Password correcto!!!') """


# Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla si es un número primo o no.
""" 
num = int(input('Introduce un entero + : '))

for i in range(2,int(num/2)+1):
    if num%i==0:
        print('El numero no es primo')
        print(i)
        break
    if i==int(num/2):
        print('El numero es primo.')


# con while    
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo") """
    
# Escribir un programa que pida al usuario una palabra y 
# luego muestre por pantalla una a una las letras de la palabra 
# introducida empezando por la última.

""" 
palabra = input('Introduce una palabra: ')

for i in range(1, len(palabra)+1):
    print(palabra[-i],end='')

#otra 

word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])    
"""


# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.

""" frase= input('Introduce una frase: ')
letra = input('Introduce una letra: ')
contador=0
for l in frase:
    if l == letra:
        contador +=1
print('La letra "', letra, '" aparece en la frase: "', frase,'"', contador, 'veces') 
print("La letra '%s' aparece %d veces en la frase '%s'." % (letra, contador, frase)) """       

# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta 
# que el usuario escriba “salir” que terminará.

while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        print('Hasta luego Lucas')
        break
    print(frase)