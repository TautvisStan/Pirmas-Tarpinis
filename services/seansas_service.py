from datetime import datetime

from models.seansas import Seansas
def patikrinti_persidengima(seansas1 : Seansas, seansas2 : Seansas):
    veliausias_startas = max(seansas1.pradzia, seansas2.pradzia)
    anskciausias_startas = min(seansas1.pabaiga, seansas2.pabaiga)

    skritumas = (anskciausias_startas - veliausias_startas).total_seconds()
    persidengimas = max(0, skritumas)
    print(f"{veliausias_startas}, {anskciausias_startas}, {persidengimas}")
    return persidengimas > 0

def patikrinti_ar_ateinantis(seansas : Seansas):
    return datetime.now() < seansas.pradzia

