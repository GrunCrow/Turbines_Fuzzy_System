from skfuzzy import control
from Fuzzy_System.membership_functions import salinidad, temperatura, corrientes, altura_laminal, viscosidad, densidad, \
    profundidad, profundidad_colocacion, turbinas

'''
Declaración de las reglas lógicas para el sistema
'''

#                                                 TURBINA OPTIMA
# optima -> tod verde
r_optima = control.Rule((salinidad['Media'] & temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta'] &
                        viscosidad['Media'] & densidad['Media'] & profundidad['Media'] &
                        profundidad_colocacion['Media']),
                        turbinas['Optima'])

#                                                   TURBINA MUY BUENA
# muy buena -> 1 amarillo
r_muy_buena = control.Rule((salinidad['Media'] & profundidad_colocacion['Media'] &
                           ((temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta'] & viscosidad['Media'] & densidad['Media'] & profundidad['Baja']) |
                            (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta'] & viscosidad['Media'] & densidad['Baja'] & profundidad['Media']) |
                            (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta'] & viscosidad['Baja'] & densidad['Media'] & profundidad['Media']) |
                            (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Media'] & viscosidad['Media'] & densidad['Media'] & profundidad['Media']) |
                            (temperatura['Media'] & corrientes['Media'] & altura_laminal['Alta'] & viscosidad['Media'] & densidad['Media'] & profundidad['Media']) |
                            ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Alta'] & altura_laminal['Alta'] & viscosidad['Media'] & densidad['Media'] & profundidad['Media']))),
                           turbinas['Muy Buena'])

#                                                           TURBINA BUENA
# buena -> 2 amarillos
r_buena = control.Rule((salinidad['Media'] & profundidad_colocacion['Media'] &
                       (((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] & altura_laminal['Alta'] & viscosidad['Media'] & densidad['Media'] & profundidad['Media']) |
                        ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Alta'] & altura_laminal['Media'] & viscosidad['Media'] & densidad['Media'] & profundidad['Media']) |
                        ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Alta'] & altura_laminal['Alta'] & viscosidad['Baja'] & densidad['Media'] & profundidad['Media']) |
                        ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Alta'] & altura_laminal['Alta'] & viscosidad['Media'] & densidad['Baja'] & profundidad['Media']) |
                        ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Alta'] & altura_laminal['Alta'] & viscosidad['Media'] & densidad['Media'] & profundidad['Baja']) |
                        (temperatura['Media'] & corrientes['Media'] & altura_laminal['Media'] & viscosidad['Media'] & densidad['Media'] & profundidad['Media']) |
                        (temperatura['Media'] & corrientes['Media'] & altura_laminal['Alta'] & viscosidad['Baja'] & densidad['Media'] & profundidad['Media']) |
                        (temperatura['Media'] & corrientes['Media'] & altura_laminal['Alta'] & viscosidad['Media'] & densidad['Baja'] & profundidad['Media']) |
                        (temperatura['Media'] & corrientes['Media'] & altura_laminal['Alta'] & viscosidad['Media'] & densidad['Media'] & profundidad['Baja']) |
                        (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Media'] & viscosidad['Baja'] & densidad['Media'] & profundidad['Media']) |
                        (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Media'] & viscosidad['Media'] & densidad['Baja'] & profundidad['Media']) |
                        (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Media'] & viscosidad['Media'] & densidad['Media'] & profundidad['Baja']) |
                        (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta'] & viscosidad['Baja'] & densidad['Baja'] & profundidad['Media']) |
                        (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta'] & viscosidad['Baja'] & densidad['Media'] & profundidad['Baja']) |
                        (temperatura['Media'] & corrientes['Alta'] & altura_laminal['Alta'] & viscosidad['Media'] & densidad['Baja'] & profundidad['Baja']))),
                       turbinas['Buena'])

#                                                   TURBINA NO RECOMENDABLE
# el problema está en el ~ hay que cambiarlo por not pero control.Rule no acepta not, asi que hay que cambiarlo por las
#   leyes de negacion, ya que con ~ devuelve un valor numerico (0 en el caso q da error y entonces la membership no se puede
#   calcular bien)
# no recomendable por 1 naranja -> solo 1 naranja, 1 naranja + 0/1/2 amarillos
#                                ningun rojo
r_no_recomendable = control.Rule((((salinidad['Media'] &
                                   (temperatura['Alta'] | temperatura['Media'] | temperatura['Baja']) &
                                   (corrientes['Alta'] | corrientes['Media'] | corrientes['Baja']) &
                                   (altura_laminal['Alta'] | altura_laminal['Media'] | altura_laminal['Baja']) &
                                   (viscosidad['Muy Baja'] | viscosidad['Media'] | viscosidad['Baja']) &
                                   (densidad['Media'] | densidad['Baja']) &
                                   (profundidad['Media'] | profundidad['Baja']) &
                                   (profundidad_colocacion['Media'] | profundidad_colocacion['Baja'])) &
                                 # no tod amarillo
                                  ((temperatura['Media'] & (corrientes['Alta'] | corrientes['Baja']) &
                                    (altura_laminal['Alta'] | altura_laminal['Baja']) & (viscosidad['Media'] | viscosidad['Muy Baja']) &
                                    densidad['Media'] & profundidad['Media'] & (profundidad_colocacion['Media'] | profundidad_colocacion['Baja']))) &
                                 # no + 1 naranjas
                                 # corrientes naranja resto de otro
                                  ((corrientes['Baja'] & (altura_laminal['Alta'] | altura_laminal['Media']) & (viscosidad['Media'] | viscosidad['Baja']) & profundidad_colocacion['Media']) |
                                   # altura laminal naranja resto de otro
                                   ((corrientes['Alta'] | corrientes['Media']) & (altura_laminal['Baja']) & (viscosidad['Media'] | viscosidad['Baja']) & profundidad_colocacion['Media']) |
                                   # viscosidad naranja resto de otro
                                   ((corrientes['Alta'] | corrientes['Media']) & (altura_laminal['Alta'] | altura_laminal['Media']) & (viscosidad['Muy Baja']) & profundidad_colocacion['Media']) |
                                   # prof colocacion naranja resto de otro
                                   ((corrientes['Alta'] | corrientes['Media']) & (altura_laminal['Alta'] | altura_laminal['Media']) & (viscosidad['Media'] | viscosidad['Baja']) & profundidad_colocacion['Baja']))) &
                                 # salinidad será media si o si en este caso -> incluir
                                  ((salinidad['Media']) &
                                 # algun naranja y menos de 3 amarillos (0/1/2)
                                 #  no hay mas de 2 amarillos
                                    # temp y corrientes amarillo
                                   ((((temperatura['Media'] | (corrientes['Alta'] | corrientes['Baja']) | (altura_laminal['Alta'] | altura_laminal['Baja']) & (viscosidad['Media'] | viscosidad['Muy Baja']) & densidad['Media'] & profundidad['Media'])
                                     & (temperatura['Media'] | (corrientes['Alta'] | corrientes['Baja']) & (altura_laminal['Alta'] | altura_laminal['Baja']) & (viscosidad['Media'] | viscosidad['Muy Baja']) & densidad['Media'] & profundidad['Media'])
                                     & (temperatura['Media'] | (corrientes['Alta'] | corrientes['Baja']) & (altura_laminal['Alta'] | altura_laminal['Baja']) & (viscosidad['Media'] | viscosidad['Muy Baja']) | densidad['Media'] & profundidad['Media'])
                                     & (temperatura['Media'] | (corrientes['Alta'] | corrientes['Baja']) & (altura_laminal['Alta'] | altura_laminal['Baja']) & (viscosidad['Media'] | viscosidad['Muy Baja']) & densidad['Media'] | profundidad['Media'])
                                     & (temperatura['Media'] & (corrientes['Alta'] | corrientes['Baja']) | (altura_laminal['Alta'] | altura_laminal['Baja']) | (viscosidad['Media'] | viscosidad['Muy Baja']) & densidad['Media'] & profundidad['Media'])
                                     & (temperatura['Media'] & (corrientes['Alta'] | corrientes['Baja']) | (altura_laminal['Alta'] | altura_laminal['Baja']) & (viscosidad['Media'] | viscosidad['Muy Baja']) | densidad['Media'] & profundidad['Media'])
                                     & (temperatura['Media'] & (corrientes['Alta'] | corrientes['Baja']) | (altura_laminal['Alta'] | altura_laminal['Baja']) & (viscosidad['Media'] | viscosidad['Muy Baja']) & densidad['Media'] | profundidad['Media'])
                                     & (temperatura['Media'] & (corrientes['Alta'] | corrientes['Baja']) & (altura_laminal['Alta'] | altura_laminal['Baja']) | (viscosidad['Media'] | viscosidad['Muy Baja']) | densidad['Media'] & profundidad['Media'])
                                     & (temperatura['Media'] & (corrientes['Alta'] | corrientes['Baja']) & (altura_laminal['Alta'] | altura_laminal['Baja']) | (viscosidad['Media'] | viscosidad['Muy Baja']) & densidad['Media'] | profundidad['Media'])
                                     & (temperatura['Media'] & (corrientes['Alta'] | corrientes['Baja']) & (altura_laminal['Alta'] | altura_laminal['Baja']) & (viscosidad['Media'] | viscosidad['Muy Baja']) | densidad['Media'] | profundidad['Media']))) &
                                   # algun naranja
                                    (corrientes['Baja'] | altura_laminal['Baja'] | viscosidad['Muy Baja'] | profundidad_colocacion['Baja'])) |
                                  # ningun naranja y hasta 5 amarillos
                                  #          ningun naranja
                                   (((corrientes['Alta'] | corrientes['Media']) & (altura_laminal['Alta'] | altura_laminal['Media']) & (viscosidad['Alta'] | viscosidad['Media']) & profundidad_colocacion['Media']) &
                                      # hasta 5 amarillos con min 3
                                      (((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] &
                                        altura_laminal['Media'] | viscosidad['Baja'] | densidad['Baja'] |
                                        profundidad['Baja'])
                                       | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] |
                                           altura_laminal['Media'] & viscosidad['Baja'] | densidad['Baja'] |
                                           profundidad['Baja'])
                                       | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] |
                                           altura_laminal['Media'] | viscosidad['Baja'] & densidad['Baja'] |
                                           profundidad['Baja'])
                                       | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] |
                                           altura_laminal['Media'] | viscosidad['Baja'] | densidad['Baja'] &
                                           profundidad['Baja'])
                                       | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] &
                                           altura_laminal['Media'] & viscosidad['Baja'] | densidad['Baja'] |
                                           profundidad['Baja'])
                                       | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] &
                                           altura_laminal['Media'] | viscosidad['Baja'] & densidad['Baja'] |
                                           profundidad['Baja'])
                                       | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] &
                                           altura_laminal['Media'] | viscosidad['Baja'] | densidad['Baja'] &
                                           profundidad['Baja'])
                                       | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] |
                                           altura_laminal['Media'] & viscosidad['Baja'] & densidad['Baja'] |
                                           profundidad['Baja'])
                                       | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] |
                                           altura_laminal['Media'] & viscosidad['Baja'] | densidad['Baja'] &
                                           profundidad['Baja'])
                                       | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] |
                                           altura_laminal['Media'] | viscosidad['Baja'] & densidad['Baja'] &
                                           profundidad['Baja']))))),
                                 turbinas['No Recomendable'])

