from skfuzzy import control
from Fuzzy_System.membership_functions import salinity, temperature, currents, laminal_height, viscosity, density, \
    depth, placement_depth, turbines

'''
Declaración de las reglas lógicas para el sistema
'''

#                                                 TURBINA OPTIMA
# optima -> tod verde
r_optimal = control.Rule((salinity['Medium'] & temperature['Medium'] & currents['High'] & laminal_height['High'] &
                         viscosity['Medium'] & density['Medium'] & depth['Medium'] &
                         placement_depth['Medium']),
                        turbines['Optimal'])

#                                                   TURBINA Very BUENA
# Very buena -> 1 amarillo
r_very_good = control.Rule((salinity['Medium'] & placement_depth['Medium'] &
                            ((temperature['Medium'] & currents['High'] & laminal_height['High'] & viscosity['Medium'] & density['Medium'] & depth['Low']) |
                             (temperature['Medium'] & currents['High'] & laminal_height['High'] & viscosity['Medium'] & density['Low'] & depth['Medium']) |
                             (temperature['Medium'] & currents['High'] & laminal_height['High'] & viscosity['Low'] & density['Medium'] & depth['Medium']) |
                             (temperature['Medium'] & currents['High'] & laminal_height['Medium'] & viscosity['Medium'] & density['Medium'] & depth['Medium']) |
                             (temperature['Medium'] & currents['Medium'] & laminal_height['High'] & viscosity['Medium'] & density['Medium'] & depth['Medium']) |
                             ((temperature['High'] | temperature['Low']) & currents['High'] & laminal_height['High'] & viscosity['Medium'] & density['Medium'] & depth['Medium']))),
                           turbines['Very Good'])

#                                                           TURBINA BUENA
# buena -> 2 amarillos
r_good = control.Rule((salinity['Medium'] & placement_depth['Medium'] &
                        (((temperature['High'] | temperature['Low']) & currents['Medium'] & laminal_height['High'] & viscosity['Medium'] & density['Medium'] & depth['Medium']) |
                         ((temperature['High'] | temperature['Low']) & currents['High'] & laminal_height['Medium'] & viscosity['Medium'] & density['Medium'] & depth['Medium']) |
                         ((temperature['High'] | temperature['Low']) & currents['High'] & laminal_height['High'] & viscosity['Low'] & density['Medium'] & depth['Medium']) |
                         ((temperature['High'] | temperature['Low']) & currents['High'] & laminal_height['High'] & viscosity['Medium'] & density['Low'] & depth['Medium']) |
                         ((temperature['High'] | temperature['Low']) & currents['High'] & laminal_height['High'] & viscosity['Medium'] & density['Medium'] & depth['Low']) |
                         (temperature['Medium'] & currents['Medium'] & laminal_height['Medium'] & viscosity['Medium'] & density['Medium'] & depth['Medium']) |
                         (temperature['Medium'] & currents['Medium'] & laminal_height['High'] & viscosity['Low'] & density['Medium'] & depth['Medium']) |
                         (temperature['Medium'] & currents['Medium'] & laminal_height['High'] & viscosity['Medium'] & density['Low'] & depth['Medium']) |
                         (temperature['Medium'] & currents['Medium'] & laminal_height['High'] & viscosity['Medium'] & density['Medium'] & depth['Low']) |
                         (temperature['Medium'] & currents['High'] & laminal_height['Medium'] & viscosity['Low'] & density['Medium'] & depth['Medium']) |
                         (temperature['Medium'] & currents['High'] & laminal_height['Medium'] & viscosity['Medium'] & density['Low'] & depth['Medium']) |
                         (temperature['Medium'] & currents['High'] & laminal_height['Medium'] & viscosity['Medium'] & density['Medium'] & depth['Low']) |
                         (temperature['Medium'] & currents['High'] & laminal_height['High'] & viscosity['Low'] & density['Low'] & depth['Medium']) |
                         (temperature['Medium'] & currents['High'] & laminal_height['High'] & viscosity['Low'] & density['Medium'] & depth['Low']) |
                         (temperature['Medium'] & currents['High'] & laminal_height['High'] & viscosity['Medium'] & density['Low'] & depth['Low']))),
                       turbines['Good'])

