import uuid
class Filmas():

    reitingai = ["V", "N-7", "N-13", "N-16", "N-18"]

    @property
    def amziaus_reitingas(self):
        return self._amziaus_reitingas

    @amziaus_reitingas.setter
    def amziaus_reitingas(self, value):
        if value in Filmas.reitingai:
            self._amziaus_reitingas = value
        else:
             raise ValueError(f"Neteisingai ivestas amziaus reitingas: {value}. Privalo buti vienas is siu: {Filmas.reitingai}")
    
    def __init__(self, pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas):
        self.id = uuid.uuid4()
        self.pavadinimas = pavadinimas
        self.trukme = trukme
        self.zanras = zanras
        self.rezisierius = rezisierius
        self.isleidimo_metai = isleidimo_metai
        self.amziaus_reitingas = amziaus_reitingas

    def __repr__(self):
        return f"Pavadinimas: {self.pavadinimas}, trukme: {self.trukme}, zanras: {self.zanras}, rezisierius: {self.rezisierius}, isleidimo metai: {self.isleidimo_metai},  amziaus reitingas: {self.amziaus_reitingas}"
