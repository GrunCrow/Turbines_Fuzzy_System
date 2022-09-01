from Fuzzy_System.FuzzyVariable import salinity, temperature, currents, laminar_height, viscosity, density, depth, \
    placement_depth, turbines
import skfuzzy as fuzz

# trimf for triangular -> (0,4,8) - peak in 4 and from 0 to 8 (laterals)
# trapmf for trapezoidal -> (8,12,20,25) - start in 8 and first edge goes to 12,
#                           the next edge connects it with 20 (it will be value 1) and next (25) down to 0

#                                                                INPUTS
#   Salinity       (20, 50)
salinity['Low'] = fuzz.trapmf(salinity.universe, [20, 20, 26, 33])
salinity['Medium'] = fuzz.trapmf(salinity.universe, [30, 33, 37, 40])
salinity['High'] = fuzz.trapmf(salinity.universe, [37, 45, 50, 50])

# salinity.view()

#   Temperature     (-20, 50, 0.1).round(1)
temperature['Very Low'] = fuzz.trapmf(temperature.universe, [-20, -20, -10, 0])
temperature['Low'] = fuzz.trimf(temperature.universe, [-5, 7, 15])
temperature['Medium'] = fuzz.trapmf(temperature.universe, [12, 15, 23, 27])
temperature['High'] = fuzz.trimf(temperature.universe, [25, 27, 35])
temperature['Very High'] = fuzz.trapmf(temperature.universe, [30, 40, 50, 50])

# temperature.view()

#   currents     (0, 300)
currents['Very Low'] = fuzz.trapmf(currents.universe, [0, 0, 50, 100])
currents['Low'] = fuzz.trimf(currents.universe, [70, 130, 180])
currents['Medium'] = fuzz.trimf(currents.universe, [170, 200, 220])
currents['High'] = fuzz.trapmf(currents.universe, [210, 255, 300, 300])

# currents.view()

#   Laminar Height   (0, 100)
laminar_height['Very Low'] = fuzz.trapmf(laminar_height.universe, [0, 0, 10, 25])
laminar_height['Low'] = fuzz.trimf(laminar_height.universe, [20, 30, 45])
laminar_height['Medium'] = fuzz.trimf(laminar_height.universe, [40, 50, 70])
laminar_height['High'] = fuzz.trapmf(laminar_height.universe, [60, 80, 100, 100])

# laminar_height.view()

#   viscosity     (0, 2, 0.01)
viscosity['Very Low'] = fuzz.trapmf(viscosity.universe, [0.3, 0.3, 0.4, 0.70])
viscosity['Low'] = fuzz.trimf(viscosity.universe, [0.50, 0.85, 1.10])
viscosity['Medium'] = fuzz.trimf(viscosity.universe, [1.00, 1.55, 1.90])
viscosity['High'] = fuzz.trapmf(viscosity.universe, [1.75, 1.95, 2, 2])

# viscosity.view()

#   density     (900, 1100)
density['Very Low'] = fuzz.trapmf(density.universe, [900, 900, 925, 950])
density['Low'] = fuzz.trimf(density.universe, [925, 950, 975])
density['Medium'] = fuzz.trimf(density.universe, [950, 1000, 1050])
density['High'] = fuzz.trapmf(density.universe, [1025, 1050, 1100, 1100])

# density.view()

#   depth     (0, 7000)
depth['Very Low'] = fuzz.trapmf(depth.universe, [0, 0, 3, 5])
depth['Low'] = fuzz.trimf(depth.universe, [2, 6, 10])
depth['Medium'] = fuzz.trimf(depth.universe, [5, 500, 1000])
depth['High'] = fuzz.trapmf(depth.universe, [800, 1000, 7000, 7000])

# depth.view()

#   placement depth     (0, 150)
placement_depth['Very Low'] = fuzz.trapmf(placement_depth.universe, [0, 0, 1, 2])
placement_depth['Low'] = fuzz.trimf(placement_depth.universe, [1, 3, 5])
placement_depth['Medium'] = fuzz.trimf(placement_depth.universe, [3, 10, 20])
placement_depth['High'] = fuzz.trapmf(placement_depth.universe, [20, 50, 150, 150])

# placement_depth.view()

#                                                                           OUTPUTS

#   turbine 0-100 %
turbines['Discarded'] = fuzz.trapmf(turbines.universe, [0, 0, 30, 50])
turbines['Not Recommendable'] = fuzz.trimf(turbines.universe, [40, 60, 70])
turbines['Good'] = fuzz.trimf(turbines.universe, [65, 80, 85])
turbines['Very Good'] = fuzz.trimf(turbines.universe, [80, 85, 90])
turbines['Optimal'] = fuzz.trapmf(turbines.universe, [85, 95, 100, 100])
