from abc import ABC, abstractmethod

class Pylek(ABC):
    @abstractmethod
    def przykladowaMetoda(daneZewnetrzne: int):
        raise NotImplementedError

class SpecyficznyPylek(Pylek):
    def przykladowaMetoda(daneZewnetrzne: int):
        print(f"Specyficzny pyłek: {daneZewnetrzne}")

class FabrykaPylkow:
    def __init__(self):
        self.pylki = {}
    
    def fabrykaPylkow(self):
        self.pylki["Q"] = SpecyficznyPylek
        self.pylki["W"] = SpecyficznyPylek
        self.pylki["E"] = SpecyficznyPylek

    def getPylek(self, key: str) -> Pylek:
        return self.pylki[key]

if __name__ == '__main__':
    daneZewnetrzne = 42

    fabryka = FabrykaPylkow()
    fabryka.fabrykaPylkow()

    fq = fabryka.getPylek("Q")
    fq.przykladowaMetoda(daneZewnetrzne-1)

    fw = fabryka.getPylek("W")
    fw.przykladowaMetoda(daneZewnetrzne-2)

    fe = fabryka.getPylek("E")
    fe.przykladowaMetoda(daneZewnetrzne-3)
