from datetime import datetime
def patikrinti_persidengima(seansas1, seansas2):
    latest_start = max(seansas1.pradzia, seansas2.pradzia)
    earliest_end = min(seansas1.pabaiga, seansas2.pabaiga)

    skritumas = (earliest_end - latest_start).total_seconds()
    overlap = max(0, skritumas)
    print(f"{latest_start}, {earliest_end}, {overlap}")
    return overlap > 0