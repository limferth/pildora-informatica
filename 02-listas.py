# LISTAS 
# Que son las LISTAS O ARRAYS
# estructura de datos que nos permite almacenar gran cantidad de valores

#SINTAXIS

#nombre_lista = [elem1, elem2];

mi_lista = ["maria", "martha", "Antonio", "pepe"];


mi_lista.extend(["Sandrita", "Ana", "Luicia"])

mi_lista.remove("pepe");

#mi_lista.pop("pepe"); # elimina la ultima en la lista
#mi_lista.insert(2,"Sandra")
#mi_lista.append("Sandra")
#print(mi_lista[:]) # para acceder y mostrar todos los parametros

print(mi_lista[:]); #para llamar en especifico

print(mi_lista.index("Ana"));

print("maria" in mi_lista);

miLista = ["mario", 5, True, 78.35]

miLista2 = ["Sandrota", "Luciota"];

miLista3 = miLista + miLista2

print(miLista3[:]);
