from app import filmai
import models.filmas as Filmas
import services.data_handler as data_handler
from config import filmu_failas
from services.filmas_service import *

def sukti_menu(filmai):
    #TODO: listai vartotoju veiksmams
    while True:
        # TODO: Prisijungimas
        try:
            veiksmas = input("Iveskite veiksma: \n")
            if veiksmas == "1":  # Prideti filma #TODO: iskelti i filmas_service?
                prideti_filma(filmai)
            elif veiksmas == "2":  # Perziureti filmus
                atspausdinti_filmus(filmai)
            elif veiksmas == '3': # Filmu paieska
                ieskoti_filmu(filmai)
            elif veiksmas == '4': # Filmu salinimas
                pasalinti_filma(filmai)
            elif veiksmas == "":
                return
            else:
                print("Neteisingai ivestas veiksmas!")
        except Exception as e:
            print("Ivyko klaida!")
            print(e)

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
        paieska_tipas = input("Ar norite ieskoti pagal pavadinima ('p') ar zanra ('z')? \n")
        if paieska_tipas == "p":
            rasti = filmu_paieska_pavadinimas(filmai, paieska.lower())
        elif paieska_tipas == "z":
            rasti = filmu_paieska_zanras(filmai, paieska.lower())
        else:
            print("Neteisingai ivestas paieskos tipas!")
            return
        if len(rasti) == 0:
            print("Nieko neradome!")
        else:
            atspausdinti_filmus(rasti)

def pasalinti_filma(filmai):
    pavadinimas = input("Iveskite filmo pavadinima, kuri norite pasalinti: \n")
    rastas = None
    for filmas in filmai:
        if filmas.pavadinimas == pavadinimas:
            rastas = filmas
            break
    if rastas is None:
        print("Tokio filmo nepavyko rasti! \n")
        return
    else:
        filmai.remove(rastas)
        print("Filmas sekmingai pasalintas!")
        data_handler.issaugoti_i_faila(filmu_failas, filmai)