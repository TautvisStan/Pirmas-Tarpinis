from models.seansas import Seansas

def rezervuoti(seansas : Seansas):
    if seansas.vietos > 0:
        seansas.vietos -= 1
        return
    else:
        raise Exception("Pasirinktame seanse nera vietu!")