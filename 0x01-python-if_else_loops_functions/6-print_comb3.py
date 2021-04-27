#!/usr/bin/python3
aux = 0
for decena in range(10):
    for unidad in range(aux, 10):
        if decena != unidad:
            if decena == 8 and unidad == 9:
                print("{0}{1}".format(decena, unidad))
            else:
                print("{0}{1}".format(decena, unidad), end=", ")
    aux = aux + 1;
