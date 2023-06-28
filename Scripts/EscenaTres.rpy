label EscenaTres:

    ##################DECLARACION OBJETOS UTILIZADOS EN LA ESCENA########################################################################################

    $ buscarla = False

    ##################INICIO DE LA ESCENA##############################################################################################################
    
    "Comienzo tercera escena"

    n "Llega la noche..."
    n "Mientras miras por la ventana..."

    h "¿Que?"
    h "¿Abuela? ¿Eres tú?"

    menu:

        "Buscar ayuda" if not Ninguno:

            if Abrazaste == "papá":

                h "Buscare a papá"
                jump EscenaCuatro

            if Abrazaste == "mamá":

                h "Buscare a mamá"
                jump EscenaCuatro
        
        "Ir a buscarla":
            
            $ buscarla = True
            jump EscenaCuatro