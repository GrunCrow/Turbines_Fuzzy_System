from skfuzzy import control
from Fuzzy_System.membership_functions import salinity, temperature, currents, laminar_height, viscosity, density, \
    depth, placement_depth, turbines

'''
Logic Rules Declaration for the System
'''

#                                                 OPTIMAL TURBINE
# optimal -> all green
r_optimal = control.Rule((salinity['Medium'] & temperature['Medium'] & currents['High'] & laminar_height['High'] &
                         viscosity['Medium'] & density['Medium'] & depth['Medium'] &
                         placement_depth['Medium']),
                         turbines['Optimal'])

#                                                   VERY GOOD TURBINE
# Very Good -> 1 yellow
r_very_good = control.Rule((salinity['Medium'] & placement_depth['Medium'] &
                            ((temperature['Medium'] & currents['High'] & laminar_height['High'] & viscosity['Medium'] & density['Medium'] & depth['Low']) |
                             (temperature['Medium'] & currents['High'] & laminar_height['High'] & viscosity['Medium'] & density['Low'] & depth['Medium']) |
                             (temperature['Medium'] & currents['High'] & laminar_height['High'] & viscosity['Low'] & density['Medium'] & depth['Medium']) |
                             (temperature['Medium'] & currents['High'] & laminar_height['Medium'] & viscosity['Medium'] & density['Medium'] & depth['Medium']) |
                             (temperature['Medium'] & currents['Medium'] & laminar_height['High'] & viscosity['Medium'] & density['Medium'] & depth['Medium']) |
                             ((temperature['High'] | temperature['Low']) & currents['High'] & laminar_height['High'] & viscosity['Medium'] & density['Medium'] & depth['Medium']))),
                           turbines['Very Good'])

#                                                           GOOD TURBINE
# good -> 2 yellows
r_good = control.Rule((salinity['Medium'] & placement_depth['Medium'] &
                       (((temperature['High'] | temperature['Low']) & currents['Medium'] & laminar_height['High'] & viscosity['Medium'] & density['Medium'] & depth['Medium']) |
                        ((temperature['High'] | temperature['Low']) & currents['High'] & laminar_height['Medium'] & viscosity['Medium'] & density['Medium'] & depth['Medium']) |
                        ((temperature['High'] | temperature['Low']) & currents['High'] & laminar_height['High'] & viscosity['Low'] & density['Medium'] & depth['Medium']) |
                        ((temperature['High'] | temperature['Low']) & currents['High'] & laminar_height['High'] & viscosity['Medium'] & density['Low'] & depth['Medium']) |
                        ((temperature['High'] | temperature['Low']) & currents['High'] & laminar_height['High'] & viscosity['Medium'] & density['Medium'] & depth['Low']) |
                        (temperature['Medium'] & currents['Medium'] & laminar_height['Medium'] & viscosity['Medium'] & density['Medium'] & depth['Medium']) |
                        (temperature['Medium'] & currents['Medium'] & laminar_height['High'] & viscosity['Low'] & density['Medium'] & depth['Medium']) |
                        (temperature['Medium'] & currents['Medium'] & laminar_height['High'] & viscosity['Medium'] & density['Low'] & depth['Medium']) |
                        (temperature['Medium'] & currents['Medium'] & laminar_height['High'] & viscosity['Medium'] & density['Medium'] & depth['Low']) |
                        (temperature['Medium'] & currents['High'] & laminar_height['Medium'] & viscosity['Low'] & density['Medium'] & depth['Medium']) |
                        (temperature['Medium'] & currents['High'] & laminar_height['Medium'] & viscosity['Medium'] & density['Low'] & depth['Medium']) |
                        (temperature['Medium'] & currents['High'] & laminar_height['Medium'] & viscosity['Medium'] & density['Medium'] & depth['Low']) |
                        (temperature['Medium'] & currents['High'] & laminar_height['High'] & viscosity['Low'] & density['Low'] & depth['Medium']) |
                        (temperature['Medium'] & currents['High'] & laminar_height['High'] & viscosity['Low'] & density['Medium'] & depth['Low']) |
                        (temperature['Medium'] & currents['High'] & laminar_height['High'] & viscosity['Medium'] & density['Low'] & depth['Low']))),
                      turbines['Good'])

