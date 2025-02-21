from models.filmas import Filmas
import pickle

def ivesti_filma():
    pavadinimas = input("Iveskite filmo pavadinima: \n")
    trukme = ivesti_skaiciu("Iveskite trukme: \n")
    zanras = input("Iveskite zanra: \n")
    rezisierius = input("Iveskite rezisieriu: \n"),
    isleidimo_metai = ivesti_skaiciu("Iveskite isleidimo metus: \n"), 
    amziaus_reitingas = input("Iveskite reitinga: \n")
    return Filmas(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas)

def ivesti_skaiciu(pranesimas):
    sk_str = input(pranesimas)
    try:
        sk_int = int(sk_str)
        return sk_int
    except:
        raise ValueError("Neteisingai ivestas skaicius!")
    

def issaugoti_i_faila(failas, objektas):
    try:
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