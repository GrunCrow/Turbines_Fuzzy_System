from skfuzzy import control
from Fuzzy_System.membership_functions import salinity, temperature, currents, viscosity, density, \
    depth, placement_depth, turbines

'''
Logic Rules Declaration for the System
'''

#                                                 OPTIMAL TURBINE
# optimal -> all green
r_optimal = control.Rule((salinity['Medium'] & temperature['Medium'] & currents['High'] & viscosity['Medium'] &
                          density['Medium'] & depth['Medium'] & placement_depth['Medium']),
                         turbines['Optimal'])

#                                                   VERY GOOD TURBINE
# Very Good -> 1 yellow
r_very_good = control.Rule((salinity['Medium'] & placement_depth['Medium'] &
                            # depth yellow
                            ((temperature['Medium'] & currents['High'] & viscosity['Medium'] & density['Medium'] & depth['Low']) |
                             # density yellow
                             (temperature['Medium'] & currents['High'] & viscosity['Medium'] & density['Low'] & depth['Medium']) |
                             # viscosity yellow
                             (temperature['Medium'] & currents['High'] & viscosity['Low'] & density['Medium'] & depth['Medium']) |
                             # currents yellow
                             (temperature['Medium'] & currents['Medium'] & viscosity['Medium'] & density['Medium'] & depth['Medium']) |
                             # temperature yellow
                             ((temperature['High'] | temperature['Low']) & currents['High'] & viscosity['Medium'] & density['Medium'] & depth['Medium']))),
                           turbines['Very Good'])

#                                                           GOOD TURBINE
# good -> 2 yellows
r_good = control.Rule((salinity['Medium'] & placement_depth['Medium'] &
                       # temperature and currents yellow
                       (((temperature['High'] | temperature['Low']) & currents['Medium'] & viscosity['Medium'] & density['Medium'] & depth['Medium']) |
                        # temperature and viscosity yellow
                        ((temperature['High'] | temperature['Low']) & currents['High'] & viscosity['Low'] & density['Medium'] & depth['Medium']) |
                        # temperature and density yellow
                        ((temperature['High'] | temperature['Low']) & currents['High'] & viscosity['Medium'] & density['Low'] & depth['Medium']) |
                        # temperature and depth yellow
                        ((temperature['High'] | temperature['Low']) & currents['High'] & viscosity['Medium'] & density['Medium'] & depth['Low']) |

                        # currents and viscosity yellow
                        (temperature['Medium'] & currents['Medium'] & viscosity['Low'] & density['Medium'] & depth['Medium']) |
                        # currents and density yellow
                        (temperature['Medium'] & currents['Medium'] & viscosity['Medium'] & density['Low'] & depth['Medium']) |
                        # currents and depth yellow
                        (temperature['Medium'] & currents['Medium'] & viscosity['Medium'] & density['Medium'] & depth['Low']) |

                        # viscosity and density yellow
                        (temperature['Medium'] & currents['High'] & viscosity['Low'] & density['Low'] & depth['Medium']) |
                        # viscosity and depth yellow
                        (temperature['Medium'] & currents['High'] & viscosity['Low'] & density['Medium'] & depth['Low']) |

                        # density and depth yellow
                        (temperature['Medium'] & currents['High'] & viscosity['Medium'] & density['Low'] & depth['Low']))),
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
                                    (viscosity['Very Low'] | viscosity['Medium'] | viscosity['Low']) &
                                    (density['Medium'] | density['Low']) &
                                    (depth['Medium'] | depth['Low']) &
                                    (placement_depth['Medium'] | placement_depth['Low'])) &

                                   # no + 1 oranges
                                   # currents orange others are other color
                                   ((currents['Low'] & (viscosity['Medium'] | viscosity['Low']) & placement_depth['Medium']) |
                                    # viscosity orange others are other color
                                    ((currents['High'] | currents['Medium']) & (viscosity['Very Low']) & placement_depth['Medium']) |
                                    # placement depth orange others are other color
                                    ((currents['High'] | currents['Medium']) & (viscosity['Medium'] | viscosity['Low']) & placement_depth['Low']))) &


                                  # any orange and less than 3 yellows (0/1/2)
                                  # no need to specify salinity as it will always be medium (no red) also placement_Depth here will be orange or green (no_red)

                                  # any orange but no more than 1 (no + 1 orange)
                                  ((currents['Low'] | viscosity['Very Low'] | placement_depth['Low']) &

                                  # 0 yellow -> as we already count with max 1 orange, for the param with orange,
                                  # it can be orange or green as it will be only 1 orange
                                   ((temperature['Medium'] & (currents['High'] | currents['Low']) &
                                   (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] & depth['Medium']) |

                                  # 1 yellow
                                   # depth yellow
                                   ((temperature['Medium'] & (currents['High'] | currents['Low']) & (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] & depth['Low']) |
                                    # density yellow
                                    (temperature['Medium'] & (currents['High'] | currents['Low']) & (viscosity['Medium'] | viscosity['Very Low']) & density['Low'] & depth['Medium']) |
                                    # viscosity yellow
                                    (temperature['Medium'] & (currents['High'] | currents['Low']) & viscosity['Low'] & density['Medium'] & depth['Medium']) |
                                    # currents yellow
                                    (temperature['Medium'] & currents['Medium'] & (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] & depth['Medium']) |
                                    # temperature yellow
                                    ((temperature['High'] | temperature['Low']) & (currents['High'] | currents['Low']) & (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] & depth['Medium'])) |

                                  # 2 yellow
                                     # temperature and currents yellow
                                     (((temperature['High'] | temperature['Low']) & currents['Medium'] & viscosity['Medium'] & (viscosity['Medium'] | viscosity['Very Low']) & depth['Medium']) |
                                      # temperature and viscosity yellow
                                      ((temperature['High'] | temperature['Low']) & (currents['High'] | currents['Low']) & viscosity['Low'] & (viscosity['Medium'] | viscosity['Very Low']) & depth['Medium']) |
                                      # temperature and density yellow
                                      ((temperature['High'] | temperature['Low']) & (currents['High'] | currents['Low']) & viscosity['Medium'] & density['Low'] & depth['Medium']) |
                                      # temperature and depth yellow
                                      ((temperature['High'] | temperature['Low']) & (currents['High'] | currents['Low']) & viscosity['Medium'] & (viscosity['Medium'] | viscosity['Very Low']) & depth['Low']) |

                                      # currents and viscosity yellow
                                      (temperature['Medium'] & currents['Medium'] & viscosity['Low'] & density['Medium'] & depth['Medium']) |
                                      # currents and density yellow
                                      (temperature['Medium'] & currents['Medium'] & (viscosity['Medium'] | viscosity['Very Low']) & density['Low'] & depth['Medium']) |
                                      # currents and depth yellow
                                      (temperature['Medium'] & currents['Medium'] & (viscosity['Medium'] | viscosity['Very Low']) & density['Medium'] & depth['Low']) |

                                      # viscosity and density yellow
                                      (temperature['Medium'] & (currents['High'] | currents['Low']) & viscosity['Low'] & density['Low'] & depth['Medium']) |
                                      # viscosity and depth yellow
                                      (temperature['Medium'] & (currents['High'] | currents['Low']) & viscosity['Low'] & density['Medium'] & depth['Low']) |

                                      # density and depth yellow
                                      (temperature['Medium'] & (currents['High'] | currents['Low']) & (viscosity['Medium'] | viscosity['Very Low']) & density['Low'] & depth['Low'])))) |


                                   # no orange and 5 yellows max
                                   #          no orange
                                   (((currents['High'] | currents['Medium']) & (viscosity['High'] | viscosity['Medium']) & placement_depth['Medium']) &
                                    # max 5 yellows with min 3
                                    (((temperature['High'] | temperature['Low']) & currents['Medium'] & viscosity['Low'] | density['Low'] | depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) & currents['Medium'] | viscosity['Low'] & density['Low'] | depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) & currents['Medium'] | viscosity['Low'] | density['Low'] & depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] & viscosity['Low'] & density['Low'] | depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] & viscosity['Low'] | density['Low'] & depth['Low'])
                                     | ((temperature['High'] | temperature['Low']) | currents['Medium'] | viscosity['Low'] & density['Low'] & depth['Low'])))),
                                   turbines['Not Recommendable'])

