from skfuzzy import control
from matplotlib import pyplot as plt    # para guardar la imagen de las graficas
from Fuzzy_System.FuzzyRule import r_optima, r_muy_buena, r_buena, r_no_recomendable_amarillos, r_no_recomendable_naranja,\
    r_descartada_rojo, r_descartada_naranjas, r_descartada_naranja_amarillos, r_descartada_amarillos
from Fuzzy_System.FuzzyVariable import turbinas

'''# Valores de input

input_salinidad = 38
input_temperatura = 30
input_corrientes = 255
input_altura_laminal = 80
input_viscodidad = 1.55
input_densidad = 1000
input_profundidad = 3500
input_profundidad_colocacion = 70

system_control = control.ControlSystem([r_optima,   # tod verde
                                        r_muy_buena,    # tod verde y un amarillo
                                        r_buena,    # tod verde y 2 amarillo
                                        r_no_recomendable_naranja, r_no_recomendable_amarillos,  # 1 naranja + 0/1/2 amarillos // 3 amarillos + 0/1/2 amarillos
                                        r_descartada_rojo, r_descartada_naranjas, r_descartada_naranja_amarillos, r_descartada_amarillos])  # min (1 rojo, 2 naranjas, 1 naranja + 3 amar, 6 amarillos)

sA = control.ControlSystemSimulation(system_control)

# Visualizar gráfico de las reglas para comprobar si hay ciclos, es un Digraph
# system_control.view()

sA.input['salinidad'] = float(input_salinidad)
sA.input['temperatura'] = float(input_temperatura)
sA.input['corrientes'] = float(input_corrientes)
sA.input['altura_laminal'] = float(input_altura_laminal)
sA.input['viscosidad'] = float(input_viscosidad)
sA.input['densidad'] = float(input_densidad)
sA.input['profundidad'] = float(input_profundidad)
sA.input['profundidad_colocacion'] = float(input_profundidad_colocacion)

sA.compute()

# Resultado en % = res
res = sA.output
print(res)

# Visualizar gráfica con donde se encuentran en turbinas los inputs introducidos
turbinas.view(sim=sA)'''


def calcular(input_salinidad, input_temperatura, input_corrientes, input_altura_laminal, input_viscosidad, input_densidad, input_profundidad, input_profundidad_colocacion):
    system_control = control.ControlSystem([r_optima,   # tod verde
                                            r_muy_buena,    # tod verde y un amarillo
                                            r_buena,    # tod verde y 2 amarillo
                                            r_no_recomendable_naranja, r_no_recomendable_amarillos,  # 1 naranja + 0/1/2 amarillos // 3 amarillos + 0/1/2 amarillos
                                            r_descartada_rojo, r_descartada_naranjas, r_descartada_naranja_amarillos, r_descartada_amarillos])  # min (1 rojo, 2 naranjas, 1 naranja + 3 amar, 6 amarillos)

    sA = control.ControlSystemSimulation(system_control)

    # Visualizar gráfico de las reglas para comprobar si hay ciclos, es un Digraph
    # system_control.view()

    sA.input['salinidad'] = float(input_salinidad)
    sA.input['temperatura'] = float(input_temperatura)
    sA.input['corrientes'] = float(input_corrientes)
    sA.input['altura_laminal'] = float(input_altura_laminal)
    sA.input['viscosidad'] = float(input_viscosidad)
    sA.input['densidad'] = float(input_densidad)
    sA.input['profundidad'] = float(input_profundidad)
    sA.input['profundidad_colocacion'] = float(input_profundidad_colocacion)

    sA.compute()

    # Resultado en % = res
    res = sA.output
    # resultado = next(iter(res))
    resultado = next(iter(res.items()))
    resultado = next(iter(res.values()))

    # Visualizar gráfica con donde se encuentran en turbinas los inputs introducidos
    image_name = 'turbinas_results.png'
    turbinas.view(image_name, sim=sA)

    return resultado
