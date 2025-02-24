from models.filmas import Filmas


def filmu_paieska_pavadinimas(filmai : list[Filmas], paieska : str):
    rasti = []
    for filmas in filmai:
        if paieska in filmas.pavadinimas:
            rasti.append(filmas)
    return rasti

def filmu_paieska_rezisierius(filmai : list[Filmas], paieska : str):
    rasti = []
    for filmas in filmai:
        if paieska in filmas.rezisierius:
            rasti.append(filmas)
    return rasti

def gauti_konkretu_filma_pav(filmai : list[Filmas], pavadinimas : str):
    rastas = None
    for filmas in filmai:
        if filmas.pavadinimas == pavadinimas:
            rastas = filmas
            break
    if rastas is None:
        raise ValueError("Tokio filmo nepavyko rasti!")
    return rastas

def gauti_konkretu_filma_id(filmai : list[Filmas], id):
    rastas = None
    for filmas in filmai:
        
        if filmas.id == id:
            rastas = filmas
            break
    if rastas is None:
        raise ValueError("Tokio filmo nepavyko rasti!")
    return rastas