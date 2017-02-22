#! /usr/bin/env python
# -*- coding: utf-8 -*-

#ejercicio No 9

a= int(input("Ingrese un numero entero: "))
b= raw_input("Ingrese un caracter: ")
def genera_n_caracteres(cant,car):
    ncar=""
    for i in range(0,cant):
        ncar=ncar+car
    return ncar

print genera_n_caracteres(a,b)