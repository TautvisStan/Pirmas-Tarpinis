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
                filmas = data_handler.ivesti_filma()
                filmai.append(filmas)
                print("Filmas sekmingai pridetas!")
                data_handler.issaugoti_i_faila(filmu_failas, filmai)
            elif veiksmas == "2":  # Perziureti filmus
                for filmas in filmai:
                    print(filmas)
            elif veiksmas == '3': # Filmu paieska
                paieska = input("Iveskite, ko ieskoma: \n")
                paieska_tipas = input("Ar norite ieskoti pagal pavadinima ('p') ar zanra ('z')? \n")
                if paieska_tipas == "p":
                    rasti = filmu_paieska_pavadinimas(filmai, paieska.lower())
                elif paieska_tipas == "z":
                    rasti = filmu_paieska_zanras(filmai, paieska.lower())
                else:
                    continue
                if len(rasti) == 0:
                    print("Nieko neradome!")
                else:
                    for filmas in filmai:
                        print(filmas)
            elif veiksmas == "":
                return
            else:
                print("Neteisingai ivestas veiksmas!")
        except Exception as e:
            print("Ivyko klaida!")
            print(e)
