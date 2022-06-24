from abc import ABC, abstractmethod

class KlasaAbstrakcyjna(ABC):
    @abstractmethod
    def zrobCos(self):
        pass

    @abstractmethod
    def jakasInnaMetoda(self):
        pass

    def metodaSzablonowa(self):
        self.zrobCos()
        self.jakasInnaMetoda()
        print("")

class SpecyficznaKlasaA(KlasaAbstrakcyjna):
    def zrobCos(self):
        print("SpecyficznaKlasaA.zrobCos()")
    def jakasInnaMetoda(self):
        print("SpecyficznaKlasaA.jakasInnaMetoda()")

class SpecyficznaKlasaB(KlasaAbstrakcyjna):
    def zrobCos(self):
        print("SpecyficznaKlasaB.zrobCos()")
    def jakasInnaMetoda(self):
        print("SpecyficznaKlasaB.jakasInnaMetoda()")

def call(klasa_abstrakcyjna: KlasaAbstrakcyjna):
    klasa_abstrakcyjna.metodaSzablonowa()

if __name__ == '__main__':
    call(SpecyficznaKlasaA())
    call(SpecyficznaKlasaB())
