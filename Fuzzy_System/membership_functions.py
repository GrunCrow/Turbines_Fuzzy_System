from Turbines_Fuzzy_System.Fuzzy_System.FuzzyVariable import salinity, temperature, currents, viscosity, density, depth, \
    placement_depth, turbines
import skfuzzy as fuzz

# trimf for triangular -> (0,4,8) - peak in 4 and from 0 to 8 (laterals)
# trapmf for trapezoidal -> (8,12,20,25) - start in 8 and first edge goes to 12,
#                           the next edge connects it with 20 (it will be value 1) and next (25) down to 0

#                                                                INPUTS
#   Salinity       (0, 40)
salinity['Low'] = fuzz.trapmf(salinity.universe, [0, 0, 20, 30])
salinity['Medium'] = fuzz.trapmf(salinity.universe, [20, 30, 100, 150])
salinity['High'] = fuzz.trapmf(salinity.universe, [100, 150, 400, 400])

#   Temperature     (-5, 40, 0.1).round(1)
temperature['Very Low'] = fuzz.trapmf(temperature.universe, [-5, -5, 0, 0])
temperature['Low'] = fuzz.trapmf(temperature.universe, [-5, 0, 7, 15])
temperature['Medium'] = fuzz.trapmf(temperature.universe, [7, 15, 30, 35])
temperature['High'] = fuzz.trimf(temperature.universe, [30, 35, 37])
temperature['Very High'] = fuzz.trapmf(temperature.universe, [35, 37, 40, 40])

#   currents     (0, 300)
currents['Very Low'] = fuzz.trapmf(currents.universe, [0, 0, 50, 100])
currents['Low'] = fuzz.trapmf(currents.universe, [50, 100, 160, 180])
currents['Medium'] = fuzz.trimf(currents.universe, [160, 180, 220])
currents['High'] = fuzz.trapmf(currents.universe, [180, 220, 300, 300])

#   viscosity     (0, 2, 0.01)
viscosity['Very Low'] = fuzz.trapmf(viscosity.universe, [0, 0.0, 0.4, 0.70])
viscosity['Low'] = fuzz.trapmf(viscosity.universe, [0.4, 0.7, 0.85, 1.10])
viscosity['Medium'] = fuzz.trapmf(viscosity.universe, [0.85, 1.10, 1.55, 1.90])
viscosity['High'] = fuzz.trapmf(viscosity.universe, [1.55, 1.9, 2, 2])

#   density     (900, 1100)
density['Very Low'] = fuzz.trapmf(density.universe, [900, 900, 925, 950])
density['Low'] = fuzz.trimf(density.universe, [925, 1000, 1030])
density['Medium'] = fuzz.trapmf(density.universe, [1000, 1030, 1040, 1050])
density['High'] = fuzz.trapmf(density.universe, [1040, 1050, 1100, 1100])

#   depth     (0, 8000)
depth['Very Low'] = fuzz.trapmf(depth.universe, [0, 0, 3, 5])
depth['Low'] = fuzz.trimf(depth.universe, [3, 5, 10])
depth['Medium'] = fuzz.trapmf(depth.universe, [5, 10, 500, 1000])
depth['High'] = fuzz.trapmf(depth.universe, [500, 1000, 8000, 8000])

#   placement depth     (0, 150)
placement_depth['Very Low'] = fuzz.trapmf(placement_depth.universe, [0, 0, 1, 2])
placement_depth['Low'] = fuzz.trimf(placement_depth.universe, [1, 2, 5])
placement_depth['Medium'] = fuzz.trapmf(placement_depth.universe, [2, 5, 10, 20])
placement_depth['High'] = fuzz.trapmf(placement_depth.universe, [10, 20, 150, 150])

#                                                                     OUTPUTS

#   turbine 0-100 %
turbines['Discarded'] = fuzz.trapmf(turbines.universe, [0, 0, 30, 50])
turbines['Not Recommendable'] = fuzz.trimf(turbines.universe, [30, 50, 70])
turbines['Good'] = fuzz.trapmf(turbines.universe, [50, 70, 80, 85])
turbines['Very Good'] = fuzz.trimf(turbines.universe, [80, 85, 90])
turbines['Optimal'] = fuzz.trapmf(turbines.universe, [85, 90, 100, 100])

def show_functions():
    salinity.view()
    temperature.view()
    currents.view()
    viscosity.view()
    density.view()
    depth.view()
    placement_depth.view()

# show_functions()
