import datetime


class Seansas():
    def __init__(self, filmas, pradzia):
        self.filmo_id = filmas.id
        self.pradzia = pradzia
        self.pabaiga = pradzia + datetime.timedelta(minutes=filmas.minutes)