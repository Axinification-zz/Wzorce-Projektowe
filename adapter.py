class ElementDocelowy:
    def metodaA():
        print("Wywołano ElementDocelowy MetodaA()")

class Adaptowany:
    def metodaAdaptowanego():
        print("Wywołano MetodaAdaptowanego()")

class Adapter(ElementDocelowy):
    def metodaA():
        Adaptowany.metodaAdaptowanego()

if __name__ == '__main__':
    adapter = Adapter
    print(adapter.metodaA())
    