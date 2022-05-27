class Jednostka:
    def __init__(self, zycie, doswiadczenie, silaZniszczen):
        self.zycie = zycie
        self.doswiadczenie = doswiadczenie
        self.silaZniszczen = silaZniszczen
    
    def create(self):
        print(self.__class__.__name__)
        print(self.zycie, self.doswiadczenie, self.silaZniszczen)
        

class Strzelec(Jednostka):
    def __init__(self):
        self.zycie = 25
        self.doswiadczenie = 0
        self.silaZniszczen = 10

class Czolg(Jednostka):
    def __init__(self):
        self.zycie = 100
        self.doswiadczenie = 0
        self.silaZniszczen = 20

def fabryka(jednostka=""):
    jednostki = {
        "Strzelec": Strzelec,
        "Czolg": Czolg
    }

    return jednostki[jednostka]()

if __name__ == '__main__':
    strzelec = fabryka("Strzelec")
    czolg = fabryka("Czolg")

    print(strzelec.create())
    print(czolg.create())