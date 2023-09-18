class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero) -> None:
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1

    def movimiento(self):
        return ""

    def totalPorTipo(self):
        mamiferos = 0
        aves = 0
        reptiles = 0
        peces = 0
        anfibios = 0
        return (
            f"Mamiferos: {mamiferos}\nAves: {aves}\nReptiles: {reptiles}\n" + \
                f"Peces: {peces}\nAnfibios:{anfibios}"
        )

    def __str__(self) -> str:
        texto = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, " + \
            f"habito en {self._habitat}, y mi genero es {self._genero}"

        if self._zona is None:
            return texto

        zona = self._zona.getNombre()
        zoo = self._zona.getZoo().getNombre()
        return f"{texto}, la zona en la que me ubico es {zona}, en el {zoo}"

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero
