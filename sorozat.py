import random


def general(kisebb, nagyobb):
    szam_lista = []

    if kisebb > nagyobb:
        atmanet = kisebb
        kisebb = nagyobb
        nagyobb = atmanet

    for i in range(0, 15, 1):
        vszam = random.randint(kisebb, nagyobb)
        szam_lista.append(vszam)

    return szam_lista


def ketto():
    szamok_listaja = general(100, 200)
