from abc import ABC, abstractmethod

class Implementacja(ABC):
    @abstractmethod
    def metodaImplementacji():
        raise NotImplementedError

class Abstrakcja:
    def __init__(self, implementacja: Implementacja) -> None:
        self.implementacja = implementacja

    def setImplementacja(self, value):
        self.implementacja = value

    def metodaImplementacji(self):
        self.implementacja.metodaImplementacji()

class AbstrakcjaPochodna(Abstrakcja):
    def metodaImplementacji(self):
        self.implementacja.metodaImplementacji()

class SpecyficznaImplementacja(Implementacja):
    def metodaImplementacji():
        print("SpecyficznaImplementacja MetodaImplementacji")

class jakasInnaImplementacja(Implementacja):
    def metodaImplementacji():
        print("JakasInnaImplementacja MetodaImplementacji")

if __name__=='__main__':
    ab = AbstrakcjaPochodna(Abstrakcja)

    ab.setImplementacja(SpecyficznaImplementacja)
    ab.metodaImplementacji()

    ab.setImplementacja(jakasInnaImplementacja)
    ab.metodaImplementacji()