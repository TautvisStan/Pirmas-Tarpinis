from models.filmas import Filmas
from models.vartotojas import Vartotojas

class Ivertinimas():
    def __init__(self, reitingas, atsiliepimas, filmas : Filmas, vartotojas : Vartotojas):
        self.filmo_id = filmas.id
        self.vartotojo_id = vartotojas.id
        self.reitingas = reitingas
        self.atsiliepimas = atsiliepimas

    def __repr__(self) -> str:
        return f"Ivertinimas: {self.reitingas}. Atsiliepimas: {self.atsiliepimas}"