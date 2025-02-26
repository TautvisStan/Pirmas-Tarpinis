from datetime import datetime
class Pardavimas():
    def __init__(self, seansas) -> None:
        self.suma = seansas.kaina
        self.data = datetime.now()
        self.filmo_id = seansas.filmo_id