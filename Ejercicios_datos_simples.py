"""
Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre 
en pantalla la suma de todos los enteros desde 1 hasta n. 
"""

n = int(input("Introduce un numero entero: "))

def sumatoria(n):
    result=0
    for i in range(1,n+1):
        result+=i
    return result

print(f'La suma de los {n} primeros numeros es : {sumatoria(n)}')

def sumatoria2(n):
    result=int((n*(n+1))/2)
    
    return result

print('La suma de los', n, 'primeros números es:', sumatoria2(n))


"""
Escribir un programa que pida al usuario su peso (en kg) 
y estatura (en metros), calcule el índice de masa corporal 
y lo almacene en una variable, e imprima por pantalla la frase 
Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal 
calculado redondeado con dos decimales.
"""

peso = float(input("¿Cuál es tu peso en kg? "))
estatura = float(input("¿Cuál es tu estatura en metros?"))
imc = round(peso/estatura**2,2)
print("Tu índice de masa corporal es " + str(imc))

"""
Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión.
"""


cantidad = float(input('Introduce el capital a invertir: '))
interes = float(input('Introduce el interes anual: '))
anios = int(input('Introduce el número de años: '))

def rentabilidad(cap, int, anios):
    
    cap=cap * (int / 100 + 1) ** anios
    
    """ for i in range(1, anios+1):
        cap = cap + cap*int/100 """
        
    return round(cap, 2)

print(rentabilidad(cantidad, interes, anios))   

