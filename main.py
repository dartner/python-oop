from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self):
        pass

    def __str__(self):
        return f"{self.jarat_tipus()} | Járatszám: {self.jaratszam}, Célállomás: {self.celallomas}, Jegyár: {self.jegyar} Ft"

class BelfoldiJarat(Jarat):
    def jarat_tipus(self):
        return "Belföldi Járat"

class NemzetkoziJarat(Jarat):
    def jarat_tipus(self):
        return "Nemzetközi Járat"