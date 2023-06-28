label EscenaDos:

    ##################DECLARACION OBJETOS UTILIZADOS EN LA ESCENA########################################################################################

    $ Abrazaste = ""
    $ Ninguno = False

    ##################INICIO DE LA ESCENA##############################################################################################################

    "Comienzo segunda escena"

    n "El protagonista llega al hogar de su abuela."
    n "Los padres empiezan a discutir."

    menu:

        h "¿Que deberia de hacer?"

        "¿Por qué estan peleando?":

            "Respuesta..."

            $ Ninguno = True # Preguntar que hacer en este caso
        
        "Abrazar a...":

            menu:

                "Abrazar a mamá":

                    n "Abrazaste a mamá."
                    $ Abrazaste = "mamá"

                "Abrazar a papá":

                    n "Abrazaste a papá."
                    $ Abrazaste = "papá"
        
        "Ignorar":

            n "Los ignoraste..."
            $ Ninguno = True

    if Abrazaste == "mamá":

        n "El padre los mira con tristeza mientras sale de la habitación."

    if Abrazaste == "papá":

        n "La madre los mira con tristeza mientras sale de la habitación."

    if Ninguno:
        
        "La discucion continua hasta que termina."

    jump FinalEscenaDos
