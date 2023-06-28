label EscenaCuatro:

    ##################INICIO DE LA ESCENA##############################################################################################################

    "Comienzo cuarta escena"

    if Ninguno or buscarla:

        h "¡Abuela!"
        h "¡Espera! ¡No te vayas!"

        n "La Abuela desaparece entrando al bosque"

        menu:

            "¿Que haces?"

            "Correr hacia el bosque":

                n "Corres hacia el bosque."
                n "Pero no encuentras nada y decides devolverte"

            "Buscar ayuda":

                if Abrazaste == "papá":

                    h "Papá, vi a la Abuela afuera, entrando al bosque."
                    p "¿Que vista a la Abuela? ¿No sera a causa del sueño?"

                    n "Tu padre te mira extrañado."

                    jump menuEscenaCuatro

                if Abrazaste == "mamá":
                    
                    h "Mamá, vi a la Abuela afuerra, entrando all bosque."
                    m "¿Que vista a la Abuela? ¿No sera a causa del sueño?"

                    n "Tu madre te mira extrañado."

                    jump menuEscenaCuatro

    if Abrazaste == "papá":

        h "Papá, vi a la Abuela afuera."
        p "No lo creo hijo, seguro sera el sueño"
        h "No papá, yo se que la ví"
        p "Pues dime donde la viste"

        n "Se acercan a donde se vio a la Abuela, pero no hay nada"
        n "Tú padre te mira extrañado"

        jump menuEscenaCuatro

    if Abrazaste == "mamá":

        h "Mamá, vi a la Abuela afuera."
        m "No lo creo hijo, seguro sera el sueño"
        h "No mamá, yo se que la ví"
        m "Pues dime donde la viste"

        n "Se acercan a donde se vio a la Abuela, pero no hay nada"
        n "Tú madre te mira extrañado"

        jump menuEscenaCuatro

    label menuEscenaCuatro:

        if Abrazaste == "papá":

            p "¿Estas totalmente seguro de haberla visto?"

        if Abrazaste == "mamá":

            m "¿Estas totalmente seguro de haberla visto?"

        if Ninguno:

            h "Mamá, Papá, vi a la Abuela afuera."
            m "No lo creo hijo, seguro sera el sueño"
            p "Debe de ser eso hijo, el sueño"
            h "No lo entienden, yo se que la vi"

            m "¿Estas totalmente seguro de haberla visto?"
        
        h "Estoy seguro de haber visto a la Abuela, y como desaparecio al entrar en el bosque."

    jump FinalEscenaCuatro