label Rio:

    image rio = "images/Rio.jpg"

    show rio
    with dissolve

    $ rio = True
    $ nadaEncontrado = False

    "Escena 2: Río"

    n "Llegas al río"

    label MenuRio:

    menu: 
        "¿Que haces?"

        "Cruzarlo":
            if palo:
                menu:
                    "¿Estas seguro?"

                    "Cruzar":
                        $ mojado = True

                    "No cruzar":
                        jump MenuRio

            $ mojado = True
            n "Cruzas el rio, pero te mojaste"

        "Buscar algo para cruzarlo" if not nadaEncontrado:
            if palo:
                n "Sacas el palo y lo utilizas para cruzar el río"

            if not palo:
                n "No encuentras nada"
                $ nadaEncontrado = True
                jump MenuRio

        "Regresar a la Caravana":
            jump CaminoAntiguo


    if mojado:
        n "Te das cuenta de que estas muy mojado"

    if not mojado:
        n "Ha bajado la temperatura, generandote frio"

    menu:
        "¿Prender fogata?"

        "Si":
            $ fogata = True
            $ mojado = False                                    # ¿Sera necesario?
            n "Entras en calor, secando tu ropa"

        "No":
            $ fogata = False
            n "Encuentras una medalla de madera y la recoges"
            $ medallasMadera += 1

    n "Sigues avanzando"

    jump FinalRio