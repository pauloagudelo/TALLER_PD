#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ejercicio No 6

cont= int(input("Introduce cantidad de listas: "))
p1=[]
p2=[]
for i in range(0,cont):
    p1.append(raw_input("lista No 1: "))

for i in range(0,cont):
    p2.append(raw_input("lista No 2: "))
concide=0;
for i in range(0, cont):
    for y in range(0, cont):
        if(p1[i]==p2[y]):
            concide=concide+1
if concide>=1:
    print "true"
else:
    print "false"
