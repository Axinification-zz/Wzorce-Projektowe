class Jednostka:
    def __init__(self, zycie, doswiadczenie, silaZniszczen):
        self.zycie = zycie
        self.doswiadczenie = doswiadczenie
        self.silaZniszczen = silaZniszczen

    def create(self):
        print(self.__class__.__name__)
        print(self.zycie, self.doswiadczenie, self.silaZniszczen)

class PieszaJednostka(Jednostka):
    pass

class NaziemnaJednostka(Jednostka):
    pass

class PowietrznaJednostka(Jednostka):
    pass

class Strzelec(PieszaJednostka):
    def __init__(self, zycie, doswiadczenie, silaZniszczen):
        self.zycie = zycie
        self.doswiadczenie = doswiadczenie
        self.silaZniszczen = silaZniszczen

class Czolg(NaziemnaJednostka):
    def __init__(self, zycie, doswiadczenie, silaZniszczen):
        self.zycie = zycie
        self.doswiadczenie = doswiadczenie
        self.silaZniszczen = silaZniszczen

class Helikopter(PowietrznaJednostka):
    def __init__(self, zycie, doswiadczenie, silaZniszczen):
        self.zycie = zycie
        self.doswiadczenie = doswiadczenie
        self.silaZniszczen = silaZniszczen

class Fabryka:
    def stworzPieszaJednostke(zycie, doswiadczenie, silaZniszczen):
        return Strzelec(zycie, doswiadczenie, silaZniszczen)
    
    def stworzNaziemnaJednostke(zycie, doswiadczenie, silaZniszczen):
        return Czolg(zycie, doswiadczenie, silaZniszczen)

    def stworzPowietrznaJednostke(zycie, doswiadczenie, silaZniszczen):
        return Helikopter(zycie, doswiadczenie, silaZniszczen)

class NiebieskaFabryka(Fabryka):
    stworzPieszaJednostke = Fabryka.stworzPieszaJednostke(25, 0, 5)
    stworzNaziemnaJednostke = Fabryka.stworzNaziemnaJednostke(100, 0, 25)
    stworzPowietrznaJednostke = Fabryka.stworzPowietrznaJednostke(50, 0 , 25)

class CzerwonaFabryka(Fabryka):
    stworzPieszaJednostke = Fabryka.stworzPieszaJednostke(80, 0, 500)
    stworzNaziemnaJednostke = Fabryka.stworzNaziemnaJednostke(200, 0, 8990)
    stworzPowietrznaJednostke = Fabryka.stworzPowietrznaJednostke(440, 0, 335)

if __name__ == '__main__':
    niebieskaFabryka = NiebieskaFabryka
    czerwonaFabryka = CzerwonaFabryka

    niebieskiStrzelec = niebieskaFabryka.stworzPieszaJednostke
    czerwonyStrzelec = czerwonaFabryka.stworzPieszaJednostke

    niebieskiCzolg = niebieskaFabryka.stworzNaziemnaJednostke
    czerwonyCzolg = czerwonaFabryka.stworzNaziemnaJednostke

    niebieskiHelikopter = niebieskaFabryka.stworzPowietrznaJednostke
    czerwonyHelikopter = czerwonaFabryka.stworzPowietrznaJednostke

    niebieskiStrzelec.create()
    czerwonyStrzelec.create()

    niebieskiCzolg.create()
    czerwonyCzolg.create()

    niebieskiHelikopter.create()
    czerwonyHelikopter.create()


