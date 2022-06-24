from abc import ABC, abstractmethod

# TODO Not working

class Iterator(ABC):
    @abstractmethod
    def pierwszy() -> object:
        raise NotImplementedError

    @abstractmethod
    def nastepny() -> object:
        raise NotImplementedError

    @abstractmethod 
    def czyKoniec() -> bool:
        raise NotImplementedError

    @abstractmethod
    def pobierzElement() -> object:
        raise NotImplementedError

class SpecyficznyIterator():
    def __init__(self, kontener):
        self.kontener = kontener
        self.obecny = 0

    def pierwszy(self) -> object:
        return self.kontener[0]

    def nastepny(self) -> object:
        ret: object = None
        if self.obecny < self.kontener.ilosc -1:
            ret = self.kontener[self.obecny + 1]
        return ret

    def pobierzElement(self) -> object:
        return self.kontener[self.obecny]

    def czyKoniec(self) -> bool:
        return self.obecny >= self.kontener.ilosc

class Kontener(ABC):
    @abstractmethod
    def stworzIterator():
        raise NotImplementedError

class SpecyficznyKontener():
    def __init__(self):
        self.elementy = []

    def stworzIterator(self):
        return SpecyficznyIterator

    def getIlosc(self):
        return self.elementy.count()

if __name__ == '__main__':
    kontener = SpecyficznyKontener()
    kontener.elementy.append("Element A")
    kontener.elementy.append("Element B")
    kontener.elementy.append("Element C")
    kontener.elementy.append("Element D")
    iterator = kontener.stworzIterator()
    element = Iterator.pierwszy()

    print("Iteracja kolekcji:")
    while element is not None:
        print(element)
        element = iterator.nastepny()