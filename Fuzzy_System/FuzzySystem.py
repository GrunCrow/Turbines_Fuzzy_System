from skfuzzy import control
from Fuzzy_System.FuzzyRule import r_optimal, r_very_good, r_good, r_not_recommendable, r_discarded
from Fuzzy_System.FuzzyVariable import turbines


def calculate(input_salinity, input_temperature, input_currents, input_laminal_height, input_viscosity,
              input_density, input_depth, input_placement_depth):
    system_control = control.ControlSystem([r_optimal,   # all green
                                            r_very_good,    # all green but 1 yellow
                                            r_good,    # all green but 2 yellow
                                            r_not_recommendable,  # 1 or + 0/1/2 yell / 3 yell + 0/1/2 yell
                                            r_discarded    # min (1 red, 2 oranges, 1 orange + 3 yell, 6 yellow)
                                            ])

    sA = control.ControlSystemSimulation(system_control)

    # Display graph of the rules to check for cycles, it is a Digraph
    system_control.view()
    # gr = system_control.graph

    def dfs(graph, start):
        color = {i: 'white' for i in graph}
        stack = [start]
        visited = []
        cycles = False
        prev = "Sin valor"

        while stack:
            vertex = stack.pop()
            if color[vertex] == 'grey':
                print(prev)
                print(vertex)
                print("============================================================================")
                cycles = True
            color[vertex] = 'grey'
            visited.append(vertex)
            stack.extend((graph[vertex]))
            if len(graph[vertex]) == 0:
                color[vertex] = 'black'
            prev = vertex
        return cycles

    def cycle_exists(graph):
        for vertex in graph:
            if dfs(graph, vertex):
                return True
        return False

    '''if cycle_exists(gr):
        print("There are cycles in the rules")'''

    sA.input['salinity'] = float(input_salinity)
    sA.input['temperature'] = float(input_temperature)
    sA.input['currents'] = float(input_currents)
    sA.input['laminal_height'] = float(input_laminal_height)
    sA.input['viscosity'] = float(input_viscosity)
    sA.input['density'] = float(input_density)
    sA.input['depth'] = float(input_depth)
    sA.input['placement_depth'] = float(input_placement_depth)

    sA.compute()

    # Result in % = res
    res = sA.output
    # result = next(iter(res))
    result = next(iter(res.items()))
    result = next(iter(res.values()))

    # Visualize graph with where the inputs entered are found in turbines
    image_name = 'turbines_results.png'
    turbines.view(image_name, sim=sA)

    return result
