from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Budowniczy(ABC):
    @property
    @abstractmethod
    def produkt(self):
        pass

    @abstractmethod
    def zlozCzescA(self):
        pass

    @abstractmethod
    def zlozCzescB(self):
        pass

class BudowniczyXY(Budowniczy):
    def __init__(self):
        self.reset()

    def reset(self):
        self._produkt = Produkt()

    @property
    def produkt(self) -> Produkt:
        produkt = self._produkt
        self.reset()
        return produkt

    def zlozCzescA(self):
        self._produkt.add("Czesc X")

    def zlozCzescB(self):
        self._produkt.add("Czesc Y")

class BudowniczyQW(Budowniczy):
    def __init__(self):
        self.reset()

    def reset(self):
        self._produkt = Produkt()

    @property
    def produkt(self) -> Produkt:
        produkt = self._produkt
        self.reset()
        return produkt

    def zlozCzescA(self):
        self._produkt.add("Czesc Q")

    def zlozCzescB(self):
        self._produkt.add("Czesc W")

class Produkt():
    def __init__(self):
        self.czesci = []

    def add(self, part: Any):
        self.czesci.append(part)

    def lista_czesci(self):
        print(f"Czesci produktu: {', '.join(self.czesci)}", end="")

class Kierownik:
    def __init__(self):
        self._budowniczy = None

    @property
    def budowniczy(self) -> Budowniczy:
        return self._budowniczy

    @budowniczy.setter
    def budowniczy(self, budowniczy: Budowniczy):
        self._budowniczy = budowniczy

    def skladaj(self):
        self.budowniczy.zlozCzescA()
        self.budowniczy.zlozCzescB()

if __name__ == "__main__":
    kierownik = Kierownik()
    budowniczyxy = BudowniczyXY()
    budowniczyqw = BudowniczyQW()
    kierownik.budowniczy = budowniczyxy
    
    print("\n")
    kierownik.skladaj()
    budowniczyxy.produkt.lista_czesci()
    
    kierownik.budowniczy = budowniczyqw

    print("\n")
    kierownik.skladaj()
    budowniczyqw.produkt.lista_czesci()

