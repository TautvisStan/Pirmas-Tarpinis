import datetime

from models.filmas import Filmas


class Seansas():
    def __init__(self, filmas : Filmas, pradzia, vietos):
        self.filmo_id = filmas.id
        self.pradzia = pradzia
        self.pabaiga = pradzia + datetime.timedelta(minutes=filmas.trukme)
        self.vietos = vietos