#                                                   TURBINA DESCARTADA
# todo check

#                               algun rojo
r_descartada = control.Rule((((salinidad['Alta'] | salinidad['Baja'])
                             | (temperatura['Muy Alta'] | temperatura['Muy Baja'])
                             | corrientes['Muy Baja']
                             | altura_laminal['Muy Baja']
                             | viscosidad['Alta']
                             | (densidad['Alta'] | densidad['Muy Baja'])
                             | (profundidad['Alta'] | profundidad['Muy Baja'])
                             | (profundidad_colocacion['Alta'] | profundidad_colocacion['Muy Baja'])) |
                            # al menos 2 naranjas
                             ((corrientes['Baja'] & altura_laminal['Baja']) | (corrientes['Baja'] & viscosidad['Muy Baja']) |
                             (corrientes['Baja'] & profundidad_colocacion['Baja']) |
                             (altura_laminal['Baja'] & viscosidad['Muy Baja']) |
                             (altura_laminal['Baja'] & profundidad_colocacion['Baja']) |
                             (viscosidad['Muy Baja'] & profundidad_colocacion['Baja'])) |
                             # 1 naranja y 3 amarillos
                             #       al menos 1 naranja
                             ((corrientes['Baja'] | altura_laminal['Baja'] | viscosidad['Muy Baja'] | profundidad_colocacion['Baja']) &
                              #      al menos 3 amarillos
                              (((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] & altura_laminal['Media'] | viscosidad['Baja'] | densidad['Baja'] | profundidad['Baja'])
                               | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] | altura_laminal['Media'] & viscosidad['Baja'] | densidad['Baja'] | profundidad['Baja'])
                               | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] | altura_laminal['Media'] | viscosidad['Baja'] & densidad['Baja'] | profundidad['Baja'])
                               | ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] | altura_laminal['Media'] | viscosidad['Baja'] | densidad['Baja'] & profundidad['Baja'])
                               | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] & altura_laminal['Media'] & viscosidad['Baja'] | densidad['Baja'] | profundidad['Baja'])
                               | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] & altura_laminal['Media'] | viscosidad['Baja'] & densidad['Baja'] | profundidad['Baja'])
                               | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] & altura_laminal['Media'] | viscosidad['Baja'] | densidad['Baja'] & profundidad['Baja'])
                               | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] | altura_laminal['Media'] & viscosidad['Baja'] & densidad['Baja'] | profundidad['Baja'])
                               | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] | altura_laminal['Media'] & viscosidad['Baja'] | densidad['Baja'] & profundidad['Baja'])
                               | ((temperatura['Alta'] | temperatura['Baja']) | corrientes['Media'] | altura_laminal['Media'] | viscosidad['Baja'] & densidad['Baja'] & profundidad['Baja']))) |
                             # descartada por min 6 amarillos (max de amarillos posibles -> todos los amarillos en am)
                             # salinidad y prof de colocacion da igual los valores
                             ((temperatura['Alta'] | temperatura['Baja']) & corrientes['Media'] & altura_laminal['Media']
                              & viscosidad['Baja'] & densidad['Baja'] & profundidad['Baja'])),
                            turbinas['Descartada'])
