from models.vartotojas import Organizatorius, Ziurovas
import views.interface as interface
import services.data_handler as data_handler
import os.path
from config import filmu_failas, seansu_failas, vartotoju_failas, ivertinimu_failas

filmai = []
seansai = []
vartotojai = []
ivertinimai = []
vartotojai.append(Organizatorius("Tautvydas", "123"))
data_handler.issaugoti_i_faila(vartotoju_failas, vartotojai)
if __name__ == "__main__":
    
    if os.path.exists(filmu_failas):
        filmai = data_handler.uzkrauti_is_failo(filmu_failas)
    if os.path.exists(seansu_failas):
        seansai = data_handler.uzkrauti_is_failo(seansu_failas)
    if os.path.exists(vartotoju_failas):
        vartotojai = data_handler.uzkrauti_is_failo(vartotoju_failas)
    if os.path.exists(ivertinimu_failas):
        ivertinimai = data_handler.uzkrauti_is_failo(ivertinimu_failas)


    interface.sukti_menu(filmai, seansai, vartotojai, ivertinimai)