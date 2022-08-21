from skfuzzy import control
from FuzzyRule import r_optima, r_muy_buena, r_buena, r_no_recomendable_amarillos, r_no_recomendable_naranja,\
    r_descartada_rojo, r_descartada_naranjas, r_descartada_naranja_amarillos, r_descartada_amarillos

system_control = control.ControlSystem([r_optima,   # tod verde
                                        r_muy_buena,    # tod verde y un amarillo
                                        r_buena,    # tod verde y 2 amarillo
                                        r_no_recomendable_naranja, r_no_recomendable_amarillos,  # 1 naranja + 0/1/2 amarillos // 3 amarillos + 0/1/2 amarillos
                                        r_descartada_rojo, r_descartada_naranjas, r_descartada_naranja_amarillos, r_descartada_amarillos])  # min (1 rojo, 2 naranjas, 1 naranja + 3 amar, 6 amarillos)
