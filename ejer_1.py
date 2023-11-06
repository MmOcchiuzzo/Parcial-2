from collections import defaultdict

nombre_tree = defaultdict(list)
numero_tree = {}
tipo_tree = defaultdict(list)

pokemon_data = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["planta", "veneno"]},
    {"nombre": "Lycanroc", "numero": 745, "tipo": ["roca"]},
    {"nombre": "Jolteon", "numero": 135, "tipo": ["eléctrico"]},
    {"nombre": "Ivysaur", "numero": 2, "tipo": ["planta", "veneno"]},
    {"nombre": "Tyrantrum", "numero": 697, "tipo": ["roca", "dragón"]},
    {"nombre": "Blaziken", "numero": 257, "tipo": ["fuego", "lucha"]},
    {"nombre": "Steelix", "numero": 208, "tipo": ["acero", "tierra"]},
    {"nombre": "Empoleon", "numero": 395, "tipo": ["agua", "acero"]},
    {"nombre": "Shaymin", "numero": 492, "tipo": ["planta"]},
    {"nombre": "Palpitoad", "numero": 536, "tipo": ["agua", "tierra"]},
    {"nombre": "Dusknoir", "numero": 477, "tipo": ["fantasma"]},
    {"nombre": "Luxray", "numero": 405, "tipo": ["electrico"]},
    {"nombre": "Roserade", "numero": 407, "tipo": ["planta", "veneno"]},
    {"nombre": "Metagross", "numero": 376, "tipo": ["acero", "psiquico"]},
    {"nombre": "Hitmonchan", "numero": 107, "tipo": ["lucha"]},
]
#a
for pokemon in pokemon_data:
   
    for i in range(len(pokemon["nombre"])):
        substring = pokemon["nombre"][:i + 1].lower()
        nombre_tree[substring].append(pokemon)

    numero_tree[pokemon["numero"]] = pokemon

    for tipo in pokemon["tipo"]:
        tipo_tree[tipo].append(pokemon)
#b
def buscar_pokemon_nombre(nombre):
    nombre = nombre.lower()
    return [pokemon for key, pokemons in nombre_tree.items() if nombre in key for pokemon in pokemons]

def buscar_pokemon_numero(numero):
    return numero_tree.get(numero)

pokemon_por_nombre = buscar_pokemon_nombre("bul") 
pokemon_por_numero = buscar_pokemon_numero(135)   
#c
nombres_tipo_agua = [pokemon["nombre"] for pokemon in tipo_tree["agua"]]
nombres_tipo_fuego = [pokemon["nombre"] for pokemon in tipo_tree["fuego"]]
nombres_tipo_planta = [pokemon["nombre"] for pokemon in tipo_tree["planta"]]
nombres_tipo_electrico = [pokemon["nombre"] for pokemon in tipo_tree["eléctrico"]]

print(nombres_tipo_agua)
print(nombres_tipo_fuego)
print(nombres_tipo_planta)
print(nombres_tipo_electrico)
#d
pokemon_orden_numero = sorted(pokemon_data, key=lambda x: x["numero"])
pokemon_orden_nombre = sorted(pokemon_data, key=lambda x: x["nombre"])
pokemon_orden_nivel_nombre = sorted(pokemon_data, key=lambda x: (len(x["nombre"]), x["nombre"]))

print("Listado en orden ascendente por número:")
for pokemon in pokemon_orden_numero:
    print(f'{pokemon["numero"]}: {pokemon["nombre"]}')

print("\nListado en orden ascendente por nombre:")
for pokemon in pokemon_orden_nombre:
    print(f'{pokemon["nombre"]}: {pokemon["numero"]}')

print("\nListado por nivel por nombre:")
for pokemon in pokemon_orden_nivel_nombre:
    print(f'{len(pokemon["nombre"])}: {pokemon["nombre"]} ({pokemon["numero"]})')
#e
jolteon_data = buscar_pokemon_nombre("Jolteon")
lycanroc_data = buscar_pokemon_nombre("Lycanroc")
tyrantrum_data = buscar_pokemon_nombre("Tyrantrum")

print(jolteon_data)
print(lycanroc_data)
print(tyrantrum_data)
#f
cantidad_tipo_electrico = len(tipo_tree["eléctrico"])
cantidad_tipo_acero = len(tipo_tree["acero"])

print("Cantidad de Pokémons de tipo eléctrico:", cantidad_tipo_electrico)
print("Cantidad de Pokémons de tipo acero:", cantidad_tipo_acero)
