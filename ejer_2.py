class Arista:
    def __init__(self, vertice, peso):
        self.vertice = vertice
        self.peso = peso

    def __str__(self):
        return f"{self.vertice} {self.peso}"

class ListaArista:
    def __init__(self):
        self.__elements = []

    def insert(self, value):
        self.__elements.append(value)

    def delete(self, value):
        if value in self.__elements:
            self.__elements.remove(value)

    def size(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value)

    def get_element_by_index(self, index):
        return self.__elements[index] if 0 <= index < len(self.__elements) else None

class Grafo:
    def __init__(self):
        self.vertices = {}

    def insert_vertice(self, value, criterio=None):
        if value not in self.vertices:
            self.vertices[value] = ListaArista()

    def insert_arista(self, vertice_ori, vertice_des, peso, criterio_vertice=None, criterio_arista='vertice'):
        if vertice_ori in self.vertices and vertice_des in self.vertices:
            self.vertices[vertice_ori].insert(Arista(vertice_des, peso))
            self.vertices[vertice_des].insert(Arista(vertice_ori, peso))

    def search_vertice(self, search_value, criterio=None):
        return search_value if search_value in self.vertices else None

    def obtener_aristas(self):
        aristas = []
        for personaje, lista_aristas in self.vertices.items():
            for arista in lista_aristas.__elements:
                aristas.append((personaje, arista.vertice, arista.peso))
        return aristas

    def arbol_expansion_minima(self):
        arbol_expansion = set()
        visitados = set()
        vertices = list(self.vertices.keys())
        if not vertices:
            return arbol_expansion

        visitados.add(vertices[0])

        while len(visitados) != len(vertices):
            min_episodios = float('inf')
            min_arista = None
            for personaje in visitados:
                for arista in self.vertices[personaje].__elements:
                    vecino = arista.vertice
                    episodios = arista.peso
                    if vecino not in visitados and episodios < min_episodios:
                        min_episodios = episodios
                        min_arista = (personaje, vecino, episodios)
            if min_arista:
                arbol_expansion.add(min_arista[:2])
                visitados.add(min_arista[1])

        return arbol_expansion

    def contiene_yoda(self):
        arbol_expansion = self.arbol_expansion_minima()
        for arista in arbol_expansion:
            if 'Yoda' in arista:
                return True
        return False

    def numero_max_episodios_compartidos(self):
        max_episodios = 0
        for personaje, lista_aristas in self.vertices.items():
            for arista in lista_aristas.__elements:
                if arista.peso > max_episodios:
                    max_episodios = arista.peso
        return max_episodios

grafo_sw = Grafo()

personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO",
    "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

for personaje in personajes:
    grafo_sw.insert_vertice(personaje)

relaciones = {
    ("Luke Skywalker", "Yoda"): 5,
    ("Luke Skywalker", "Leia"): 7,
    ("Leia", "Han Solo"): 4,
    ("Luke Skywalker", "Darth Vader"): 4,
    ("Luke Skywalker", "Leia"): 7,
    ("Leia", "Han Solo"): 5,
    ("Rey", "Kylo Ren"): 6,
    ("Chewbacca", "Han Solo"): 4,
    ("R2-D2", "C-3PO"): 8,
    ("R2-D2", "BB-8"): 3,
}

for relacion, episodios in relaciones.items():
    grafo_sw.insert_arista(relacion[0], relacion[1], episodios)

print("Árbol de expansión mínima:", grafo_sw.arbol_expansion_minima())
print("¿Contiene a Yoda?", grafo_sw.contiene_yoda())
print("Número máximo de episodios compartidos:", grafo_sw.numero_max_episodios_compartidos())


