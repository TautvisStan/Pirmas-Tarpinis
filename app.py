import views.interface as interface
import services.data_handler as data_handler
import os.path
from config import filmu_failas, seansu_failas

filmai = []
seansai = []
if __name__ == "__main__":
    
    if os.path.exists(filmu_failas):
        filmai = data_handler.uzkrauti_is_failo(filmu_failas)
    if os.path.exists(seansu_failas):
        seansai = data_handler.uzkrauti_is_failo(seansu_failas)
    interface.sukti_menu(filmai, seansai)