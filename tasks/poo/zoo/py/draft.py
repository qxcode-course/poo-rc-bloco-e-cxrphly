class Animal:
    def __init__(self, name:str):
        self.name = name
    
    def apresentar_animal(self):
        return f"Eu sou um(a) {self.name}"
    
    def fazer_som(self):
        pass
    def mover(self):
        pass

class Leao(Animal):
    def __init__(self, name:str):
        super().__init__(name)

    def fazer_som(self):
        print("Roooar")

    def mover(self):
        pass

class Elefante(Animal):

    def __init__(sefl, name:str):
        super().__init__(name)

    def fazer_som(self):
        print("PRRRR")
    def mover(self):
        pass

class Cobra(Animal):
    def __init__(self, name):
        super().__init__(name)
    def fazer_som(self):
        print("ssssssss")
    def mover(self):
        pass

def apresentar(animal:Animal):
    animal.apresentar_animal()
    animal.fazer_som()
    animal.mover()
    print("Tipo Objeto = ", type(animal).__name__)


animais = [
    Leao("Lion"),
    Cobra("Snake"),
    Elefante("Dumbo")
]

for animal in animais:
    apresentar(animal)