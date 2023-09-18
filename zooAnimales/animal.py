class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero) -> None:
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1

    @staticmethod
    def totalPorTipo():
        from .mamifero import Mamifero
        from .ave import Ave
        from .reptil import Reptil
        from .pez import Pez
        from .anfibio import Anfibio

        mamiferos = Mamifero.cantidadMamiferos()
        aves = Ave.cantidadAves()
        reptiles = Reptil.cantidadReptiles()
        peces = Pez.cantidadPeces()
        anfibios = Anfibio.cantidadAnfibios()
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

    def toString(self):
        return str(self)

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
