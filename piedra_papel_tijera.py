jugador_1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
jugador_2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

if jugador_1 == "piedra":
    if jugador_2 == "piedra":
        print("Empate")
    elif jugador_2 == "papel":
        print("Jugador 2 gana")
    elif jugador_2 == "tijera":
        print("Jugador 1 gana")
    else:
        print("Entrada no válida")
elif jugador_1 == "papel":
    if jugador_2 == "piedra":
        print("Jugador 1 gana")
    elif jugador_2 == "papel":
        print("Empate")
    elif jugador_2 == "tijera":
        print("Jugador 2 gana")
    else:
        print("Entrada no válida")
elif jugador_1 == "tijera":
    if jugador_2 == "piedra":
        print("Jugador 2 gana")
    elif jugador_2 == "papel":
        print("Jugador 1 gana")
    elif jugador_2 == "tijera":
        print("Empate")
    else:
        print("Entrada no válida")

else:
    print("Entrada no válida")