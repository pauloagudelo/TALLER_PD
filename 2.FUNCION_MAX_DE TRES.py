#!/usr/bin/env python
# -*- coding: utf-8 -*

#ejercicio No 2

x = int(input("Digite el primer numero: "))
y = int(input("Digite el segundo numero: "))
z = int(input("Digite el tercer numero: "))

if x>y and x>z:
    print ("el numero mayor es:", x)
elif y>x and y>z:
            print ("el numero mayor es:", y)
elif z>x and z>y:
            print ("el numero mayor es:", z)
else:
    print "los numero digitados son iguales"