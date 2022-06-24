class Element:
    def __init__(self, *args):
        self.position = args[0]

    def pokaz(self):
        print("\t", end ="")
        print(self.position)

class Kompozyt:
    def __init__(self, *args):
        self.position = args[0]
        self.children = []

    def dodaj(self, child):
        self.children.append(child)

    def usun(self, child):
        self.children.remove(child)

    def pokaz(self):
        print(self.position)
        for _ in self.children:
            print("\t", end ="")
            _.pokaz()

if __name__ == "__main__":
    root = Kompozyt("root")
    comp1 = Kompozyt("Kompozyt X")
    comp2 = Kompozyt("Kompozyt Y")

    root.dodaj(Element("Lisc A"))
    root.dodaj(Element("Lisc B"))
    comp1.dodaj(Element("Lisc XA"))
    comp1.dodaj(Element("Lisc XB"))

    root.dodaj(comp1)
    root.dodaj(comp2)

    root.pokaz()