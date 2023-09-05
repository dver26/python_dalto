# creando una lista (mutable)
lista = ["Lucas Dalto", "SoyDalto", True, 1.85]
print(lista[1]) # SoyDalto

# creando una tupla (inmutable)
tupla = ("Lucas Dalto", "SoyDalto", True, 1.85)
print(tupla[1])

# modificamos la lista
lista[3] = "Maquinola"

# creando un conjunto o set
conjunto = {"Lucas Dalto", "SoyDalto", True, 1.85}
print(conjunto) 

# creando un diccionario (dict)
diccionario = {
  'nombre': 'Lucas Dalto',
  'canal' : 'Soy dalto',
  'esta_emocionado' : True,
  'altura' : 1.84,
  'dato_duplicado' : 'Soy Dalto'
}
print(diccionario['nombre'])
print(lista[3])