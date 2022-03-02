# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Variables

a= 3
print(type(a))
a= "hola"
print(type(a))
a =3.5
print(type(a))
a= True
print(type(a))

print('Hola Mundo')
print('Hola Mundo dos')

print("I can't do it")
print('Su nombre es "Diego"')

#Operaciones en esta wea

#suma
a=5
b=2
c= a + b
print(c)

#resta
a=5
b=2
c= a - b
print(c)

#Multiplicacion
a=5
b=2
c= a * b
print(c)

#Division
a=5
b=2
c= a / b
print(c)

#Division parte entera
a=5
b=2
c= a // b
print(c)

#Potencia
a=2
b=6
c= a ** b
print(c)

#Raiz cubica
a=16
b=a ** (1/3)
print(b)

#Raiz cuadrada
import math
raiz = math.sqrt(a)
print(raiz)

# Tipos de datos

# String str

a = "Hola Mundo"
a = 'Hola Mundo'
b = " I can't do it"
c = 'Alias "Diego"'

# Entero int
a = 5

# Decimal float
a = 5.6

# Booleano bool
x = True
y = False

# Conversiones entre tipos de datos

# Convertir de x a entero

a = '3'
b = int(a)
print(type(b))

# Convertir de x a deimal
a = 3
b = float(a)
print(type(b))

# Convertir de x a String
a = 3
b = str(a)
print(type(b))

# Concatenaciones
a = 'hola'
b = 'mundo'
c = a + ' ' + b

a = 'hola'
b = a * 5
print(b)

# Capturar por pantalla
nombre = input('Digite su nombre: ')
print('Hola',nombre, sep='**', end='DIEGO')


nombre = input('Digite su nombre: ')
print('Hola' + nombre)

# Interpolación

nombre = input('Digite su nombre: ')
print(f'Su nombre es {nombre}')


#Algoritmo que sume 2 numeros e imprima su resultado
 
Num1 = int(input('Ingrese numero 1: \n'))
Num2 = int(input('Ingrese numero 2: \n'))
res = Num1 + Num2

print(res)

#Algoritmo que lea un numero y lo eleve al cuadrado

import math
Num1 = int(input('Ingrese numero 1: \n'))
raiz = math.sqrt(Num1)
print(raiz)

valorProducto = int(input('Ingrese el valor del producto: \n'))
Descuento= 0.20
valorAhorrado = valorProducto * Descuento
ValorConDescuento= valorProducto - valorAhorrado
print("El valor inicial es: $", valorProducto)
print("Usted Ahorro: $",valorAhorrado )
print("El valor final es: $",ValorConDescuento )



valorProducto = int(input('Ingrese el valor del producto: \n'))
valorDescuento = int(input('Ingrese de cuanto es el descuento: \n'))
Descuento= valorDescuento / 100
valorAhorrado = valorProducto * Descuento
ValorConDescuento= valorProducto - valorAhorrado
print("El valor inicial es: $", valorProducto)
print("Usted Ahorro: $",valorAhorrado )
print("El valor final es: $",ValorConDescuento )
#Comentario uwu
#Comentario 2 uwu
