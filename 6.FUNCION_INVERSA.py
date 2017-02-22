#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ejercicion No 6
texto = raw_input("Ingrese cadena: ")
def inversa (cadena):
    invertida = []
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida
print inversa(texto)