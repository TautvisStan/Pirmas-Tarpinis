import uuid

class Vartotojas():
    def __init__(self, vardas, slaptazodis):
        self.id = uuid.uuid4()
        self.vardas = vardas
        self.slaptazodis = slaptazodis

class Organizatorius(Vartotojas):
    def __init__(self, vardas, slaptazodis):
        super().__init__(vardas, slaptazodis)

class Ziurovas(Vartotojas):
    def __init__(self):
        self.id = uuid.uuid4()