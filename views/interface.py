from models.vartotojas import Organizatorius, Ziurovas
from services import rezervacija_service
import services.data_handler as data_handler
from config import filmu_failas, seansu_failas
import services.filmas_service as filmas_service
import services.seansas_service as seansas_service

from collections import namedtuple
# from enum import Enum



# class Organizatoriaus_Veiksmai(Enum):
#     prideti_filma = 1
#     atspausdinti_filmus = 2
#     ieskoti_filmu = 3
#     pasalinti_filma = 4
#     redaguoti_filma = 5
#     prideti_seansa = 6
#     rodyti_seansus = 7
#     rezervuoti_seansa = 8


# alias = {
#     '1': 'id1',
#     '2': 'id1',
#     '3': 'id2',
#     '4': 'id2'
# }

# dictionary = {
#     'id1': 1,
#     'id2': 2
# }

# dictionary[alias['a']]
def sukti_menu(filmai, seansai, vartotojai):
    Veiksmas = namedtuple("Veiksmas", ("pav", "funkcija"))
    visi_veiksmai = [
        Veiksmas("Iseiti", None), #TODO: iseiti is programos????
        Veiksmas("Prideti filma", lambda: prideti_filma(filmai)), # 1
        Veiksmas("Atspausdinti filmus", lambda: atspausdinti_filmus(filmai)), # 2
        Veiksmas("Ieskoti filmu", lambda: ieskoti_filmu(filmai)), #3
        Veiksmas("Pasalinti filma", lambda: pasalinti_filma(filmai)), #4
        Veiksmas("Redaguoti filma", lambda: redaguoti_filma(filmai)), #5
        Veiksmas("Prideti seansa", lambda: prideti_seansa(filmai,seansai)), #6
        Veiksmas("Rodyti seansus", lambda: rodyti_seansus(filmai, seansai)), #7
        Veiksmas("Rezervuoti seansa", lambda: rezervuoti_seansa(filmai, seansai)) # 8

    ]
    prisijunges = None
    while prisijunges is None:
        prisijunges = prisijungti(vartotojai)
    


    # organizatoriaus_veiksmai = [
    #     Veiksmas("1. Prideti filma", prideti_filma(filmai))
    # ]

    org_veiksmai = [0, 1, 2, 3, 4, 5, 6, 7]
    vart_veiksmai = [0, 2, 3, 7, 8]
    # veiksmas = veiksmai[org_veiksmai[indeksas]]
    if isinstance(prisijunges, Ziurovas):
        print("ziur")
        veiksmai = vart_veiksmai
    else:
        veiksmai = org_veiksmai
        print("org")
    while True:
        try:
            print("Galimi veiksmai: \n")
            for i, sk in enumerate(veiksmai, 0):
                print(f"{i}: {visi_veiksmai[sk].pav}")
            pasirinktas = int(input("Iveskite veiksma: \n")) #TODO: int patik
            if pasirinktas in range(len(veiksmai)) and pasirinktas != 0:
                visi_veiksmai[veiksmai[pasirinktas]].funkcija()
            elif pasirinktas == 0:
                return
            else:
                print("Neteisingai pasirinktas veiksmas!")
        except Exception as e:
            print("Ivyko klaida!")
            print(e)

def prisijungti(vartotojai):
    vardas = input("Iveskite prisijungimo varda: \n")
    slaptazodis = input("Iveskite slaptazodi: \n")
    for vartotojas in vartotojai:
        if vartotojas.vardas == vardas and vartotojas.slaptazodis == slaptazodis:
            return vartotojas
    print("Neteisingas prisijungimas!")
    return None

def prideti_filma(filmai):
    filmas = data_handler.ivesti_filma()
    filmai.append(filmas)
    print("Filmas sekmingai pridetas!")
    data_handler.issaugoti_i_faila(filmu_failas, filmai)

def atspausdinti_filmus(filmai):
    for filmas in filmai:
        print(filmas)

def ieskoti_filmu(filmai):
        paieska = input("Iveskite, ko ieskoma: \n")
        paieska_tipas = input("Ar norite ieskoti pagal pavadinima ('p') ar rezisieriu ('r')? \n")
        if paieska_tipas == "p":
            rasti = filmas_service.filmu_paieska_pavadinimas(filmai, paieska)
        elif paieska_tipas == "r":
            rasti = filmas_service.filmu_paieska_rezisierius(filmai, paieska)
        else:
            print("Neteisingai ivestas paieskos tipas!")
            return
        if len(rasti) == 0:
            print("Nieko neradome!")
        else:
            atspausdinti_filmus(rasti)

def pasalinti_filma(filmai):
    pavadinimas = input("Iveskite filmo pavadinima, kuri norite pasalinti: \n")
    rastas = filmas_service.gauti_konkretu_filma_pav(filmai, pavadinimas)
    if rastas is None:
        print("Tokio filmo nepavyko rasti! \n")
        return
    else:
        filmai.remove(rastas)
        print("Filmas sekmingai pasalintas!")
        data_handler.issaugoti_i_faila(filmu_failas, filmai)

def redaguoti_filma(filmai):
    pavadinimas = input("Iveskite filmo pavadinima, kuri norite redaguoti: \n")
    rastas = filmas_service.gauti_konkretu_filma_pav(filmai, pavadinimas)
    if rastas is None:
        print("Tokio filmo nepavyko rasti! \n")
        return
    keiciamas = input("Iveskite, ka norite redaguoti: ('pavadinimas', 'trukme', 'zanras', 'rezisierius', 'isleidimo_metai', 'amziaus_reitingas') \n")
    nauja_verte = input("Iveskite nauja verte: \n")
    rastas_dict = vars(rastas)
    rastas_dict[keiciamas] = nauja_verte  # TODO: rasti kaip geriau, uztikrinant be klaidu
    print("Filmas sekmingai paredaguotas!")
    data_handler.issaugoti_i_faila(filmu_failas, filmai)

def prideti_seansa(filmai, seansai):
    seansas = data_handler.ivesti_seansa(filmai)
    for esantis in seansai:
        persidengimas = seansas_service.patikrinti_persidengima(esantis, seansas)
        if persidengimas is True:
            print("Negalima prideti seanso, sis laikas persidengia su kitu seansu!")
            return
    seansai.append(seansas)
    print("Seansas sekmingai pridetas!")
    data_handler.issaugoti_i_faila(seansu_failas, seansai)

def rodyti_seansus(filmai, seansai):
    for i, seansas in enumerate(seansai):
        if seansas_service.patikrinti_ar_ateinantis(seansas):
            try:
                pav = filmas_service.gauti_konkretu_filma_id(filmai, seansas.filmo_id).pavadinimas
            except Exception as e:
                pav = "Filmas nebuvo rastas"
            print(f"Seanso numeris: {i+1}, Filmas: {pav}, pradzia: {seansas.pradzia}, pabaiga: {seansas.pabaiga}, laisvos vietos: {seansas.vietos}")

def rezervuoti_seansa(filmai, seansai):
    indeksas = data_handler.ivesti_skaiciu("Iveskite seanso numeri: \n")
    if 0 < indeksas <= len(seansai) and seansas_service.patikrinti_ar_ateinantis(seansai[indeksas-1]):
        rezervacija_service.rezervuoti(seansai[indeksas-1])
        print("Sekmingai rezervuota!")
        data_handler.issaugoti_i_faila(seansu_failas, seansai)
    else:
        print("Neteisingai ivestas indeksas!")