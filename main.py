from skfuzzy import control
from FuzzySystem import system_control
# from FuzzyVariable import salinidad, temperatura, corrientes, altura_laminal, viscodidad, densidad, profundidad, profundidad_colocacion
from membership_functions import turbinas

'''while True:
    # Ask for the values for the function:
    input_salinidad = input("Valor de salinidad: ")
    input_temperatura = input("Valor de temperaturas: ")
    input_corrientes = input("Valor de corrientes: ")
    input_altura_laminal = input("Valor de Altura laminal del fluido: ")
    input_viscodidad = input("Valor de viscodidad: ")
    input_densidad = input("Valor de densidad: ")
    input_profundidad = input("Valor de profundidad: ")
    input_profundidad_colocacion = input("Valor de profundidad de colocacion de la turbina: ")'''

sA = control.ControlSystemSimulation(system_control)

sA.input['salinidad'] = 34
sA.input['temperatura'] = 16
sA.input['corrientes'] = 50
sA.input['altura_laminal'] = 5
sA.input['viscodidad'] = 1.7
sA.input['densidad'] = 1050
sA.input['profundidad'] = 3000
sA.input['profundidad_colocacion'] = 40

'''sA.input['salinidad'] = float(input_salinidad)
sA.input['temperatura'] = float(input_temperatura)
sA.input['corrientes'] = float(input_corrientes)
sA.input['altura_laminal'] = float(input_altura_laminal)
sA.input['viscodidad'] = float(input_viscodidad)
sA.input['densidad'] = float(input_densidad)
sA.input['profundidad'] = float(input_profundidad)
sA.input['profundidad_colocacion'] = float(input_profundidad_colocacion)'''

sA.compute()

sA.output

turbinas.view(sim=sA)
