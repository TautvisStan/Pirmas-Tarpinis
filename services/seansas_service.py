from datetime import datetime

from models.seansas import Seansas
def patikrinti_persidengima(seansas1 : Seansas, seansas2 : Seansas):
    latest_start = max(seansas1.pradzia, seansas2.pradzia)
    earliest_end = min(seansas1.pabaiga, seansas2.pabaiga)

    skritumas = (earliest_end - latest_start).total_seconds()
    overlap = max(0, skritumas)
    print(f"{latest_start}, {earliest_end}, {overlap}")
    return overlap > 0

def patikrinti_ar_ateinantis(seansas : Seansas):
    return datetime.now() < seansas.pradzia

