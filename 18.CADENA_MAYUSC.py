#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Ejercicio No 18

palabra=raw_input("Ingrese Palabra: ")
c_mayusculas="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cont=0

for i in palabra:
     if i in c_mayusculas:
       cont=cont+1
print cont

print ("La cadena tiene", cont, "mayusculas")