#                                                   TURBINA NO RECOMENDABLE
# el problema está en el ~ hay que cambiarlo por not pero control.Rule no acepta not, asi que hay que cambiarlo por las
#   leyes de negacion, ya que con ~ devuelve un valor numerico (0 en el caso q da error y entonces la membership no se puede
#   calculate bien)
# no recomendable por 1 naranja -> solo 1 naranja, 1 naranja + 0/1/2 amarillos
#                                ningun rojo
r_not_recommendable = control.Rule((((salinity['Medium'] &
                                    (temperature['High'] | temperature['Medium'] | temperature['Low']) &
                                    (currents['High'] | currents['Medium'] | currents['Low']) &
                                    (laminal_height['High'] | laminal_height['Medium'] | laminal_height['Low']) &
                                    (viscosity['Very Low'] | viscosity['Medium'] | viscosity['Low']) &
                                    (density['Medium'] | density['Low']) &
                                    (depth['Medium'] | depth['Low']) &
                                    (placement_depth['Medium'] | placement_depth['Low'])) &
                                   # no tod amarillo
                                   ((temperature['Medium'] & (currents['High'] | currents['Low']) &
                                     (laminal_height['High'] | laminal_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) &
                                     density['Medium'] & depth['Medium'] & (placement_depth['Medium'] | placement_depth['Low']))) &
                                   # no + 1 naranjas
                                   # corrientes naranja resto de otro
                                   ((currents['Low'] & (laminal_height['High'] | laminal_height['Medium']) & (viscosity['Medium'] | viscosity['Low']) & placement_depth['Medium']) |
                                    # altura laminal naranja resto de otro
                                    ((currents['High'] | currents['Medium']) & (laminal_height['Low']) & (viscosity['Medium'] | viscosity['Low']) & placement_depth['Medium']) |
                                    # viscosidad naranja resto de otro
                                    ((currents['High'] | currents['Medium']) & (laminal_height['High'] | laminal_height['Medium']) & (viscosity['Very Low']) & placement_depth['Medium']) |
                                    # prof colocacion naranja resto de otro
                                    ((currents['High'] | currents['Medium']) & (laminal_height['High'] | laminal_height['Medium']) & (viscosity['Medium'] | viscosity['Low']) & placement_depth['Low']))) &
                                  # salinidad será Medium si o si en este caso -> incluir
                                  ((salinity['Medium']) &
                                   # algun naranja y menos de 3 amarillos (0/1/2)
                                   #  no hay mas de 2 amarillos
                                   # temp y corrientes amarillo
                                   ((((temperature['Medium'] | (currents['High'] | currents['Low']) | (laminal_height['High'] | laminal_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] & depth['Medium'])
                                      & (temperature['Medium'] | (currents['High'] | currents['Low']) & (laminal_height['High'] | laminal_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] & depth['Medium'])
                                      & (temperature['Medium'] | (currents['High'] | currents['Low']) & (laminal_height['High'] | laminal_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) | density['Medium'] & depth['Medium'])
                                      & (temperature['Medium'] | (currents['High'] | currents['Low']) & (laminal_height['High'] | laminal_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] | depth['Medium'])
                                      & (temperature['Medium'] & (currents['High'] | currents['Low']) | (laminal_height['High'] | laminal_height['Low']) | (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] & depth['Medium'])
                                      & (temperature['Medium'] & (currents['High'] | currents['Low']) | (laminal_height['High'] | laminal_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) | density['Medium'] & depth['Medium'])
                                      & (temperature['Medium'] & (currents['High'] | currents['Low']) | (laminal_height['High'] | laminal_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] | depth['Medium'])
                                      & (temperature['Medium'] & (currents['High'] | currents['Low']) & (laminal_height['High'] | laminal_height['Low']) | (viscosity['Medium'] | viscosity['Very Low']) | density['Medium'] & depth['Medium'])
                                      & (temperature['Medium'] & (currents['High'] | currents['Low']) & (laminal_height['High'] | laminal_height['Low']) | (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] | depth['Medium'])
                                      & (temperature['Medium'] & (currents['High'] | currents['Low']) & (laminal_height['High'] | laminal_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) | density['Medium'] | depth['Medium']))) &
                                    # algun naranja
                                    (currents['Low'] | laminal_height['Low'] | viscosity['Very Low'] | placement_depth['Low'])) |
                                   # ningun naranja y hasta 5 amarillos
                                   #          ningun naranja
                                   (((currents['High'] | currents['Medium']) & (laminal_height['High'] | laminal_height['Medium']) & (viscosity['High'] | viscosity['Medium']) & placement_depth['Medium']) &
                                    # hasta 5 amarillos con min 3
                                    (((temperature['High'] | temperature['Low']) & currents['Medium'] &
                                      laminal_height['Medium'] | viscosity['Low'] | density['Low'] |
                                      depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) & currents['Medium'] |
                                        laminal_height['Medium'] & viscosity['Low'] | density['Low'] |
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) & currents['Medium'] |
                                        laminal_height['Medium'] | viscosity['Low'] & density['Low'] |
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) & currents['Medium'] |
                                        laminal_height['Medium'] | viscosity['Low'] | density['Low'] &
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] &
                                        laminal_height['Medium'] & viscosity['Low'] | density['Low'] |
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] &
                                        laminal_height['Medium'] | viscosity['Low'] & density['Low'] |
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] &
                                        laminal_height['Medium'] | viscosity['Low'] | density['Low'] &
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] |
                                        laminal_height['Medium'] & viscosity['Low'] & density['Low'] |
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] |
                                        laminal_height['Medium'] & viscosity['Low'] | density['Low'] &
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] |
                                        laminal_height['Medium'] | viscosity['Low'] & density['Low'] &
                                        depth['Low']))))),
                                   turbines['Not Recommendable'])

