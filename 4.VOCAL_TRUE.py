#!/usr/bin/env python
# -*- coding: utf-8 -*

# Ejercicio No 4

vocal = raw_input("Ingrese una letra:")
def evalue(letra):
    vocales = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']

    if letra in vocales:
       return True
    else:
        return False
print evalue(vocal)