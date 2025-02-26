from models.pardavimas import Pardavimas


def uzregistruoti_pardavima(seansas):
    return Pardavimas(seansas)

def gauti_pardavimus(pardavimai, nuo, iki):
    viso = 0
    filmu_sumos = {}

    for pardavimas in pardavimai:
        if nuo <= pardavimas.data <= iki:
            viso += pardavimas.suma
            filmu_sumos[pardavimas.filmo_id] =  filmu_sumos.get(pardavimas.filmo_id, 0) + pardavimas.suma
    return viso, filmu_sumos