from abc import ABC, abstractmethod
import copy

class Prototyp(ABC):
    def __init__(self):
        self.id = None

    def set_id(self, id):
        self.id = id

    @abstractmethod
    def klonuj(self):
        pass

class PrototypX(Prototyp):
    def __init__(self):
        super().__init__()

    def klonuj(self):
        return copy.deepcopy(self)


class PrototypY(Prototyp):
    def __init__(self):
        super().__init__()
    
    def klonuj(self):
        return copy.copy(self)

prototypx = PrototypX()
prototypx.set_id("I")
klonx = prototypx.klonuj()

prototypy = PrototypY()
prototypy.set_id("II")
klony = prototypy.klonuj()

print(f"Id klona X: {klonx.id}, Id klona Y: {klony.id}")

