from FuzzyVariable import salinidad, temperatura, corrientes, altura_laminal, viscodidad, densidad, profundidad, profundidad_colocacion, turbinas
import skfuzzy as fuzz

# trimf for triangular -> (0,4,8) - pico en el 4 y va de 0 a 8 las laterales
# trapmf for trapezoidal -> (8,12,20,25) - empieza en 8 y la primera arista hacia arriba en 12, la siguiente lateral la une con 20 (seria valor 1) y la siguiente (25) para abajo hacia el 0

#                                                                INPUTS
#   Salinidad       (20, 50)
salinidad['Muy Baja'] = fuzz.trimf(salinidad.universe, [20, 22, 25])
salinidad['Baja'] = fuzz.trimf(salinidad.universe, [22, 26, 33])
salinidad['Media'] = fuzz.trapmf(salinidad.universe, [30, 33, 37, 40])
salinidad['Alta'] = fuzz.trimf(salinidad.universe, [37, 43, 45])
salinidad['Muy Alta'] = fuzz.trimf(salinidad.universe, [43, 45, 50])

#   Temperatura     (-20, 50, 0.1).round(1)
temperatura['Muy Baja'] = fuzz.trimf(temperatura.universe, [-20, -10, 0])
temperatura['Baja'] = fuzz.trimf(temperatura.universe, [-4, 7, 15])
temperatura['Media'] = fuzz.trapmf(temperatura.universe, [12, 15, 23, 27])
temperatura['Alta'] = fuzz.trimf(temperatura.universe, [25, 27, 35])
temperatura['Muy Alta'] = fuzz.trimf(temperatura.universe, [30, 40, 50])

#   corrientes     (0, 300)
corrientes['Muy Baja'] = fuzz.trimf(corrientes.universe, [0, 50, 100])
corrientes['Baja'] = fuzz.trimf(corrientes.universe, [70, 130, 180])
corrientes['Media'] = fuzz.trimf(corrientes.universe, [170, 200, 220])
corrientes['Alta'] = fuzz.trimf(corrientes.universe, [210, 230, 250])
corrientes['Muy Alta'] = fuzz.trimf(corrientes.universe, [240, 270, 300])

#   Altura Laminal     (0, 100)
altura_laminal['Muy Baja'] = fuzz.trimf(altura_laminal.universe, [0, 10, 25])
altura_laminal['Baja'] = fuzz.trimf(altura_laminal.universe, [20, 30, 45])
altura_laminal['Media'] = fuzz.trimf(altura_laminal.universe, [40, 50, 65])
altura_laminal['Alta'] = fuzz.trimf(altura_laminal.universe, [60, 70, 85])
altura_laminal['Muy Alta'] = fuzz.trimf(altura_laminal.universe, [80, 90, 100])

#   viscodidad     (0.300, 2.000, 0.001)
viscodidad['Muy Baja'] = fuzz.trimf(viscodidad.universe, [0.30, 0.40, 0.70])
viscodidad['Baja'] = fuzz.trimf(viscodidad.universe, [0.50, 0.85, 1.10])
viscodidad['Media'] = fuzz.trimf(viscodidad.universe, [1.00, 1.70, 1.80])
viscodidad['Alta'] = fuzz.trimf(viscodidad.universe, [1.70, 1.85, 1.90])
viscodidad['Muy Alta'] = fuzz.trimf(viscodidad.universe, [1.80, 1.95, 2.00])

#   densidad     (900, 1100)
densidad['Muy Baja'] = fuzz.trimf(densidad.universe, [900, 925, 950])
densidad['Baja'] = fuzz.trimf(densidad.universe, [925, 950, 975])
densidad['Media'] = fuzz.trimf(densidad.universe, [950, 975, 1025])
densidad['Alta'] = fuzz.trimf(densidad.universe, [975, 1025, 1050])
densidad['Muy Alta'] = fuzz.trimf(densidad.universe, [1025, 1050, 1100])

#   profundidad     (0, 7000)
profundidad['Muy Baja'] = fuzz.trimf(profundidad.universe, [0, 500, 1000])
profundidad['Baja'] = fuzz.trimf(profundidad.universe, [500, 1250, 2000])
profundidad['Media'] = fuzz.trimf(profundidad.universe, [1500, 2500, 3500])
profundidad['Alta'] = fuzz.trimf(profundidad.universe, [2500, 4000, 5500])
profundidad['Muy Alta'] = fuzz.trimf(profundidad.universe, [4500, 6000, 7000])

#   profundidad colocacion     (0, 150)
profundidad_colocacion['Muy Baja'] = fuzz.trimf(profundidad_colocacion.universe, [0, 5, 15])
profundidad_colocacion['Baja'] = fuzz.trimf(profundidad_colocacion.universe, [15, 20, 35])
profundidad_colocacion['Media'] = fuzz.trimf(profundidad_colocacion.universe, [30, 60, 80])
profundidad_colocacion['Alta'] = fuzz.trimf(profundidad_colocacion.universe, [70, 90, 120])
profundidad_colocacion['Muy Alta'] = fuzz.trimf(profundidad_colocacion.universe, [100, 125, 150])

#                                                                           OUTPUTS
#   turbina 0-100 %
turbinas['Descartada'] = fuzz.trapmf(turbinas.universe, [0, 0, 30, 40])
turbinas['No Recomendable'] = fuzz.trimf(turbinas.universe, [30, 50, 70])
turbinas['Buena'] = fuzz.trimf(turbinas.universe, [65, 80, 85])
turbinas['Muy Buena'] = fuzz.trimf(turbinas.universe, [80, 85, 90])
turbinas['Optima'] = fuzz.trapmf(turbinas.universe, [85, 95, 100, 100])

