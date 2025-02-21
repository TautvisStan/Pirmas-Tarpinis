def filmu_paieska_pavadinimas(filmai, paieska):
    rasti = []
    for filmas in filmai:
        if paieska in filmas.pavadinimas:
            rasti.append(filmas)
    return rasti

def filmu_paieska_zanras(filmai, paieska):
    rasti = []
    for filmas in filmai:
        if paieska in filmas.zanras:
            rasti.append(filmas)
    return rasti