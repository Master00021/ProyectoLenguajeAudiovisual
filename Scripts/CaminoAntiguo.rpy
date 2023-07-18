label CaminoAntiguo:

    "Escena 1: Camino Antiguo"

    if not rio:
        n "Entras al bosque"
        n "Luego de haber estado recorriendo el Camino Antiguo, vez una carabana abandonada."

    if rio:
        n "Volviste a la Caravana"

    if palo:
        p "No me queda nada por hacer aquí"

        menu:
            "Seguir avanzando":
                $ investigaste = False
                jump SeguirAvanzando

    menu: 
        "¿Que haces?"

        "Investigar":
            $ investigaste = True
        
        "Seguir avanzando":
            $ investigaste = False

    if investigaste:
        n "Encuentras un palo"

        menu:
            n "¿Lo recoges?"

            "Si":
                $ palo = True
            "No":
                $ palo = False

    label SeguirAvanzando:
    jump FinalCaminoAntiguo