import numpy as np
from skfuzzy import control

'''Definición de las variables lo cual incluye:
    - Dominio de cada variable (val min y max posibles y paso entre valores)
    - Declaración de los inputs (Antecedentes) y outputs (Consecuente) para la libreria skfuzzy
'''

dominio_salinidad = np.arange(20, 50)  # en gramos por litros
dominio_temperatura = np.arange(-20, 50, 0.1).round(1)  # en grados celsius
dominio_corrientes = np.arange(0, 300)  # en cm por segundo
dominio_altura_laminal = np.arange(0, 100)  # TODO Dominio de la altura laminal
dominio_viscosidad = np.arange(0.30, 2.00, 0.01)  # en mPa
dominio_densidad = np.arange(900, 1100)  # Kg/m3
dominio_profundidad = np.arange(0, 7000)  # m
dominio_profundidad_colocacion = np.arange(0, 150)  # m

# dominio_turbinas = np.array(['Optima', 'Muy Buena', 'Buena', 'No recomendable', 'Descartada'])
dominio_turbinas = np.arange(0, 100)  # %

salinidad = control.Antecedent(dominio_salinidad, 'salinidad')
temperatura = control.Antecedent(dominio_temperatura, 'temperatura')
corrientes = control.Antecedent(dominio_corrientes, 'corrientes')
altura_laminal = control.Antecedent(dominio_altura_laminal, 'altura_laminal')
viscodidad = control.Antecedent(dominio_viscosidad, 'viscodidad')
densidad = control.Antecedent(dominio_densidad, 'densidad')
profundidad = control.Antecedent(dominio_profundidad, 'profundidad')
profundidad_colocacion = control.Antecedent(dominio_profundidad_colocacion, 'profundidad_colocacion')

turbinas = control.Consequent(dominio_turbinas, 'turbinas')