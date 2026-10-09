from weerstation import weerstation
from smart_app_controller import smart_app_controller
from huidige import huidige_temperatuur
while True :
    try:
        keuze = int(input(
            "1. Weerstation\n"
            "2. Smart App Controller\n"
            "3. Huidige temperatuur \n"
            "4. Stoppen \n"
            "Maak uw keuze: "
        ))

        if keuze == 1 :
            weerstation()
        elif keuze == 2 :
            smart_app_controller()
        elif keuze == 3 :
            temp = huidige_temperatuur()
            print(f"Huidige Temperatuur in Utrecht: {temp} C")
        elif keuze == 4 :
            break
        else:
            print("Ongeldig keuze.")


    except FileNotFoundError:
        print("Het bestand is niet gevonden.")

    except ValueError:
        print("Ongeldig invoer.")


