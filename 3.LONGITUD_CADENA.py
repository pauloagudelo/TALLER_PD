#!/usr/bin/env python
# -*- coding: utf-8 -*

# Ejercicio No 3

print ("Longitud de una cadena")

cadena = raw_input("ingrese su nombre")
print cadena
def longitud_cadena(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont
print longitud_cadena(cadena)