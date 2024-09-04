# generadores (que son?)

# son estructuras que extraen valores de una funcion y se almacenan en objetos iterables
# que se puden recorrer.

# Estos valores se almacenan de uno en uno.
# Cada vez que un generadore almacena un valor, esta permite en un estado pausado hasta que ...
# que se solicita el siguiente. Esta caracteristica es conocido como suspension de estado.


# limite = int(50)
# def genera_pares(limite):
#     num=1
#     mi_lista =[]
    
#     while num<limite:
#         mi_lista.append(num*2)
        
#         num = num + 1
    
#     return mi_lista

# print(genera_pares(10))


def num_pares(limite):
    num = 1
    
    while num<limite:
    
        yield num*2
        num = num + 1
        
devuelve_pares = num_pares(10)

print(next(devuelve_pares))
print("awuipodria haber mas codigo")

print(next(devuelve_pares))
print(next(devuelve_pares))
