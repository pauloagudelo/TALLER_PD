#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicion No 5

def sum(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

def multip(lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion

n=int(input("cantidad numeros:"))
lista=[]
for i in range(0,n):
    lista.append(int(input("ingrese numero "+str(i+1)+" de la lista: ")))

print "La Suma de los elementos es: " + str(sum(lista))
print "La Multiplicación de los elementos es: " + str(multip(lista))