#!/usr/bin/env python
# -*- coding: utf-8 -*

#ejercicio No 14

factor=int(raw_input("ingrese el numero que desea multiplicar:"))
rango=range(1,11)

for elemento in rango :
    producto=factor * elemento
    print factor, " X ",elemento, " = ", producto
print "Fin Del Programa"