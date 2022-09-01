import numpy as np
from skfuzzy import control

'''
Definition of the variables which includes:
    - Domain of each variable (val min and max possible and step between values)
    - Declaration of the inputs (Background) and outputs (Consequent) for the skfuzzy library
'''

domain_salinity = np.arange(20, 50)  # gram per litre
domain_temperature = np.arange(-20, 50, 0.1).round(1)  # grades celsius
domain_currents = np.arange(0, 300)  # cm per second
domain_laminar_height = np.arange(0, 100)  # TODO Domain of laminar Height
domain_viscosity = np.arange(0.3, 2, 0.01)  # centi-poise (mPa)
domain_density = np.arange(900, 1100)  # Kg/m3
domain_depth = np.arange(0, 7000)  # m
domain_placement_depth = np.arange(0, 150)  # m

# domain_turbines = np.array(['Optimal', 'Very Good', 'Good', 'Not recommendable', 'Discarded'])
domain_turbines = np.arange(0, 100)  # %

salinity = control.Antecedent(domain_salinity, 'salinity')
temperature = control.Antecedent(domain_temperature, 'temperature')
currents = control.Antecedent(domain_currents, 'currents')
laminar_height = control.Antecedent(domain_laminar_height, 'laminar_height')
viscosity = control.Antecedent(domain_viscosity, 'viscosity')
density = control.Antecedent(domain_density, 'density')
depth = control.Antecedent(domain_depth, 'depth')
placement_depth = control.Antecedent(domain_placement_depth, 'placement_depth')

turbines = control.Consequent(domain_turbines, 'turbines')
