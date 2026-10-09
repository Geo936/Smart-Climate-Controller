def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - (luchtvochtigheid / 100) * windsnelheid


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoels_t = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if gevoels_t < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoels_t < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= gevoels_t < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gevoels_t < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gevoels_t < 22:
        return "Heerlijk weer, niet te koud en niet te warm."
    else:
        return "Warm! Airco aan!"


def weerstation():
    totaal_temp = 0

    for dag in range(1, 8):

        while True:
            temp = input(f"Wat is op dag {dag} de temperatuur:")

            if temp == "":
                print("Bye")
                return

            try:
                temp_celsius = float(temp)
                break
            except ValueError:
                print("Ongeldige invoer, probeer opnieuw.")

        while True:
            wind = input(f"Wat is op dag {dag} de windsnelheid[m/s]: ")

            if wind == "":
                print("Bye")
                return

            try:
                windsnelheid = float(wind)
                break
            except ValueError:
                print("Ongeldige invoer, probeer opnieuw.")

        while True:
            vocht = input(f"Wat is op dag {dag} de vochtigheid[%]: ")

            if vocht == "":
                print("Bye")
                return

            try:
                luchtvochtigheid = int(vocht)

                if 0 <= luchtvochtigheid <= 100:
                    break
                else:
                    print("Voer een geheel getal tussen 0 en 100 in.")

            except ValueError:
                print("Ongeldige invoer, probeer opnieuw.")

        temp_fahrenheit = Fahrenheit(temp_celsius)

        totaal_temp += temp_celsius
        gemiddelde_temp = totaal_temp / dag

        print(f"Het is {temp_celsius:.2f}C ({temp_fahrenheit:.2f}F)")
        print(weerrapport(temp_celsius, windsnelheid, luchtvochtigheid))
        print(f"Gem. temp tot nu toe is {gemiddelde_temp:.2f}")
        print("=============================================")


