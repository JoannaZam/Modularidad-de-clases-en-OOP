# misterio.py
class Misterio:
    def __init__(self, nombre):
        self.__nombre = nombre

    def resolver(self):
        print(f"El jugador {self.__nombre} está resolviendo el misterio.")
