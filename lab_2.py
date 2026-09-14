abecele = "aąbcčdeęėfghiįyjklmnoprsštuųūvzž"
tekstas1 = "Ėmįąnc ąnvmėčšgųv fz čehee nčfčkž."
raktas1 = "nevėžis"

with open("variantai/7.txt", "r", encoding="utf-8") as failas:
    nuskaitytas = failas.readlines()

tekstas2 = "".join(nuskaitytas[5:])

def desifravimas(tekstas, raktas):

    desifruotas = ""
    rakto_pozicija = 0

    for i in range(len(tekstas)):

        simb = abecele.find(tekstas[i].lower())

        if simb >= 0:
            rakto_index = abecele.find(raktas[rakto_pozicija % len(raktas)])
            index = (simb - rakto_index) % 32
            rakto_pozicija += 1

            if tekstas[i].isupper():
                desifruotas += abecele[index].upper()
            else:
                desifruotas += abecele[index]            
        else:
            desifruotas += tekstas[i]
        
    return desifruotas


def teksto_tvarkymas():

    sutvarkytas = ""

    for simb in tekstas2:
        if simb.lower() in abecele:
            sutvarkytas += simb.lower()
    return sutvarkytas

def rakto_ilgio_paieska(paruostas_tekstas):

    paruostas_tekstas = teksto_tvarkymas()

    digrama = {}
    for i in range(len(paruostas_tekstas) - 1):
        derinys = paruostas_tekstas[i:i + 2]

        if derinys not in digrama:
            digrama[derinys] = []

        digrama[derinys].append(i)


    atstumai = []
    for pozicija in digrama.values():
        if len(pozicija) > 1:
            for i in range(len(pozicija)):
                for j in range(i + 1, len(pozicija)):
                    atstumas = pozicija[j] - pozicija[i]
                    atstumai.append(atstumas)

    # print(atstumai)

    dalikliai = {}
    for atstumas in atstumai:
        for daliklis in range(2, atstumas + 1):
            if atstumas % daliklis == 0:
                if daliklis not in dalikliai:
                    dalikliai[daliklis] = 0 

                dalikliai[daliklis] += 1


    dalikliai = sorted( 
        dalikliai.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return dalikliai

def padalijimas_grupes(paruostas_tekstas, k):

    galimi_ilgiai = rakto_ilgio_paieska(paruostas_tekstas)
    ilgis = galimi_ilgiai[k][0]
    grupes = [""] * ilgis

    for i, simbolis in enumerate(paruostas_tekstas):
        grupes[i % ilgis] += simbolis

    return grupes

pasiskirstymas_kalboje = {
    "i": 12.96, "u": 4.59, "g": 1.79, "ą": 0.54,
    "a": 11.19, "k": 4.17, "ė": 1.66, "į": 0.48,
    "s": 7.88, "m": 3.58, "b": 1.48, "č": 0.43,
    "o": 6.74, "l": 3.50, "y": 1.43, "ū": 0.40,
    "r": 5.67, "p": 2.73, "ų": 1.26, "f": 0.35,
    "e": 5.62, "v": 2.65, "š": 1.13, "z": 0.35,
    "t": 5.33, "d": 2.58, "ž": 0.80, "h": 0.28,
    "n": 5.14, "j": 2.38, "c": 0.60, "ę": 0.17
}

def geriausias_cezario_poslinkis(grupe):
    geriausias_poslinkis = 0
    maziausias_ivertis = float("inf")

    for poslinkis in range(len(abecele)):
        desifruota = ""
        for raide in grupe:
            index = abecele.find(raide.lower())
            desifruota += abecele[(index - poslinkis) % len(abecele)]

        daznis = {raide: 0 for raide in abecele}
        for raide in desifruota:
            daznis[raide] += 1

        ivertis = 0
        for raide in abecele:
            tiketinas = pasiskirstymas_kalboje[raide] * len(grupe) / 100
            if tiketinas > 0:
                ivertis += (daznis[raide] - tiketinas) ** 2 / tiketinas

        if ivertis < maziausias_ivertis:
            maziausias_ivertis = ivertis
            geriausias_poslinkis = poslinkis

    print(f"poslinkis: {geriausias_poslinkis}")
    return geriausias_poslinkis


def vigenere_rakto_paieska(paruostas_tekstas, k):

    grupes = padalijimas_grupes(paruostas_tekstas, k)
    poslinkiai = [geriausias_cezario_poslinkis(grupe) for grupe in grupes]
    raktas = "".join(abecele[poslinkis] for poslinkis in poslinkiai)
    return raktas

def desifravimas_vigenere_be_rakto():

    paruostas_tekstas = teksto_tvarkymas()
    galimi_ilgiai = rakto_ilgio_paieska(paruostas_tekstas)

    for k in range(min(4, len(galimi_ilgiai))):
        raktas = vigenere_rakto_paieska(paruostas_tekstas, k)
        ilgis, pasikartojimai = galimi_ilgiai[k]
        tekstas = desifravimas(tekstas2, raktas)

        print(f"Rakto ilgis: {ilgis}")
        print(f"Galimas raktas: {raktas}\n")
        print(tekstas)




desifravimas_vigenere_be_rakto()
print(desifravimas(tekstas1, raktas1))

        





