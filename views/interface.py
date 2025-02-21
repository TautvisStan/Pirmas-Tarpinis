from app import filmai, filmu_failas
import models.filmas as Filmas
import services.data_handler as data_handler

def sukti_menu():
    
    while True:
        # TODO: Prisijungimas
        try:
            veiksmas = input("Iveskite veiksma: \n")
            if veiksmas == "1":  # Prideti filma #TODO: iskelti i filmas_service?
                filmas = data_handler.ivesti_filma()
                filmai.append(filmas)
                print("Filmas sekmingai pridetas!")
                data_handler.issaugoti_i_faila(filmu_failas, filmai)
        except Exception as e:
            print("Ivyko klaida!")
            print(e)
