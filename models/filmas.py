class Filmas():

    reitingai = ["V", "N-7", "N-13", "N-16", "N-18"]

    @classmethod
    def patikrinti_reitinga(cls, reitingas):
        return reitingas in Filmas.reitingai
    
    def __init__(self, pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas):
        if self.patikrinti_reitinga(amziaus_reitingas) is False:
            raise ValueError(f"Nepavyko sukurti filmo! Neteisingai ivestas reitingas: {amziaus_reitingas}. Privalo buti vienas is siu: {Filmas.reitingai}")
        
        self.pavadinimas = pavadinimas
        self.trukme = trukme
        self.zanras = zanras
        self.rezisierius = rezisierius
        self.isleidimo_metai = isleidimo_metai
        self.amziaus_reitingas = amziaus_reitingas

