from abc import ABC, abstractmethod

class Przedmiot(ABC):
    @abstractmethod
    def zapytanie():
        raise NotImplementedError

class KonkretnyPrzedmiot(Przedmiot):
    def zapytanie(self):
        print("Wywołanie KonkretnyPrzedmiot.Zapytanie()")

class Pelnomocnik(Przedmiot):
    def __init__(self):
        self.konkretnyPrzedmiot: KonkretnyPrzedmiot = None
    
    def zapytanie(self):
        if self.konkretnyPrzedmiot is None:
            self.konkretnyPrzedmiot = KonkretnyPrzedmiot()
        self.konkretnyPrzedmiot.zapytanie()

if __name__ == '__main__':
    pelnomocnik = Pelnomocnik()
    pelnomocnik.zapytanie()