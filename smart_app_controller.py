def aantal_dagen (inputFile) :
    with open(inputFile, "r") as bestand :
        regels = bestand.readlines()
        return len(regels) - 1



def auto_bereken (inputFile,outputFile) :
    with open(inputFile, "r") as bestand :
        regels = bestand.readlines()

    with open(outputFile, "w") as uitvoer :

        for regel in regels[1:]:
            gegevens = regel.split()

            datum = gegevens[0]
            aantal_mensen = int(gegevens[1])
            temp_setpoint = float(gegevens[2])
            temp_buiten = float(gegevens[3])
            neerslag = float(gegevens[4])

            verschil = temp_setpoint - temp_buiten

            if verschil >= 20 :
                cv_ketel = 100
            elif verschil >= 10 :
                cv_ketel = 50
            else:
                cv_ketel = 0


            ventilatie = aantal_mensen + 1
            if ventilatie > 4 :
                ventilatie = 4


            if neerslag < 3 :
                bewatering = True
            else :
                bewatering = False

            uitvoer.write(f"{datum};{cv_ketel};{ventilatie};{bewatering}\n")



def overwrite_settings(outputFile):
    with open(outputFile, "r") as bestand :
        regels = bestand.readlines()

    datum = input("Welke datum wil je aanpassen? ")

    gevonden = False

    for i in range(len(regels)):
        gegevens = regels[i].strip().split(";")

        if gegevens[0] == datum :
            gevonden = True
            break

    if gevonden == False :
        return -1

    print("1. CV-ketel")
    print("2. Ventilatie")
    print("3. Bewatering")

    keuze = input("Welke instelling wil je aanpassen? ")

    if keuze != "1" and keuze != "2" and keuze != "3" :
        return -3

    if keuze == "1" :
        nieuwe_waarde = input("Nieuwe waarde voor CV-ketel (0-100): ")

        try:
            nieuwe_waarde = int(nieuwe_waarde)

            if 0 <= nieuwe_waarde <= 100 :
                gegevens[1] = str(nieuwe_waarde)
            else:
                return -3

        except ValueError:
            return -3


    elif keuze == "2" :
        nieuwe_waarde = input("Nieuwe waarde voor ventilatie (0-4): ")

        try:
            nieuwe_waarde = int(nieuwe_waarde)

            if 0 <= nieuwe_waarde <= 4 :
                gegevens[2] = str(nieuwe_waarde)
            else:
                return -3

        except ValueError:
            return -3


    elif keuze == "3" :
        nieuwe_waarde = input("Nieuwe waarde voor bewatering (0 of 1): ")

        if nieuwe_waarde == "0" :
            gegevens[3] = "False"
        elif nieuwe_waarde == "1" :
            gegevens[3] = "True"
        else:
            return -3

    regels[i] = ";".join(gegevens) + ("\n")

    with open (outputFile, "w") as bestand :
        bestand.writelines(regels)
        return 0

def smart_app_controller():
    while True:
        print("========================================")
        print("1. Aantal dagen weergeven")
        print("2. Automatisch alle actuatoren berekenen")
        print("3. Waarde overschrijven")
        print("4. Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1" :
            aantal = aantal_dagen("input.txt")
            print("Aantal dagen: ", aantal)

        elif keuze == "2" :
            auto_bereken("input.txt", "output.txt")
            print("Outputbestand is aangemaakt.")

        elif keuze == "3" :
            resultaat = overwrite_settings("output.txt")

            if resultaat == 0 :
                print("Waarde succesvol aangepast.")
            elif resultaat == -1 :
                print("Datum niet gevonden.")
            elif resultaat == -3 :
                print("Ongeldige keuze of waarde.")

        elif keuze == "4" :
            print("Programma gestopt.")
            break

        else :
            print("Ongeldige keuze, probeer opnieuw.")