#                                                   TURBINA DESCARTADA
# todo check

#                               algun rojo
r_discarded = control.Rule((((salinity['High'] | salinity['Low'])
                              | (temperature['Very High'] | temperature['Very Low'])
                              | currents['Very Low']
                              | laminal_height['Very Low']
                              | viscosity['High']
                              | (density['High'] | density['Very Low'])
                              | (depth['High'] | depth['Very Low'])
                              | (placement_depth['High'] | placement_depth['Very Low'])) |
                             # al menos 2 naranjas
                             ((currents['Low'] & laminal_height['Low']) | (currents['Low'] & viscosity['Very Low']) |
                              (currents['Low'] & placement_depth['Low']) |
                              (laminal_height['Low'] & viscosity['Very Low']) |
                              (laminal_height['Low'] & placement_depth['Low']) |
                              (viscosity['Very Low'] & placement_depth['Low'])) |
                             # 1 naranja y 3 amarillos
                             #       al menos 1 naranja
                             ((currents['Low'] | laminal_height['Low'] | viscosity['Very Low'] | placement_depth['Low']) &
                              #      al menos 3 amarillos
                              (((temperature['High'] | temperature['Low']) & currents['Medium'] & laminal_height['Medium'] | viscosity['Low'] | density['Low'] | depth['Low'])
                               | ((temperature['High'] | temperature['Low']) & currents['Medium'] | laminal_height['Medium'] & viscosity['Low'] | density['Low'] | depth['Low'])
                               | ((temperature['High'] | temperature['Low']) & currents['Medium'] | laminal_height['Medium'] | viscosity['Low'] & density['Low'] | depth['Low'])
                               | ((temperature['High'] | temperature['Low']) & currents['Medium'] | laminal_height['Medium'] | viscosity['Low'] | density['Low'] & depth['Low'])
                               | ((temperature['High'] | temperature['Low']) | currents['Medium'] & laminal_height['Medium'] & viscosity['Low'] | density['Low'] | depth['Low'])
                               | ((temperature['High'] | temperature['Low']) | currents['Medium'] & laminal_height['Medium'] | viscosity['Low'] & density['Low'] | depth['Low'])
                               | ((temperature['High'] | temperature['Low']) | currents['Medium'] & laminal_height['Medium'] | viscosity['Low'] | density['Low'] & depth['Low'])
                               | ((temperature['High'] | temperature['Low']) | currents['Medium'] | laminal_height['Medium'] & viscosity['Low'] & density['Low'] | depth['Low'])
                               | ((temperature['High'] | temperature['Low']) | currents['Medium'] | laminal_height['Medium'] & viscosity['Low'] | density['Low'] & depth['Low'])
                               | ((temperature['High'] | temperature['Low']) | currents['Medium'] | laminal_height['Medium'] | viscosity['Low'] & density['Low'] & depth['Low']))) |
                             # descartada por min 6 amarillos (max de amarillos posibles -> todos los amarillos en am)
                             # salinidad y prof de colocacion da igual los valores
                             ((temperature['High'] | temperature['Low']) & currents['Medium'] & laminal_height['Medium']
                              & viscosity['Low'] & density['Low'] & depth['Low'])),
                            turbines['Discarded'])
