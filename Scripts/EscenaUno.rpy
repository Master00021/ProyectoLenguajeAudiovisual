label EscenaUno:

    ##################DECLARACION OBJETOS UTILIZADOS EN LA ESCENA########################################################################################

    $ bolso_recogido = False
    $ chaqueta_recogida = False
    $ amuleto_recogido = False

    ##################INICIO DE LA ESCENA##############################################################################################################

    "Comienzo Primera Escena"

    n "En tú hogar..."

    h "¿Que esta pasando?"

    h "¿Humo?"

    n "¿Que objetos recogeras?"


    label MenuEscenaUno: #Bucle del menu de opciones, mientras quede tiempo

    show screen countdown # Llamada al contador, se activa con show

    if time > 0: # Entrara al menu de opciones mientras quede tiempo en el timer

        menu:
        
            "Bolso" if not bolso_recogido: # if not condition, hace que la opción desaparezca segun la condicion

                $ bolso_recogido = True
                n "Bolso recogido"

                if time > 0:

                    jump MenuEscenaUno # Si el tiempo es mayor a cero, volvera a entrar al option menu

                jump time_end # Si el tiempo es menor a cero, saltara al label time_out

            "Chaqueta" if not chaqueta_recogida:

                $ chaqueta_recogida = True
                n "Chaqueta recogida"

                if time > 0:

                    jump MenuEscenaUno

                jump time_end

            "Amuleto" if not amuleto_recogido:

                $ amuleto_recogido = True
                n "Amuleto recogido"

                if time > 0:

                    jump MenuEscenaUno

                jump time_end
    
    hide screen countdown # Esconder el contador, se desactiva y resetea sus valores con hide

    label time_out:

        n "El tiempo se ha acabado"

        jump time_end

    label time_end:

        if bolso_recogido:

            n "Recogiste el bolso."

        if chaqueta_recogida:

            n "Recogiste la chaqueta."

        if amuleto_recogido:

            n "Recogiste el amuleto."

        if not bolso_recogido and not chaqueta_recogida and not amuleto_recogido:
            
            n "No alcanzaste a recoger nada."

    n "El protagonista sale rapidamente de la casa."

    "Final escena 1"

    jump FinalEscenaUno