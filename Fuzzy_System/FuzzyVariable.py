import numpy as np
from skfuzzy import control

'''Definición de las variables lo cual incluye:
    - Dominio de cada variable (val min y max posibles y paso entre valores)
    - Declaración de los inputs (Antecedentes) y outputs (Consecuente) para la libreria skfuzzy
'''

domain_salinity = np.arange(20, 50)  # en gramos por litros
domain_temperature = np.arange(-20, 50, 0.1).round(1)  # en grados celsius
domain_currents = np.arange(0, 300)  # en cm por segundo
domain_laminal_height = np.arange(0, 100)  # TODO Dominio de la altura laminal
domain_viscosity = np.arange(0.3, 2, 0.01)  # en centipoise (mPa)
domain_density = np.arange(900, 1100)  # Kg/m3
domain_depth = np.arange(0, 7000)  # m
domain_placement_depth = np.arange(0, 150)  # m

# domain_turbines = np.array(['Optima', 'Muy Buena', 'Buena', 'No recomendable', 'Descartada'])
domain_turbines = np.arange(0, 100)  # %

salinity = control.Antecedent(domain_salinity, 'salinity')
temperature = control.Antecedent(domain_temperature, 'temperature')
currents = control.Antecedent(domain_currents, 'currents')
laminal_height = control.Antecedent(domain_laminal_height, 'laminal_height')
viscosity = control.Antecedent(domain_viscosity, 'viscosity')
density = control.Antecedent(domain_density, 'density')
depth = control.Antecedent(domain_depth, 'depth')
placement_depth = control.Antecedent(domain_placement_depth, 'placement_depth')

turbines = control.Consequent(domain_turbines, 'turbines')