#                                                    NOT RECOMMENDABLE TURBINE
# the problem is in the ~ you have to change it to not but control.Rule does not accept not, so you have to change it to
# negation laws, since with ~ it returns a numeric value (0 in the case that gives an error and then the membership cannot be
# calculated well)
# not recommendable for 1 orange -> just 1 orange, 1 orange + 0/1/2 yellows
#                                no red
r_not_recommendable = control.Rule((((salinity['Medium'] &
                                    (temperature['High'] | temperature['Medium'] | temperature['Low']) &
                                    (currents['High'] | currents['Medium'] | currents['Low']) &
                                    (laminar_height['High'] | laminar_height['Medium'] | laminar_height['Low']) &
                                    (viscosity['Very Low'] | viscosity['Medium'] | viscosity['Low']) &
                                    (density['Medium'] | density['Low']) &
                                    (depth['Medium'] | depth['Low']) &
                                    (placement_depth['Medium'] | placement_depth['Low'])) &
                                   # no all yellow
                                   ((temperature['Medium'] & (currents['High'] | currents['Low']) &
                                     (laminar_height['High'] | laminar_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) &
                                     density['Medium'] & depth['Medium'] & (placement_depth['Medium'] | placement_depth['Low']))) &
                                   # no + 1 oranges
                                   # currents orange others are other color
                                   ((currents['Low'] & (laminar_height['High'] | laminar_height['Medium']) & (viscosity['Medium'] | viscosity['Low']) & placement_depth['Medium']) |
                                    # laminar height orange others are other color
                                    ((currents['High'] | currents['Medium']) & (laminar_height['Low']) & (viscosity['Medium'] | viscosity['Low']) & placement_depth['Medium']) |
                                    # viscosity orange others are other color
                                    ((currents['High'] | currents['Medium']) & (laminar_height['High'] | laminar_height['Medium']) & (viscosity['Very Low']) & placement_depth['Medium']) |
                                    # placement depth orange others are other color
                                    ((currents['High'] | currents['Medium']) & (laminar_height['High'] | laminar_height['Medium']) & (viscosity['Medium'] | viscosity['Low']) & placement_depth['Low']))) &
                                  # salinity will be Medium in this case -> include
                                  ((salinity['Medium']) &
                                   # any orange and less than 3 yellows (0/1/2)
                                   #  no more than 2 yellows
                                   # temp and currents yellow
                                   ((((temperature['Medium'] | (currents['High'] | currents['Low']) | (laminar_height['High'] | laminar_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] & depth['Medium'])
                                      & (temperature['Medium'] | (currents['High'] | currents['Low']) & (laminar_height['High'] | laminar_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] & depth['Medium'])
                                      & (temperature['Medium'] | (currents['High'] | currents['Low']) & (laminar_height['High'] | laminar_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) | density['Medium'] & depth['Medium'])
                                      & (temperature['Medium'] | (currents['High'] | currents['Low']) & (laminar_height['High'] | laminar_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] | depth['Medium'])
                                      & (temperature['Medium'] & (currents['High'] | currents['Low']) | (laminar_height['High'] | laminar_height['Low']) | (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] & depth['Medium'])
                                      & (temperature['Medium'] & (currents['High'] | currents['Low']) | (laminar_height['High'] | laminar_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) | density['Medium'] & depth['Medium'])
                                      & (temperature['Medium'] & (currents['High'] | currents['Low']) | (laminar_height['High'] | laminar_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] | depth['Medium'])
                                      & (temperature['Medium'] & (currents['High'] | currents['Low']) & (laminar_height['High'] | laminar_height['Low']) | (viscosity['Medium'] | viscosity['Very Low']) | density['Medium'] & depth['Medium'])
                                      & (temperature['Medium'] & (currents['High'] | currents['Low']) & (laminar_height['High'] | laminar_height['Low']) | (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] | depth['Medium'])
                                      & (temperature['Medium'] & (currents['High'] | currents['Low']) & (laminar_height['High'] | laminar_height['Low']) & (viscosity['Medium'] | viscosity['Very Low']) | density['Medium'] | depth['Medium']))) &
                                    # any orange
                                    (currents['Low'] | laminar_height['Low'] | viscosity['Very Low'] | placement_depth['Low'])) |
                                   # no orange and 5 yellows max
                                   #          no orange
                                   (((currents['High'] | currents['Medium']) & (laminar_height['High'] | laminar_height['Medium']) & (viscosity['High'] | viscosity['Medium']) & placement_depth['Medium']) &
                                    # max 5 yellows with min 3
                                    (((temperature['High'] | temperature['Low']) & currents['Medium'] &
                                      laminar_height['Medium'] | viscosity['Low'] | density['Low'] |
                                      depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) & currents['Medium'] |
                                        laminar_height['Medium'] & viscosity['Low'] | density['Low'] |
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) & currents['Medium'] |
                                        laminar_height['Medium'] | viscosity['Low'] & density['Low'] |
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) & currents['Medium'] |
                                        laminar_height['Medium'] | viscosity['Low'] | density['Low'] &
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] &
                                        laminar_height['Medium'] & viscosity['Low'] | density['Low'] |
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] &
                                        laminar_height['Medium'] | viscosity['Low'] & density['Low'] |
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] &
                                        laminar_height['Medium'] | viscosity['Low'] | density['Low'] &
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] |
                                        laminar_height['Medium'] & viscosity['Low'] & density['Low'] |
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] |
                                        laminar_height['Medium'] & viscosity['Low'] | density['Low'] &
                                        depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] |
                                        laminar_height['Medium'] | viscosity['Low'] & density['Low'] &
                                        depth['Low']))))),
                                   turbines['Not Recommendable'])