#                                                  DISCARDED TURBINE
# todo check

#                               any red
r_discarded = control.Rule((((salinity['High'] | salinity['Low'])
                             | (temperature['Very High'] | temperature['Very Low'])
                             | currents['Very Low']
                             | viscosity['High']
                             | (density['High'] | density['Very Low'])
                             | (depth['High'] | depth['Very Low'])
                             | (placement_depth['High'] | placement_depth['Very Low'])) |
                            # at least 2 oranges
                            ((currents['Low'] & viscosity['Very Low']) | (currents['Low'] & placement_depth['Low']) |
                             (viscosity['Very Low'] & placement_depth['Low'])) |
                            # 1 orange and 3 yellows
                            #       at least 1 orange
                            ((currents['Low'] | viscosity['Very Low'] | placement_depth['Low']) &
                             #      at least 3 yellows
                             (((temperature['High'] | temperature['Low']) & currents['Medium'] & viscosity['Low'] | density['Low'] | depth['Low'])
                              | ((temperature['High'] | temperature['Low']) & currents['Medium'] | viscosity['Low'] & density['Low'] | depth['Low'])
                              | ((temperature['High'] | temperature['Low']) & currents['Medium'] | viscosity['Low'] | density['Low'] & depth['Low'])
                              | ((temperature['High'] | temperature['Low']) | currents['Medium'] & viscosity['Low'] & density['Low'] | depth['Low'])
                              | ((temperature['High'] | temperature['Low']) | currents['Medium'] & viscosity['Low'] | density['Low'] & depth['Low'])
                              | ((temperature['High'] | temperature['Low']) | currents['Medium'] | viscosity['Low'] & density['Low'] & depth['Low'])))
                            # discarded for min 6 yellows (max of yellows possible = 5 -> it is not possible)
                            ),
                           turbines['Discarded'])
