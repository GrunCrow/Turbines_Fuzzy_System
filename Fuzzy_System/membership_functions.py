from Fuzzy_System.FuzzyVariable import salinidad, temperatura, corrientes, altura_laminal, viscosidad, densidad, profundidad, \
    profundidad_colocacion, turbinas
import skfuzzy as fuzz

# trimf for triangular -> (0,4,8) - pico en el 4 y va de 0 a 8 las laterales
# trapmf for trapezoidal -> (8,12,20,25) - empieza en 8 y la primera arista hacia arriba en 12,
#                           la siguiente lateral la une con 20 (seria valor 1) y la siguiente (25) para abajo hacia el 0

#                                                                INPUTS
#   Salinidad       (20, 50)
salinidad['Baja'] = fuzz.trapmf(salinidad.universe, [20, 20, 26, 33])
salinidad['Media'] = fuzz.trapmf(salinidad.universe, [30, 33, 37, 40])
salinidad['Alta'] = fuzz.trapmf(salinidad.universe, [37, 45, 50, 50])

# salinidad.view()

#   Temperatura     (-20, 50, 0.1).round(1)
temperatura['Muy Baja'] = fuzz.trapmf(temperatura.universe, [-20, -20, -10, 0])
temperatura['Baja'] = fuzz.trimf(temperatura.universe, [-5, 7, 15])
temperatura['Media'] = fuzz.trapmf(temperatura.universe, [12, 15, 23, 27])
temperatura['Alta'] = fuzz.trimf(temperatura.universe, [25, 27, 35])
temperatura['Muy Alta'] = fuzz.trapmf(temperatura.universe, [30, 40, 50, 50])

# temperatura.view()

#   corrientes     (0, 300)
corrientes['Muy Baja'] = fuzz.trapmf(corrientes.universe, [0, 0, 50, 100])
corrientes['Baja'] = fuzz.trimf(corrientes.universe, [70, 130, 180])
corrientes['Media'] = fuzz.trimf(corrientes.universe, [170, 200, 220])
corrientes['Alta'] = fuzz.trapmf(corrientes.universe, [210, 255, 300, 300])

# corrientes.view()

#   Altura Laminal     (0, 100)
altura_laminal['Muy Baja'] = fuzz.trapmf(altura_laminal.universe, [0, 0, 10, 25])
altura_laminal['Baja'] = fuzz.trimf(altura_laminal.universe, [20, 30, 45])
altura_laminal['Media'] = fuzz.trimf(altura_laminal.universe, [40, 50, 70])
altura_laminal['Alta'] = fuzz.trapmf(altura_laminal.universe, [60, 80, 100, 100])

# altura_laminal.view()

#   viscosidad     (0, 2, 0.01)
viscosidad['Muy Baja'] = fuzz.trapmf(viscosidad.universe, [0.3, 0.3, 0.4, 0.70])
viscosidad['Baja'] = fuzz.trimf(viscosidad.universe, [0.50, 0.85, 1.10])
viscosidad['Media'] = fuzz.trimf(viscosidad.universe, [1.00, 1.55, 1.90])
viscosidad['Alta'] = fuzz.trapmf(viscosidad.universe, [1.75, 1.95, 2, 2])

# viscosidad.view()

#   densidad     (900, 1100)
densidad['Muy Baja'] = fuzz.trapmf(densidad.universe, [900, 900, 925, 950])
densidad['Baja'] = fuzz.trimf(densidad.universe, [925, 950, 975])
densidad['Media'] = fuzz.trimf(densidad.universe, [950, 1000, 1050])
densidad['Alta'] = fuzz.trapmf(densidad.universe, [1025, 1050, 1100, 1100])

# densidad.view()

#   profundidad     (0, 7000)
profundidad['Muy Baja'] = fuzz.trapmf(profundidad.universe, [0, 0, 500, 1000])
profundidad['Baja'] = fuzz.trimf(profundidad.universe, [500, 1250, 2000])
profundidad['Media'] = fuzz.trimf(profundidad.universe, [1500, 3500, 5500])
profundidad['Alta'] = fuzz.trapmf(profundidad.universe, [4500, 6000, 7000, 7000])

# profundidad.view()

#   profundidad colocacion     (0, 150)
profundidad_colocacion['Muy Baja'] = fuzz.trapmf(profundidad_colocacion.universe, [0, 0, 5, 15])
profundidad_colocacion['Baja'] = fuzz.trimf(profundidad_colocacion.universe, [15, 20, 35])
profundidad_colocacion['Media'] = fuzz.trimf(profundidad_colocacion.universe, [30, 70, 120])
profundidad_colocacion['Alta'] = fuzz.trapmf(profundidad_colocacion.universe, [100, 125, 125, 150])

# profundidad_colocacion.view()

#                                                                           OUTPUTS

#   turbina 0-100 %
turbinas['Descartada'] = fuzz.trapmf(turbinas.universe, [0, 0, 30, 50])
turbinas['No Recomendable'] = fuzz.trimf(turbinas.universe, [40, 60, 70])
turbinas['Buena'] = fuzz.trimf(turbinas.universe, [65, 80, 85])
turbinas['Muy Buena'] = fuzz.trimf(turbinas.universe, [80, 85, 90])
turbinas['Optima'] = fuzz.trapmf(turbinas.universe, [85, 95, 100, 100])