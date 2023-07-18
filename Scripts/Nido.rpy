label Nido:

    "Escena 4: Nido"

    n "Vez un nido de aves en la distancia"
    n "Encuentras unas rocas en el suelo"

    menu:
        "¿Que haces?"

        "¿Tirar las piedras al nido?":
            $ tirarPiedras = True
        
        "Seguir avanzando":
            $ tirarPiedras = False
            $ medallasMadera += 1

    if tirarPiedras:
        n "El nido se cae, rompiendo sus huevos"

    if not tirarPiedras:
        n "Encuentras una medalla de madera en el suelo y la recoges"

    "Sigues avanzando"

    jump FinalNido