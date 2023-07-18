# Coloca el código de tu juego en este archivo. 

# Declara los personajes usados en el juego como en el ejemplo:

# El juego comienza aquí.

label start:

    jump Objetos
    label FinObjetos:

    jump Contador
    label main:

    jump CaminoAntiguo
    label FinalCaminoAntiguo:

    jump Rio
    label FinalRio:

    jump Animal
    label FinalAnimal:

    jump Nido
    label FinalNido:

    jump Comida
    label FinalComida:

    if medallasMadera == 3:
        "MedallasMadera = 3"
    
    #jump EscenaUno
    #label FinalEscenaUno:

    #jump EscenaDos
    #label FinalEscenaDos:

    #jump EscenaTres
    #label FinalEscenaTres:

    #jump EscenaCuatro
    #label FinalEscenaCuatro:

    "FIN"