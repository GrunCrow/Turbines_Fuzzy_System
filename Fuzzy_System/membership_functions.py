from Fuzzy_System.FuzzyVariable import salinity, temperature, currents, laminal_height, viscosity, density, depth, \
    placement_depth, turbines
import skfuzzy as fuzz

# trimf for triangular -> (0,4,8) - pico en el 4 y va de 0 a 8 las laterales
# trapmf for trapezoidal -> (8,12,20,25) - empieza en 8 y la primera arista hacia arriba en 12,
#                           la siguiente lateral la une con 20 (seria valor 1) y la siguiente (25) para abajo hacia el 0

#                                                                INPUTS
#   Salinidad       (20, 50)
salinity['Low'] = fuzz.trapmf(salinity.universe, [20, 20, 26, 33])
salinity['Medium'] = fuzz.trapmf(salinity.universe, [30, 33, 37, 40])
salinity['High'] = fuzz.trapmf(salinity.universe, [37, 45, 50, 50])

# salinidad.view()

#   Temperatura     (-20, 50, 0.1).round(1)
temperature['Very Low'] = fuzz.trapmf(temperature.universe, [-20, -20, -10, 0])
temperature['Low'] = fuzz.trimf(temperature.universe, [-5, 7, 15])
temperature['Medium'] = fuzz.trapmf(temperature.universe, [12, 15, 23, 27])
temperature['High'] = fuzz.trimf(temperature.universe, [25, 27, 35])
temperature['Very High'] = fuzz.trapmf(temperature.universe, [30, 40, 50, 50])

# temperatura.view()

#   corrientes     (0, 300)
currents['Very Low'] = fuzz.trapmf(currents.universe, [0, 0, 50, 100])
currents['Low'] = fuzz.trimf(currents.universe, [70, 130, 180])
currents['Medium'] = fuzz.trimf(currents.universe, [170, 200, 220])
currents['High'] = fuzz.trapmf(currents.universe, [210, 255, 300, 300])

# corrientes.view()

#   Altura Laminal     (0, 100)
laminal_height['Very Low'] = fuzz.trapmf(laminal_height.universe, [0, 0, 10, 25])
laminal_height['Low'] = fuzz.trimf(laminal_height.universe, [20, 30, 45])
laminal_height['Medium'] = fuzz.trimf(laminal_height.universe, [40, 50, 70])
laminal_height['High'] = fuzz.trapmf(laminal_height.universe, [60, 80, 100, 100])

# altura_laminal.view()

#   viscosidad     (0, 2, 0.01)
viscosity['Very Low'] = fuzz.trapmf(viscosity.universe, [0.3, 0.3, 0.4, 0.70])
viscosity['Low'] = fuzz.trimf(viscosity.universe, [0.50, 0.85, 1.10])
viscosity['Medium'] = fuzz.trimf(viscosity.universe, [1.00, 1.55, 1.90])
viscosity['High'] = fuzz.trapmf(viscosity.universe, [1.75, 1.95, 2, 2])

# viscosidad.view()

#   densidad     (900, 1100)
density['Very Low'] = fuzz.trapmf(density.universe, [900, 900, 925, 950])
density['Low'] = fuzz.trimf(density.universe, [925, 950, 975])
density['Medium'] = fuzz.trimf(density.universe, [950, 1000, 1050])
density['High'] = fuzz.trapmf(density.universe, [1025, 1050, 1100, 1100])

# densidad.view()

#   profundidad     (0, 7000)
depth['Very Low'] = fuzz.trapmf(depth.universe, [0, 0, 3, 5])
depth['Low'] = fuzz.trimf(depth.universe, [2, 6, 10])
depth['Medium'] = fuzz.trimf(depth.universe, [5, 500, 1000])
depth['High'] = fuzz.trapmf(depth.universe, [800, 1000, 7000, 7000])

# profundidad.view()

#   profundidad colocacion     (0, 150)
placement_depth['Very Low'] = fuzz.trapmf(placement_depth.universe, [0, 0, 1, 2])
placement_depth['Low'] = fuzz.trimf(placement_depth.universe, [1, 3, 5])
placement_depth['Medium'] = fuzz.trimf(placement_depth.universe, [3, 10, 20])
placement_depth['High'] = fuzz.trapmf(placement_depth.universe, [20, 50, 150, 150])

# profundidad_colocacion.view()

#                                                                           OUTPUTS

#   turbina 0-100 %
turbines['Discarded'] = fuzz.trapmf(turbines.universe, [0, 0, 30, 50])
turbines['Not Recommendable'] = fuzz.trimf(turbines.universe, [40, 60, 70])
turbines['Good'] = fuzz.trimf(turbines.universe, [65, 80, 85])
turbines['Very Good'] = fuzz.trimf(turbines.universe, [80, 85, 90])
turbines['Optimal'] = fuzz.trapmf(turbines.universe, [85, 95, 100, 100])
