def patikrinti_ar_toks_yra(ivertinimai, naujas):
    for iver in ivertinimai:
        if iver.filmo_id == naujas.filmo_id and iver.vartotojo_id == naujas.vartotojo_id:
            return True
    return False

def gauti_filmo_atsiliepimus(ivertinimai, filmas):
    rasti = []
    for iver in ivertinimai:
        if iver.filmo_id == filmas.id:
            rasti.append(iver)

    return rasti


def gauti_vidurki(ivertinimai, filmas):
    rasti = gauti_filmo_atsiliepimus(ivertinimai, filmas)
    if len(rasti) == 0:
        return None
    suma = 0
    for iver in rasti:
        suma += iver.reitingas
    return suma / len(rasti)