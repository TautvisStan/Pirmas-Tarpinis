from models.filmas import Filmas
from services import data_handler
from config import filmu_failas

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

def pasalinti_filma_pagal_pav(filmai, pavadinimas):
    rastas = gauti_konkretu_filma_pav(filmai, pavadinimas)
    if rastas is None:
        raise ValueError("Tokio filmo nepavyko rasti! \n")
    else:
        filmai.remove(rastas)
        data_handler.issaugoti_i_faila(filmu_failas, filmai)
        return True
    
def redaguoti_filma(filmas):

    keiciamas = input(f"Iveskite, ka norite redaguoti: 'pavadinimas' 'trukme', 'zanras', 'rezisierius', 'metai', 'amzius' \n")
    match keiciamas:
        case "pavadinimas":
            pass
        case _: 
            raise ValueError("Neteisingai ivestas pasirinkimas!")

    rastas_dict = vars(filmas)
    if keiciamas not in list(rastas_dict.keys()):
        print("Neteisingai ivestas atributas!")
        return
    nauja_verte = input("Iveskite nauja verte: \n")
    tipas = type(rastas_dict[keiciamas])
    rastas_dict[keiciamas] = tipas(nauja_verte)  # TODO: keiciant int, bus str