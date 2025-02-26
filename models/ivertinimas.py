from models.filmas import Filmas
from models.vartotojas import Vartotojas

class Ivertinimas():
    @property
    def ivertinimas(self):
        return self._ivertinimas

    @ivertinimas.setter
    def ivertinimas(self, value):
        if value in range(1, 10+1):
            self._ivertinimas = value
        else:
             raise ValueError(f"Neteisingai ivestas ivertinimas: {value}. Privalo buti 1-10!")

    def __init__(self, reitingas, atsiliepimas, filmas : Filmas, vartotojas : Vartotojas):
        self.filmo_id = filmas.id
        self.vartotojo_id = vartotojas.id
        self.reitingas = reitingas
        self.atsiliepimas = atsiliepimas

    def __repr__(self) -> str:
        return f"Ivertinimas: {self.reitingas}. Atsiliepimas: {self.atsiliepimas}"