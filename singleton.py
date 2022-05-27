class Singleton(type):
    _instancja = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancja:
            cls._instancja[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instancja[cls]

class Program(metaclass=Singleton):
    pass

prog1 = Program()
prog2 = Program()

print(prog1 is prog2)