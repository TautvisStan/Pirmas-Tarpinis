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
    
def redaguoti_filma(filmas : Filmas):

    keiciamas = input(f"Iveskite, ka norite redaguoti: 'pavadinimas' 'trukme', 'zanras', 'rezisierius', 'metai', 'amzius' \n")
    match keiciamas:
        case "pavadinimas":
            filmas.pavadinimas = input("Iveskite nauja pavadinima: \n")
        case "trume":
            filmas.trukme = data_handler.ivesti_skaiciu("Iveskite nauja trukme: \n")
        case "zanras":
            filmas.zanras = input("Iveskite nauja zanra: \n")
        case "rezisierius":
            filmas.rezisierius = input("Iveskite nauja rezisieriu: \n")
        case "metai":
            filmas.isleidimo_metai = data_handler.ivesti_skaiciu("Iveskite naujus isleidimo metus: \n")
        case "amzius":
            filmas.amziaus_reitingas = input("Iveskite nauja amziaus reitinga: \n")
        case _: 
            raise ValueError("Neteisingai ivestas pasirinkimas!")
    return True