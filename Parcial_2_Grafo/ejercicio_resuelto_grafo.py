from grafo import Grafo


g = Grafo(dirigido=False)


g.insertar_vertice('Luke Skywalker', datos={})
g.insertar_vertice('Darth Vader', datos={})
g.insertar_vertice('Yoda', datos={})
g.insertar_vertice('Boba Fett', datos={})

g.insertar_vertice('C 3PO', datos={})
g.insertar_vertice('Leia', datos={})
g.insertar_vertice('Rey', datos={})
g.insertar_vertice('Kylo Ren', datos={})

g.insertar_vertice('Chewbacca', datos={})
g.insertar_vertice('Han Solo', datos={})
g.insertar_vertice('R2 D2', datos={})

g.insertar_vertice('Obi Wan kenobi', datos={})
g.insertar_vertice('BB 8', datos={})



#aristas
g.insertar_arista('Luke Skywalker', 'Darth Vader', 6)
g.insertar_arista('Luke Skywalker', 'Yoda', 3)
g.insertar_arista('Luke Skywalker', 'Boba Fett', 2)

g.insertar_arista('Darth Vader', 'Boba Fett', 3)

g.insertar_arista('Yoda', 'Boba Fett', 2)

g.insertar_arista('C 3PO', 'Leia', 6)
g.insertar_arista('C 3PO', 'Rey', 3)
g.insertar_arista('C 3PO', 'Kylo Ren', 2)

g.insertar_arista('Leia', 'Rey', 6)
g.insertar_arista('Leia', 'Kylo Ren', 3)

g.insertar_arista('Rey', 'Kylo Ren', 1)

g.insertar_arista('Chewbacca', 'Leia', 6)
g.insertar_arista('Chewbacca', 'Han Solo', 3)
g.insertar_arista('Chewbacca', 'R2 D2', 1)
g.insertar_arista('Chewbacca', 'C 3PO', 4)

g.insertar_arista('Han Solo', 'Yoda', 3)
g.insertar_arista('Han Solo', 'Kylo Ren', 2)

g.insertar_arista('R2 D2', 'Kylo Ren', 11)

g.insertar_arista('BB 8', 'Yoda', 11)

g.insertar_arista('Obi Wan kenobi', 'Yoda', 11)

print('''
b. hallar el árbol de expansión mínimo desde el vértice que contiene a C 3PO, Yoda y la princesa Leia;
''')

arbol_min = g.kruskal()
print('Arbol de expansion minima:')
print(arbol_min)

arbol_min = arbol_min[0].split('-')
#peso_total = 0
#for nodo in arbol_min:
    #nodo = nodo.split(';')
    #peso_total += int(nodo[2])
    #print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')


print(
'''
c. determinar cuales personajes comparten con otro dos episodios o mas (mostrar el par de pesonajes);
'''
)
#g.mostrar_todos_los_personajes_con_sus_adyacentes()
g.cuales_personajes_comparten_con_otro_dos_episodios_o_mas()


print('''
e. determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los personajes.
''')

print(
g.personaje_que_a_compartido_episodio_con_la_mayor_cantidad_del_resto_de_los_personajes()
)