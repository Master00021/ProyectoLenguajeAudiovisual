label Animal:

    "Escena 3: Animal"

    n "Vez a lo lejos lo que parece ser un animal"

    menu:
        "¿Te acercas?"

        "Si":
            $ acercado = True
        "No":
            $ acercado = False

    if acercado:
        "Vez que el animal esta herido"

        menu:
            "¿Que haces?"

            "Ayudarlo":
                $ ayudarAnimal = True

            "Seguir avanzando":
                $ ayudarAnimal = False

    if ayudarAnimal:
        n "Te acercas de a poco hacia el animal"
        n "Observas detenidamente su pata herida"
        n "Tomas una venda y tapas su herida"
        n "El animal se levanta y corre hacia unos arbustos"
        n "Vez una medalla de madera por donde paso el animal y la recoges"

        $ medallasMadera += 1

    n "Sigues avanzando"

    jump FinalAnimal