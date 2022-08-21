from skfuzzy import control
from FuzzySystem import system_control
from FuzzyVariable import turbinas

sA = control.ControlSystemSimulation(system_control)

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

input_salinidad = 35
input_temperatura = 20
input_corrientes = 255
input_altura_laminal = 80
input_viscodidad = 1.55
input_densidad = 1000
input_profundidad = 3500
input_profundidad_colocacion = 70

# Visualizar gráfico de las reglas para comprobar si hay ciclos, es un Digraph
# system_control.view()

sA.input['salinidad'] = float(input_salinidad)
sA.input['temperatura'] = float(input_temperatura)
sA.input['corrientes'] = float(input_corrientes)
sA.input['altura_laminal'] = float(input_altura_laminal)
sA.input['viscodidad'] = float(input_viscodidad)
sA.input['densidad'] = float(input_densidad)
sA.input['profundidad'] = float(input_profundidad)
sA.input['profundidad_colocacion'] = float(input_profundidad_colocacion)

sA.compute()

# Resultado en % = res
res = sA.output
print(res)

# Visualizar gráfica con donde se encuentran en turbinas los inputs introducidos
turbinas.view(sim=sA)
