
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
# introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

""" 
password='8314A'
codigo=input('Introduce el codigo:')
if(password.lower()==codigo.lower()):
    print('Contraseña correcta')
else:
    print('Contraseña incorrecta')
 """
 
 # Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
 # Si el divisor es cero el programa debe mostrar un error.
 
""" num1 = int(input('Introduce un numero1: '))
num2 = int(input('Introduce un numero2: '))

if num2==0:
    print('Error: No se puede dividir por 0.')
else:
    print(num1/num2) """
    

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

""" number = int(input('Introduce un numero: '))

if number%2==0:
    print('El numero es par')
else:
    print('El numero es impar') """
    
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N 
# y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

""" name = input('Introduce tu nombre: ')
sex = input('Introduce tu sexo (M - H):')

if sex=='M':
    if name[0].lower() < 'm':
        group = 'A'
    else:
        group='B'

if sex == 'H':
    if name.lower() > 'n':
        group = 'A'
    else:
        group='B'
print('Tu grupo es el ', group)
 """
 
""" name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if (gender == "M" and name.lower() < 'm') or (gender == "H" and name.lower() > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group) """


# Los tramos impositivos para la declaración de la renta en un
# determinado país son los siguientes:
"""
Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por 
pantalla el tipo impositivo que le corresponde. """


""" # Preguntar al usuario por la renta
renta = float(input("¿Cuál es tu renta anual? "))
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
# Mostrar por pantalla el producto de la renta por el tipo impositivo
print("Tienes que pagar ", renta * tipo / 100, "€", sep='') """

# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

# Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")