#                                                  DISCARDED TURBINE
# todo check

#                               any red
r_discarded = control.Rule((((salinity['High'] | salinity['Low'])
                             | (temperature['Very High'] | temperature['Very Low'])
                             | currents['Very Low']
                             | laminar_height['Very Low']
                             | viscosity['High']
                             | (density['High'] | density['Very Low'])
                             | (depth['High'] | depth['Very Low'])
                             | (placement_depth['High'] | placement_depth['Very Low'])) |
                            # at least 2 oranges
                            ((currents['Low'] & laminar_height['Low']) | (currents['Low'] & viscosity['Very Low']) |
                             (currents['Low'] & placement_depth['Low']) |
                             (laminar_height['Low'] & viscosity['Very Low']) |
                             (laminar_height['Low'] & placement_depth['Low']) |
                             (viscosity['Very Low'] & placement_depth['Low'])) |
                            # 1 orange and 3 yellows
                            #       at least 1 orange
                            ((currents['Low'] | laminar_height['Low'] | viscosity['Very Low'] | placement_depth['Low']) &
                             #      at least 3 yellows
                              (((temperature['High'] | temperature['Low']) & currents['Medium'] & laminar_height['Medium'] | viscosity['Low'] | density['Low'] | depth['Low'])
                               | ((temperature['High'] | temperature['Low']) & currents['Medium'] | laminar_height['Medium'] & viscosity['Low'] | density['Low'] | depth['Low'])
                               | ((temperature['High'] | temperature['Low']) & currents['Medium'] | laminar_height['Medium'] | viscosity['Low'] & density['Low'] | depth['Low'])
                               | ((temperature['High'] | temperature['Low']) & currents['Medium'] | laminar_height['Medium'] | viscosity['Low'] | density['Low'] & depth['Low'])
                               | ((temperature['High'] | temperature['Low']) | currents['Medium'] & laminar_height['Medium'] & viscosity['Low'] | density['Low'] | depth['Low'])
                               | ((temperature['High'] | temperature['Low']) | currents['Medium'] & laminar_height['Medium'] | viscosity['Low'] & density['Low'] | depth['Low'])
                               | ((temperature['High'] | temperature['Low']) | currents['Medium'] & laminar_height['Medium'] | viscosity['Low'] | density['Low'] & depth['Low'])
                               | ((temperature['High'] | temperature['Low']) | currents['Medium'] | laminar_height['Medium'] & viscosity['Low'] & density['Low'] | depth['Low'])
                               | ((temperature['High'] | temperature['Low']) | currents['Medium'] | laminar_height['Medium'] & viscosity['Low'] | density['Low'] & depth['Low'])
                               | ((temperature['High'] | temperature['Low']) | currents['Medium'] | laminar_height['Medium'] | viscosity['Low'] & density['Low'] & depth['Low']))) |
                            # discarded for min 6 yellows (max of yellows possible -> all with yellows in yellow)
                            # salinity y placement depth (no mather the values)
                            ((temperature['High'] | temperature['Low']) & currents['Medium'] & laminar_height['Medium']
                             & viscosity['Low'] & density['Low'] & depth['Low'])),
                           turbines['Discarded'])
