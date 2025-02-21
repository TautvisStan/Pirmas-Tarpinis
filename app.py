import views.interface as interface
import services.data_handler as data_handler
import os.path
from config import filmu_failas

filmai = []

if __name__ == "__main__":
    
    if os.path.exists(filmu_failas):
        filmai = data_handler.uzkrauti_is_failo(filmu_failas)
    interface.sukti_menu(filmai)