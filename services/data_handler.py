import os
from models.filmas import Filmas
from models.seansas import Seansas
from models.ivertinimas import Ivertinimas
import pickle
import datetime

from services import filmas_service

def ivesti_filma():
    pavadinimas = input("Iveskite filmo pavadinima: \n")
    trukme = ivesti_skaiciu("Iveskite trukme: \n")
    zanras = input("Iveskite zanra: \n")
    rezisierius = input("Iveskite rezisieriu: \n")
    isleidimo_metai = ivesti_skaiciu("Iveskite isleidimo metus: \n")
    amziaus_reitingas = input("Iveskite reitinga: \n")
    return Filmas(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas)

def ivesti_seansa(filmai):
    filmo_pav = input("Iveskite filmo pavadinima: \n")
    filmas = filmas_service.gauti_konkretu_filma_pav(filmai, filmo_pav)
    pradzia = ivesti_data_laika("Iveskite pradzios data ir laika: \n")
    vietos = ivesti_skaiciu("Iveskite, kiek is viso vietu yra seanse: \n")
    kaina = ivesti_skaiciu_f("Iveskite bilieto kaina: \n")
    return Seansas(filmas, pradzia, vietos, kaina)

def ivesti_data_laika(pranesimas):    
    data_str = input(f"{pranesimas} (YYYY-MM-DD HH:MM:SS)\n")
    try:
        data = datetime.datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
        return data
    except:
        raise ValueError("Neteisingai ivesta data/laikas!")

def ivesti_skaiciu(pranesimas):
    sk_str = input(pranesimas)
    try:
        sk_int = int(sk_str)
        return sk_int
    except:
        raise ValueError("Neteisingai ivestas skaicius!")

def ivesti_skaiciu_f(pranesimas):
    sk_str = input(pranesimas)
    try:
        sk_float = float(sk_str)
        return sk_float
    except:
        raise ValueError("Neteisingai ivestas skaicius!")

def issaugoti_i_faila(failas, objektas):
    try:
        os.makedirs(os.path.dirname(failas), exist_ok=True)
        with open(failas, 'wb') as f:
            pickle.dump(objektas, f)
    except Exception as e:
        raise e

def uzkrauti_is_failo(failas):
    try:
        with open(failas, 'rb') as f:
            objektas = pickle.load(f)
        return objektas 
    except FileNotFoundError:
        raise FileNotFoundError("Tokio failo nera!")
    except Exception as e:
        raise e
    
def ivesti_ivertinima(filmai, prisijunges):
    pavadinimas = input("Iveskite filmo pavadinima: \n")
    rastas = filmas_service.gauti_konkretu_filma_pav(filmai, pavadinimas)
    if rastas is None:
        print("Tokio filmo nepavyko rasti! \n")
        return
    reitingas = ivesti_skaiciu("Iveskite reitinga: \n")
    atsiliepimas = input("Iveskite atsiliepima: \n")
    ivertinimas = Ivertinimas(reitingas, atsiliepimas, rastas, prisijunges)
    return ivertinimas