label Contador:

    $ timer_range = 0
    $ timer_jump = 0

    transform alpha_dissolve: # Aparece de alpha 0.5 hacia alpha 1.0

        alpha 0.0
        linear 0.5 alpha 1.0

        on hide:
            linear 0.5 alpha 0 # Desaparece de alpha 1.0 hacia alpha 0.0

    screen countdown:
        timer 0.01 repeat True action If(time > 0.0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
            # Valor del timer
        bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
            # Valor pasado a la barra

    $ time = 5.0 # Tiempo del timer
    $ timer_range = 5.0 # El alcance de la barra en segundos
    $ timer_jump = "time_out"

    jump main