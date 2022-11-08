from arbol import (
    nodoArbol,
    insertar_nodo,
    inorden_villano,
    inorden_empieza_con,
    contar_heroes,
    eliminar_nodo,
    inorden,
    postorden_heroes,
    crear_bosque,
    arbol_vacio,
    contar_heroes_villanos,
    busqueda,
    por_nivel,
    preorden,
)

arbol = nodoArbol()


#heroes = nodoArbol()
#villanos = nodoArbol()


lista = [
    ['Yoda', 1.60, 40],
    ['Mandalorian', 1.60, 60],
    ['Luke Skywalker', 1.60, 70],
    ['Grogu', 0.89, 60],
    ['mace windu', 1.89, 60],
    ['quinlan vos', 1.67, 60],
    ['darth vader', 1.68, 60],
    ['plo koon', 1.70, 60],
    ['saesee tiin', 1.60, 60],
    ['yaddle', 1.89, 60],
    ['even pieli', 1.89, 60],
    ['oppo rancisis', 1.89, 60],
    ['adi gallia', 1.89, 60],
    ['yarael poof', 1.89, 60],
    ['eeth koth', 1.70, 60],
    ['depa billaba', 1.40, 50],
    ['kit fisto', 1.35, 65],
    ['luminara unduli', 1.25, 50],
    ['barriss offee', 1.60, 40],
    ['shaak ti', 1.70, 60],
    ['coleman trebor', 1.70, 60],
]

for nombre, altura, peso in lista:
    datos = {'altura': altura,
             'peso': peso}
    
    insertar_nodo(arbol, nombre, datos)



print('''
a. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
''')
#agregar un personaaje
nombre = input('Ingrese el nombre del nuevo personaje:')
altura = float(input('Ingrese el altura del nuevo personaje:'))
peso = int(input('Ingrese el peso del nuevo personaje:'))
datos = {'altura': altura,
             'peso': peso}
insertar_nodo(arbol, nombre, datos)

#modificar un personaje
print()
clave = input('ingrese el nombre del personaje que desea modificar:')
pos = eliminar_nodo(arbol, clave)

#print(pos)
if pos[0] is not None:
    nombre = input('ingrese su nuevo nombre:')
    altura = float(input('Ingrese su nueva altura:'))
    peso = int(input('Ingrese su nuevo peso:'))
    datos = {'altura': altura,
             'peso': peso}
    insertar_nodo(arbol, nombre, datos)
else:
    print('valor no encontrado en el arbol')

#eliminar un personaje
print()
clave = input('ingrese el nombre del personaje que desea eliminar:')
pos = eliminar_nodo(arbol, clave)
if pos[0] is not None:
    print('el personaje',clave,'fue eliminado')
else:
    print('el personaje',clave,'no fue eliminado ya que no se encontro en el arbol')

inorden(arbol)
print()

print('''
b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker
''')

print()
pos = busqueda(arbol, 'Yoda')
print(pos['info'],pos['datos'])

print()
pos = busqueda(arbol, 'Mandalorian')
print(pos['info'],pos['datos'])

print()
pos = busqueda(arbol, 'Luke Skywalker')
print(pos['info'],pos['datos'])

print('''
c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;
''')
#inorden(arbol)
def listar_personaje_que_miden_menos_de_x_metros(arbol,altura):
    if(arbol is not None):
        listar_personaje_que_miden_menos_de_x_metros(arbol['izq'],altura)
        if arbol['datos']['altura'] < altura:
            print(arbol['info'])
        listar_personaje_que_miden_menos_de_x_metros(arbol['der'],altura)

listar_personaje_que_miden_menos_de_x_metros(arbol,0.9)


print('''
d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;
''')

def listar_personaje_que_pesan_menos_de_x_kilos(arbol,peso):
    if(arbol is not None):
        listar_personaje_que_pesan_menos_de_x_kilos(arbol['izq'],peso)
        if arbol['datos']['peso'] < peso:
            print(arbol['info'])
        listar_personaje_que_pesan_menos_de_x_kilos(arbol['der'],peso)

listar_personaje_que_pesan_menos_de_x_kilos(arbol,75)

print('''
e. mostrar un listado por nivel de los personajes del árbol;
''')
por_nivel(arbol)

print(
'''
f. determinar si Grogu esta en el árbol y responder lo siguiente:
''')
clave='Grogu'
pos = busqueda(arbol, clave)

#print(pos)
if pos is not None:
    print(clave,'esta en el arbol')
    print('mostrar toda su información;')
    print(pos['info'],pos['datos'])
    print('en que tipo de nodo esta (hoja, intermedio o raíz);')
    if(pos['altura'] == 0):
        print('esta en un nodo hoja')
    elif(arbol['altura'] == pos['altura']):
        print('esta en un nodo raiz')
    else:
        print('esta en un nodo intermedio')
    
    print('que altura tiene el nodo dentro del árbol.')
    print('la altura del nodo es:',pos['altura'])
else:
    print(clave,'no esta en el arbol')


#preorden(arbol)