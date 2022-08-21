from skfuzzy import control
from membership_functions import salinidad, temperatura, corrientes, altura_laminal, viscodidad, densidad, profundidad, \
    profundidad_colocacion, turbinas

'''
Declaración de las reglas lógicas para el sistema
'''

#                                                 TURBINA OPTIMA
# optima -> tod verde
r_optima = control.Rule(salinidad['Media'] & temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta']
                        & viscodidad['Media'] & densidad['Media'] & profundidad['Media']
                        & profundidad_colocacion['Media'],
                        turbinas['Optima'])

#                                                   TURBINA MUY BUENA
# muy buena -> 1 amarillo
r_muy_buena = control.Rule(salinidad['Media'] & profundidad_colocacion['Media']
                           & ((temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Media'] & densidad['Media'] & profundidad['Baja'])
                              | (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Media'] & densidad['Baja'] & profundidad['Media'])
                              | (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Baja'] & densidad['Media'] & profundidad['Media'])
                              | (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Media'] & viscodidad['Media'] & densidad['Media'] & profundidad['Media'])
                              | (temperatura['Media'] & corrientes['Media'] & altura_laminal['Alta'] & viscodidad['Media'] & densidad['Media'] & profundidad['Media'])
                              | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Media'] & densidad['Media'] & profundidad['Media'])),
                           turbinas['Muy Buena'])

#                                                   TURBINA BUENA
# buena -> 2 amarillos
r_buena = control.Rule(salinidad['Media'] & profundidad_colocacion['Media']
                       & (((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] & altura_laminal['Alta'] & viscodidad['Media'] & densidad['Media'] & profundidad['Media'])
                          | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Alta'] & altura_laminal['Media'] & viscodidad['Media'] & densidad['Media'] & profundidad['Media'])
                          | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Baja'] & densidad['Media'] & profundidad['Media'])
                          | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Media'] & densidad['Baja'] & profundidad['Media'])
                          | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Media'] & densidad['Media'] & profundidad['Baja'])
                          | (temperatura['Media'] & corrientes['Media'] & altura_laminal['Media'] & viscodidad['Media'] & densidad['Media'] & profundidad['Media'])
                          | (temperatura['Media'] & corrientes['Media'] & altura_laminal['Alta'] & viscodidad['Baja'] & densidad['Media'] & profundidad['Media'])
                          | (temperatura['Media'] & corrientes['Media'] & altura_laminal['Alta'] & viscodidad['Media'] & densidad['Baja'] & profundidad['Media'])
                          | (temperatura['Media'] & corrientes['Media'] & altura_laminal['Alta'] & viscodidad['Media'] & densidad['Media'] & profundidad['Baja'])
                          | (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Media'] & viscodidad['Baja'] & densidad['Media'] & profundidad['Media'])
                          | (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Media'] & viscodidad['Media'] & densidad['Baja'] & profundidad['Media'])
                          | (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Media'] & viscodidad['Media'] & densidad['Media'] & profundidad['Baja'])
                          | (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Baja'] & densidad['Baja'] & profundidad['Media'])
                          | (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Baja'] & densidad['Media'] & profundidad['Baja'])
                          | (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Media'] & densidad['Baja'] & profundidad['Baja'])),
                       turbinas['Buena'])

#                                                   TURBINA NO RECOMENDABLE
# no recomendable por 1 naranja
r_no_recomendable_naranja = control.Rule((salinidad['Media']
                                          # solo 1 naranja
                                          & ((temperatura['Media'] & densidad['Media'] & profundidad['Media']
                                              & ((corrientes['Baja'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Media'])
                                                 | (corrientes['Alta'] & altura_laminal['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])
                                                 | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])
                                                 | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))
                                             #  1 naranja + 1 amarillo
                                             | ((temperatura['Alta'] | temperatura['Baja']) & densidad['Media'] & profundidad['Media']    # temp amarillo
                                                & ((corrientes['Baja'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Media'])   # corrientes nar
                                                   | (corrientes['Alta'] & altura_laminal['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])     # alt_laminal nar
                                                   | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])  # viscosidad nar
                                                   | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))    # prof_coloc nar
                                             | (temperatura['Media'] & densidad['Baja'] & profundidad['Media']  # densidad amarillo
                                                & ((corrientes['Baja'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Media'])    # corrientes nar
                                                    | (corrientes['Alta'] & altura_laminal['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])      # alt_laminal nar
                                                    | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])   # viscosidad nar
                                                    | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))     # prof_coloc nar
                                             | (temperatura['Media'] & densidad['Media'] & profundidad['Baja']     # profundidad amarillo
                                                & ((corrientes['Baja'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Media'])   # corrientes nar
                                                    | (corrientes['Alta'] & altura_laminal['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])     # alt_laminal nar
                                                    | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])  # viscosidad nar
                                                    | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))    # prof_coloc nar
                                             | (temperatura['Media'] & densidad['Media'] & profundidad['Media'] & corrientes['Media']     # corrientes amarillo
                                                & ((altura_laminal['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])   # alt_laminal nar
                                                    | (altura_laminal['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])  # viscosidad nar
                                                    | (altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))    # prof_coloc nar
                                             | (temperatura['Media'] & densidad['Media'] & profundidad['Media'] & altura_laminal['Media']    # alt_laminal amarillo
                                                & ((corrientes['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])   # corrientes nar
                                                    | (corrientes['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])  # viscosidad nar
                                                    | (corrientes['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))    # prof_coloc nar
                                             | (temperatura['Media'] & densidad['Media'] & profundidad['Media'] & viscodidad['Baja']  # viscosidad amarillo
                                                & ((corrientes['Baja'] & altura_laminal['Alta'] & profundidad_colocacion['Media'])   # corrientes nar
                                                    | (corrientes['Alta'] & altura_laminal['Baja'] & profundidad_colocacion['Media'])     # alt_laminal nar
                                                    | (corrientes['Alta'] & altura_laminal['Alta'] & profundidad_colocacion['Baja']))))   # prof_coloc nar
                                          # 1 naranja + 2 amarillos
                                          | (((temperatura['Alta'] | temperatura['Baja']) & densidad['Baja'] & profundidad['Media']  # temperatura y densidad amarillo
                                              & ((corrientes['Baja'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Media'])    # corrientes nar
                                                 | (corrientes['Alta'] & altura_laminal['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])      # alt_laminal nar
                                                 | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])   # viscosidad nar
                                                 | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))     # prof_coloc nar
                                             | ((temperatura['Alta'] | temperatura['Baja']) & densidad['Media'] & profundidad['Baja']  # temperatura y prof amarillo
                                                & ((corrientes['Baja'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Media'])    # corrientes nar
                                                    | (corrientes['Alta'] & altura_laminal['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])      # alt_laminal nar
                                                    | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])   # viscosidad nar
                                                    | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))     # prof_coloc nar
                                             | ((temperatura['Alta'] | temperatura['Baja']) & densidad['Media'] & profundidad['Media'] & corrientes['Media']  # temperatura y corrientes amarillo
                                                & ((altura_laminal['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])      # alt_laminal nar
                                                    | (altura_laminal['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])   # viscosidad nar
                                                    | (altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))     # prof_coloc nar
                                             | ((temperatura['Alta'] | temperatura['Baja']) & densidad['Media'] & profundidad['Baja'] & altura_laminal['Media']  # temperatura y alt laminal amarillo
                                                & ((corrientes['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])    # corrientes nar
                                                    | (corrientes['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])   # viscosidad nar
                                                    | (corrientes['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))     # prof_coloc nar
                                             | ((temperatura['Alta'] | temperatura['Baja']) & densidad['Baja'] & profundidad['Media'] & viscodidad['Baja']  # temperatura y viscosidad amarillo
                                                & ((corrientes['Baja'] & altura_laminal['Alta'] & profundidad_colocacion['Media'])    # corrientes nar
                                                    | (corrientes['Alta'] & altura_laminal['Baja'] & profundidad_colocacion['Media'])      # alt_laminal nar
                                                    | (corrientes['Alta'] & altura_laminal['Alta'] & profundidad_colocacion['Baja'])))     # prof_coloc nar

                                             | (temperatura['Media'] & densidad['Baja'] & profundidad['Baja']  # densidad  y profundidad amarillo
                                                & ((corrientes['Baja'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Media'])    # corrientes nar
                                                    | (corrientes['Alta'] & altura_laminal['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])      # alt_laminal nar
                                                    | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])   # viscosidad nar
                                                    | (corrientes['Alta'] & altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))     # prof_coloc nar
                                             | (temperatura['Media'] & densidad['Baja'] & profundidad['Media'] & corrientes['Media']  # densidad y corrientes amarillo
                                                & ((altura_laminal['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])      # alt_laminal nar
                                                    | (altura_laminal['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])   # viscosidad nar
                                                    | (altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))     # prof_coloc nar
                                             | (temperatura['Media'] & densidad['Baja'] & profundidad['Baja'] & altura_laminal['Media']  # densidad y alt laminal amarillo
                                                & ((corrientes['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])    # corrientes nar
                                                    | (corrientes['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])   # viscosidad nar
                                                    | (corrientes['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))     # prof_coloc nar
                                             | (temperatura['Media'] & densidad['Baja'] & profundidad['Media'] & viscodidad['Baja']  # densidad y viscosidad amarillo
                                                & ((corrientes['Baja'] & altura_laminal['Alta'] & profundidad_colocacion['Media'])    # corrientes nar
                                                    | (corrientes['Alta'] & altura_laminal['Baja'] & profundidad_colocacion['Media'])      # alt_laminal nar
                                                    | (corrientes['Alta'] & altura_laminal['Alta'] & profundidad_colocacion['Baja'])))     # prof_coloc nar

                                             | (temperatura['Media'] & densidad['Media'] & profundidad['Baja'] & corrientes['Media']  # profundidad y corrientes amarillo
                                                & ((altura_laminal['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])      # alt_laminal nar
                                                    | (altura_laminal['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])   # viscosidad nar
                                                    | (altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))     # prof_coloc nar
                                             | (temperatura['Media'] & densidad['Media'] & profundidad['Baja'] & altura_laminal['Media']  # profundidad y alt laminal amarillo
                                                & ((corrientes['Baja'] & viscodidad['Media'] & profundidad_colocacion['Media'])    # corrientes nar
                                                    | (corrientes['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])   # viscosidad nar
                                                    | (corrientes['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))     # prof_coloc nar
                                             | (temperatura['Media'] & densidad['Media'] & profundidad['Baja'] & viscodidad['Baja']  # profundidad y viscosidad amarillo
                                                & ((corrientes['Baja'] & altura_laminal['Alta'] & profundidad_colocacion['Media'])    # corrientes nar
                                                    | (corrientes['Alta'] & altura_laminal['Baja'] & profundidad_colocacion['Media'])      # alt_laminal nar
                                                    | (corrientes['Alta'] & altura_laminal['Alta'] & profundidad_colocacion['Baja'])))     # prof_coloc nar

                                             | (temperatura['Media'] & densidad['Media'] & profundidad['Media'] & corrientes['Media'] & altura_laminal['Media']  # corrientes y alt laminal amarillo
                                                & ((altura_laminal['Alta'] & viscodidad['Muy Baja'] & profundidad_colocacion['Media'])   # viscosidad nar
                                                    | (altura_laminal['Alta'] & viscodidad['Media'] & profundidad_colocacion['Baja'])))     # prof_coloc nar
                                             | (temperatura['Media'] & densidad['Media'] & profundidad['Baja'] & corrientes['Media'] & viscodidad['Baja']   # corrientes y viscosidad amarillo
                                                & ((corrientes['Alta'] & altura_laminal['Baja'] & profundidad_colocacion['Media'])      # alt_laminal nar
                                                    | (corrientes['Alta'] & altura_laminal['Alta'] & profundidad_colocacion['Baja'])))     # prof_coloc nar

                                             | (temperatura['Media'] & densidad['Media'] & profundidad['Media'] & altura_laminal['Media'] & viscodidad['Baja']  # alt laminal y viscosidad amarillo
                                                & ((corrientes['Baja'] & profundidad_colocacion['Media'])   # corrientes nar
                                                    | (corrientes['Alta'] & profundidad_colocacion['Baja']))))),    # prof_coloc nar
                                         turbinas['No Recomendable'])

# no algun rojo
# no algun naranja
# no tod naranja
# -> 3 am + or del resto
# no recomendable por 3 amarillos
r_no_recomendable_amarillos = control.Rule((~((salinidad['Alta'] | salinidad['Baja'])   # ningun rojo
                                            | (temperatura['Muy Alta'] | temperatura['Muy Baja'])
                                            | corrientes['Muy Baja']
                                            | altura_laminal['Muy Baja']
                                            | viscodidad['Alta']
                                            | (densidad['Alta'] | densidad['Muy Baja'])
                                            | (profundidad['Alta'] | profundidad['Muy Baja'])
                                            | (profundidad_colocacion['Alta'] | profundidad_colocacion['Muy Baja'])) &
                                            ~(corrientes['Baja'] | altura_laminal['Baja'] | viscodidad['Muy Baja'] |    # no algun naranja
                                              profundidad_colocacion['Baja']) &  # and no tod naranj
                                            ~(((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] &      # no tod amarillo
                                               altura_laminal['Media'] & viscodidad['Baja'] & densidad['Baja'] &
                                               profundidad['Baja']))) &
                                           (((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] &        # min 3 amarillos
                                             altura_laminal['Media'] | viscodidad['Baja'] | densidad['Baja'] |
                                             profundidad['Baja'])
                                            | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] |
                                               altura_laminal['Media'] & viscodidad['Baja'] | densidad['Baja'] |
                                               profundidad['Baja'])
                                            | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] |
                                               altura_laminal['Media'] | viscodidad['Baja'] & densidad['Baja'] |
                                               profundidad['Baja'])
                                            | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] |
                                               altura_laminal['Media'] | viscodidad['Baja'] | densidad['Baja'] &
                                               profundidad['Baja'])
                                            | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] &
                                               altura_laminal['Media'] & viscodidad['Baja'] | densidad['Baja'] |
                                               profundidad['Baja'])
                                            | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] &
                                               altura_laminal['Media'] | viscodidad['Baja'] & densidad['Baja'] |
                                               profundidad['Baja'])
                                            | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] &
                                               altura_laminal['Media'] | viscodidad['Baja'] | densidad['Baja'] &
                                               profundidad['Baja'])
                                            | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] |
                                               altura_laminal['Media'] & viscodidad['Baja'] & densidad['Baja'] |
                                               profundidad['Baja'])
                                            | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] |
                                               altura_laminal['Media'] & viscodidad['Baja'] | densidad['Baja'] &
                                               profundidad['Baja'])
                                            | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] |
                                               altura_laminal['Media'] | viscodidad['Baja'] & densidad['Baja'] &
                                               profundidad['Baja'])),
                                           turbinas['No Recomendable'])

#                                                   TURBINA DESCARTADA
# descartada por (al menos 1) rojo
r_descartada_rojo = control.Rule((salinidad['Alta'] | salinidad['Baja'])
                                 | (temperatura['Muy Alta'] | temperatura['Muy Baja'])
                                 | corrientes['Muy Baja']
                                 | altura_laminal['Muy Baja']
                                 | viscodidad['Alta']
                                 | (densidad['Alta'] | densidad['Muy Baja'])
                                 | (profundidad['Alta'] | profundidad['Muy Baja'])
                                 | (profundidad_colocacion['Alta'] | profundidad_colocacion['Muy Baja']),
                                 turbinas['Descartada'])

#   descartada por (al menos 2) naranjas
r_descartada_naranjas = control.Rule(((corrientes['Baja'] & altura_laminal['Baja']) | (corrientes['Baja'] & viscodidad['Muy Baja']) |
                                      (corrientes['Baja'] & profundidad_colocacion['Baja']) |
                                      (altura_laminal['Baja'] & viscodidad['Muy Baja']) |
                                      (altura_laminal['Baja'] & profundidad_colocacion['Baja']) |
                                      (viscodidad['Muy Baja'] & profundidad_colocacion['Baja'])),
                                     turbinas['Descartada'])

r_descartada_naranja_amarillos = control.Rule(((corrientes['Baja'] | altura_laminal['Baja'] | viscodidad['Muy Baja'] | profundidad_colocacion['Baja']) &    # al menos un naranja
                                               (salinidad['Media'] &
                                                # al menos 3 amarillos
                                                (((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] & altura_laminal['Media'] | viscodidad['Baja'] | densidad['Baja'] | profundidad['Baja'])
                                                 | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] | altura_laminal['Media'] & viscodidad['Baja'] | densidad['Baja'] | profundidad['Baja'])
                                                 | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] | altura_laminal['Media'] | viscodidad['Baja'] & densidad['Baja'] | profundidad['Baja'])
                                                 | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] | altura_laminal['Media'] | viscodidad['Baja'] | densidad['Baja'] & profundidad['Baja'])
                                                 | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] & altura_laminal['Media'] & viscodidad['Baja'] | densidad['Baja'] | profundidad['Baja'])
                                                 | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] & altura_laminal['Media'] | viscodidad['Baja'] & densidad['Baja'] | profundidad['Baja'])
                                                 | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] & altura_laminal['Media'] | viscodidad['Baja'] | densidad['Baja'] & profundidad['Baja'])
                                                 | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] | altura_laminal['Media'] & viscodidad['Baja'] & densidad['Baja'] | profundidad['Baja'])
                                                 | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] | altura_laminal['Media'] & viscodidad['Baja'] | densidad['Baja'] & profundidad['Baja'])
                                                 | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] | altura_laminal['Media'] | viscodidad['Baja'] & densidad['Baja'] & profundidad['Baja'])))),
                                              turbinas['Descartada'])

# descartada por min 6 amarillos (es el max de amarillos posibles -> todos los amarillos en am)
r_descartada_amarillos = control.Rule(((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] & altura_laminal['Media']
                                      & viscodidad['Baja'] & densidad['Baja'] & profundidad['Baja']),
                                      turbinas['Descartada'])
