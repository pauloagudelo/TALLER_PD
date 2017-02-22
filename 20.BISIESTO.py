#!/usr/bin/env python
# -*- coding: utf-8 -*

#ejercicio No 20

a = input("Escriba un año para saber si es bisiesto: ")

def es_bisiesto(a):

    if a % 4 == 0 and (not(a % 100 == 0)):
        print "El año", a, "es un año bisiesto"
    elif a % 400 == 0:
        print "El año", a, "es un año bisiesto"
    else:
        print "El año", a, "no es bisiesto"

print es_bisiesto(a)



