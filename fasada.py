class PodSystemPierwszy:
    def metodaPierwsza():
        print("PodSystemPierwszy Metoda")

class PodSystemDrugi:
    def metodaDruga():
        print("PodSystemDrugi Metoda")

class PodSystemTrzeci:
    def metodaTrzecia():
        print("PodSystemTrzeci Metoda")

class PodSystemCzwarty:
    def metodaCzwarta():
        print("PodSystemCzwarty Metoda")

class Fasada():
    def __init__(self) -> None:
        self.pierwszy = PodSystemPierwszy
        self.drugi = PodSystemDrugi
        self.trzeci = PodSystemTrzeci
        self.czwarty = PodSystemCzwarty

    def metodaA(self):
        print("Metoda A")
        self.pierwszy.metodaPierwsza()
        self.drugi.metodaDruga()
        self.czwarty.metodaCzwarta()

    def metodaB(self):
        print("Metoda B")
        self.drugi.metodaDruga()
        self.trzeci.metodaTrzecia()

if __name__ == '__main__':
    fasada = Fasada()

    fasada.metodaA()
    fasada.metodaB()