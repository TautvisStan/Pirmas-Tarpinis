from models.ivertinimas import Ivertinimas
from models.vartotojas import Organizatorius, Ziurovas
from services import rezervacija_service
import services.data_handler as data_handler
from config import filmu_failas, seansu_failas, ivertinimu_failas, vartotoju_failas
import services.filmas_service as filmas_service
import services.seansas_service as seansas_service
import services.ivertinimas_service as ivertinimas_service

from collections import namedtuple

def sukti_menu(filmai, seansai, vartotojai, ivertinimai):
    Veiksmas = namedtuple("Veiksmas", ("pav", "funkcija"))

    veiksmas_iseiti = Veiksmas("Iseiti", lambda: iseiti())
    veiksmas_prideti_filma = Veiksmas("Prideti filma", lambda: prideti_filma(filmai))
    veiksmas_atspausdinti_filmus = Veiksmas("Atspausdinti filmus", lambda: atspausdinti_filmus(ivertinimai, filmai))
    veiksmas_ieskoti_filmu = Veiksmas("Ieskoti filmu", lambda: ieskoti_filmu(ivertinimai, filmai))
    veiksmas_pasalinti_filma = Veiksmas("Pasalinti filma", lambda: pasalinti_filma(filmai))
    veiksmas_redaguoti_filma = Veiksmas("Redaguoti filma", lambda: redaguoti_filma(filmai))
    veiksmas_prideti_seansa = Veiksmas("Prideti seansa", lambda: prideti_seansa(filmai,seansai))
    veiksmas_rodyti_seansus = Veiksmas("Rodyti seansus", lambda: rodyti_seansus(filmai, seansai))
    veiksmas_rezervuoti_seansa = Veiksmas("Rezervuoti seansa", lambda: rezervuoti_seansa(filmai, seansai)) 
    veiksmas_palikti_atsiliepima = Veiksmas("Palikti atsiliepima", lambda: palikti_atsiliepima(filmai, prisijunges, ivertinimai))

#TODO pop filmai pagal rezervacijas;
#TODO pajamos pagal bilietus
    org_veiksmai = [veiksmas_iseiti,
                    veiksmas_prideti_filma,
                    veiksmas_atspausdinti_filmus, 
                    veiksmas_ieskoti_filmu,
                    veiksmas_pasalinti_filma,
                    veiksmas_redaguoti_filma,
                    veiksmas_prideti_seansa,
                    veiksmas_rodyti_seansus]
    
    vart_veiksmai = [veiksmas_iseiti,
                     veiksmas_atspausdinti_filmus,
                     veiksmas_ieskoti_filmu,
                     veiksmas_rodyti_seansus,
                     veiksmas_rezervuoti_seansa,
                     veiksmas_palikti_atsiliepima]

    prisijunges = None
    while prisijunges is None:
        prisijunges = prijungti_vartotoja(vartotojai)

    if isinstance(prisijunges, Ziurovas):
        veiksmai = vart_veiksmai
    else:
        veiksmai = org_veiksmai  

    while True:
        try:
            print("Galimi veiksmai: \n")
            for i, veiksmas in enumerate(veiksmai, 0):
                print(f"{i}: {veiksmas.pav}")
            pasirinktas = data_handler.ivesti_skaiciu("Iveskite veiksma: \n")
            if pasirinktas in range(len(veiksmai)):
                veiksmai[pasirinktas].funkcija()
            else:
                print("Neteisingai pasirinktas veiksmas!")
        except Exception as e:
            print("Ivyko klaida!")
            print(e)
def iseiti():
    quit()

def prijungti_vartotoja(vartotojai):
    veiksmas = input("Iveskite 'p', jei norite prisijungti, kitu atveju bus sukurta nauja ziurovo paskyra \n")
    if veiksmas == "p":
        return prisijungti_esamu(vartotojai)
    else:
        return registruoti_ziurova(vartotojai)

def registruoti_ziurova(vartotojai):
    vartotojas = Ziurovas()
    print(f"Jusu unikalus prisijungimo id yra: '{vartotojas.id}'. Atsiminkie si id!")
    vartotojai.append(vartotojas)
    data_handler.issaugoti_i_faila(vartotoju_failas, vartotojai)
    return vartotojas

def prisijungti_esamu(vartotojai):
    vardas = input("Iveskite prisijungimo varda arba id: \n")
    for vartotojas in vartotojai:
        if isinstance(vartotojas, Ziurovas) and vardas == str(vartotojas.id):
            return vartotojas
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

def atspausdinti_filmus(ivertinimai, filmai):
    for filmas in filmai:
        print(filmas)
        filmo_ivertinimai = ivertinimas_service.gauti_filmo_atsiliepimus(ivertinimai, filmas)
        if len(filmo_ivertinimai) != 0:
            print(f"Ivertinimu vidurkis: {ivertinimas_service.gauti_vidurki(ivertinimai, filmas)}")
            for iver in filmo_ivertinimai:
                print(iver)

def ieskoti_filmu(ivertinimai, filmai):
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
            atspausdinti_filmus(ivertinimai, rasti)

def pasalinti_filma(filmai):
    pavadinimas = input("Iveskite filmo pavadinima, kuri norite pasalinti: \n")
    if filmas_service.pasalinti_filma_pagal_pav(filmai, pavadinimas) is True:
        print("Filmas sekmingai pasalintas!")

def redaguoti_filma(filmai):
    pavadinimas = input("Iveskite filmo pavadinima, kuri norite redaguoti: \n")
    rastas = filmas_service.gauti_konkretu_filma_pav(filmai, pavadinimas)
    if rastas is None:
        print("Tokio filmo nepavyko rasti! \n")
        return
    filmas_service.redaguoti_filma(rastas)
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
        
def palikti_atsiliepima(filmai, prisijunges, ivertinimai):
    ivertinimas = data_handler.ivesti_ivertinima(filmai, prisijunges)
    if ivertinimas_service.patikrinti_ar_toks_yra(ivertinimai, ivertinimas):
        print("Jus jau esate palikes atsiliepima siam filmui!")
        return
    ivertinimai.append(ivertinimas)
    data_handler.issaugoti_i_faila(ivertinimu_failas, ivertinimai)
    print("Atsiliepimas sekmingai paliktas")

