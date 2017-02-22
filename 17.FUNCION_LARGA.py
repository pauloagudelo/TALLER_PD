#!/usr/bin/env python
# -*- coding: utf-8 -*

# Ejercicio No 17

frase=int(input("Ingrese cantidad de palabras: "))
palabras=[]
for i in range(0,frase):
    palabras.append(raw_input("Palabra "+str(i+1)+": "))

def mas_larga(lista):
    mayor=len(lista[0])
    maslarga=lista[0]
    for palabra in lista:
        if mayor <= len(palabra):
            mayor=len(palabra)
            maslarga = palabra
        else:
            maslarga=maslarga
    return maslarga

print "la palabra mas larga es: "+mas_larga(palabras)