from skfuzzy import control
from Fuzzy_System.FuzzyRule import r_optima, r_muy_buena, r_buena, r_no_recomendable, r_descartada
from Fuzzy_System.FuzzyVariable import turbinas


def calcular(input_salinidad, input_temperatura, input_corrientes, input_altura_laminal, input_viscosidad,
             input_densidad, input_profundidad, input_profundidad_colocacion):
    system_control = control.ControlSystem([r_optima,   # tod verde
                                            r_muy_buena,    # tod verde y un amarillo
                                            r_buena,    # tod verde y 2 amarillo
                                            r_no_recomendable,  # 1 nar + 0/1/2 amar / 3 amar + 0/1/2 amar
                                            r_descartada    # min (1 rojo, 2 naranjas, 1 naranja + 3 amar, 6 amarillos)
                                            ])

    sA = control.ControlSystemSimulation(system_control)

    # Visualizar gráfico de las reglas para comprobar si hay ciclos, es un Digraph
    system_control.view()
    # gr = system_control.graph

    def dfs(graph, start):
        color = {i: 'white' for i in graph}
        stack = [start]
        visited = []
        ciclos = False
        prev = "Sin valor"

        while stack:
            vertex = stack.pop()
            if color[vertex] == 'grey':
                print(prev)
                print(vertex)
                print("============================================================================")
                ciclos = True
            color[vertex] = 'grey'
            visited.append(vertex)
            stack.extend((graph[vertex]))
            if len(graph[vertex]) == 0:
                color[vertex] = 'black'
            prev = vertex
        return ciclos

    def cycle_exists(graph):
        for vertex in graph:
            if dfs(graph, vertex):
                return True
        return False

    '''if cycle_exists(gr):
        print("Hay ciclos en las reglas")'''

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
