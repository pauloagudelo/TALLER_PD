#! /usr/bin/env python
# -*- coding: utf-8 -*-

#ejercicio No 7

texto = raw_input("Ingrese palabra: ")
def palindromo(palabra):
    x = []
    y = []
    cuenta=len(palabra)
    for i in range(0,len(palabra)):
        cuentas = cuenta - i
        cuentas = cuentas - 1
        x.append(palabra[cuentas])
        y.append(palabra[i])
    if (x==y):
        return "Palindromo"
    else:
        return "no es palindromo"
print palindromo(texto)
