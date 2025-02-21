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

def gauti_konkretu_filma(filmai, pavadinimas):
    rastas = None
    indeksas = -1
    for i, filmas in enumerate(filmai):
        if filmas.pavadinimas == pavadinimas:
            rastas = filmas
            indeksas = i
            
    return indeksas, rastas