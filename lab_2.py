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


# print(desifravimas(tekstas1, raktas1))


def teksto_tvarkymas():

    sutvarkytas = ""

    for simb in tekstas2:
        if simb.lower() in abecele:
            sutvarkytas += simb.lower()
    return sutvarkytas


def rakto_ilgio_paieska():

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

    for ilgis, kiekis in dalikliai [:10]:
        print(f"rakto ilgis {ilgis} pasikartojimų: {kiekis}")

    return dalikliai

rakto_ilgio_paieska()

     

