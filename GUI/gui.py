import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image

from Fuzzy_System import FuzzySystem
from Color_Maps import image_detector
from Color_Maps import color_map

'''
Color Palette:
Lighter fonts: #585866
Medium: #8F8FA6
Medium light: #B0AFCC
Darker highlight: #3B3966
'''

color_main_bg = "#8683EA"
color_bg = "#C6C5E6"
color_bg_subframe = "#D1D0F2"
color_bg_error = "#EBA09B"

color_font = "#292930"

color_textbox = "#DCDBFF"

'''res = None
label_result = None'''


str_salinity = "Salinity"
str_temperature = "Temperature"
str_currents = "Currents"
str_laminar_height = "Laminar Height"
str_viscosity = "Viscosity"
str_density = "Density"
str_depth = "Depth"
str_placement_depth = "Placement Depth"
str_error_win = "Error in parameter value"
str_clear = "Clear"
str_calculate = "Calculate"
str_title = "Turbines Fuzzy System Calculator"
str_error1 = "Parameter value "
str_error2 = " must be between "
str_error3 = " and "
str_map = "Map"


def spanish():
    str_salinity = "Salinidad"
    str_temperature = "Temperatura"
    str_currents = "Corrientes"
    str_laminar_height = "Altura Laminal"
    str_viscosity = "Viscosidad"
    str_density = "Densidad"
    str_depth = "Profundidad"
    str_placement_depth = "Profundidad de Colocación"
    str_clear = "Limpiar"
    str_calculate = "Calcular"
    str_error_win = "Error en el valor del parametro"
    str_title = "Calculadora de Turbinas con Lógica Difusa"
    str_error1 = "Valor del parametro "
    str_error2 = " debe estar entre "
    str_error3 = " y "
    str_map = "Mapa"


def load():
    input_salinity = 20
    input_temperature = -20
    input_currents = 0
    input_laminar_height = 1
    input_viscosity = 0.3
    input_density = 900
    input_depth = 0
    input_placement_depth = 0

    return input_salinity, input_temperature, input_currents, input_laminar_height, input_viscosity, input_density, input_depth, input_placement_depth


def get_inputs():
    input_salinity = textbox_input_salinity.get()
    input_temperature = textbox_input_temperature.get()
    input_currents = textbox_input_currents.get()
    input_laminar_height = textbox_input_laminar_height.get()
    input_viscosity = textbox_input_viscosity.get()
    input_density = textbox_input_density.get()
    input_depth = textbox_input_depth.get()
    input_placement_depth = textbox_input_placement_depth.get()

    return input_salinity, input_temperature, input_currents, input_laminar_height, input_viscosity, input_density, input_depth, input_placement_depth


def calculate():
    clear_results()

    input_salinity, input_temperature, input_currents, input_laminar_height, input_viscosity, input_density, input_depth, input_placement_depth = get_inputs()

    if not (
            input_salinity or input_temperature or input_currents or input_laminar_height or input_viscosity or input_density or input_depth or input_placement_depth):
        input_salinity, input_temperature, input_currents, input_laminar_height, input_viscosity, input_density, input_depth, input_placement_depth = load()

    if constraints(input_salinity, input_temperature, input_currents, input_laminar_height, input_viscosity,
                   input_density, input_depth, input_placement_depth):
        # FuzzySystem.calculate()
        result = FuzzySystem.calculate(input_salinity, input_temperature, input_currents, input_laminar_height,
                                       input_viscosity, input_density, input_depth, input_placement_depth)

        img = Image.open("turbines_results.png")
        new_img = img.resize((320, 240))
        new_img.save("resized_turbines_results.png")
        image = ImageTk.PhotoImage(Image.open("resized_turbines_results.png"))

        res = tk.Label(frame_results, image=image, padx=20)
        res.pack()

        result = round(result, 3)
        result = str(result) + '%'
        result_cfg = font.Font(family='Nunito', size=12, weight="bold")
        label_result = tk.Label(frame_results, anchor="center", pady=10, text=result, fg=color_font,
                                bg=color_bg_subframe)
        label_result['font'] = result_cfg
        label_result.pack()


def open_popup(parameter, minimum_value, maximum_value):
    top = tk.Toplevel(root)
    top.config(bg=color_bg_error)
    top.geometry("600x100")
    top.resizable(False, False)
    top.title(str_error_win)
    # root.eval(f'tk::PlaceWindow {str(top)} center')
    error = str_error1 + str(parameter) + str_error2 + str(minimum_value) + str_error3 + str(maximum_value)
    tk.Label(top, text=error, bg=color_bg_error, font='Nunito 14').place(x=40, y=35)


def constraints(input_salinity, input_temperature, input_currents, input_laminar_height, input_viscosity,
                input_density, input_depth, input_placement_depth):
    if not (20 <= float(input_salinity) <= 50):
        open_popup(str_salinity, 20, 50)
    elif not (-20 <= float(input_temperature) <= 50):
        open_popup(str_temperature, -20, 50)
    elif not (0 <= float(input_currents) <= 300):
        open_popup(str_currents, 0, 300)
    # todo change Laminar Height values
    elif not (0 <= float(input_laminar_height) <= 100):
        open_popup(str_laminar_height, 0, 100)
    elif not (0.3 <= float(input_viscosity) <= 2):
        open_popup(str_viscosity, 0.3, 2)
    elif not (900 <= float(input_density) <= 1100):
        open_popup(str_density, 90, 1100)
    elif not (0 <= float(input_depth) <= 7000):
        open_popup(str_depth, 0, 7000)
    elif not (0 <= float(input_placement_depth) <= 150):
        open_popup(str_placement_depth, 0, 150)
    else:
        return True

    return False


def clear_textbox():
    textbox_input_salinity.delete(0, 'end')
    textbox_input_temperature.delete(0, 'end')
    textbox_input_currents.delete(0, 'end')
    textbox_input_laminar_height.delete(0, 'end')
    textbox_input_viscosity.delete(0, 'end')
    textbox_input_density.delete(0, 'end')
    textbox_input_depth.delete(0, 'end')
    textbox_input_placement_depth.delete(0, 'end')


def clear_results():
    not_empty = frame_results.winfo_children()
    if not_empty:
        for widgets in frame_results.winfo_children():
            widgets.destroy()


def clear_all():
    clear_textbox()
    clear_results()


def map_action():
    # red, green, blue = image_detector.map()
    depth_value = color_map.color_map()
    textbox_input_depth.delete(0, 'end')
    textbox_input_depth.insert("end", str(depth_value))


#                                              MAIN WINDOW
root = tk.Tk()
root.resizable(False, False)
root.title(str_title)
root.geometry("900x500")
root.configure(bg=color_main_bg)

'''canvas = tk.Canvas(root, height=500, width=900, bg=color_main_bg)
canvas.pack()'''

#                                              FRAMES AND SUBFRAMES
frame = tk.Frame(root, bg=color_bg)
frame.place(relwidth=0.97, relheight=0.95, relx=0.015, rely=0.025)

frame.grid_rowconfigure(9, weight=1)
frame.grid_columnconfigure(3, weight=1)

frame_salinity = tk.Frame(frame, bg=color_bg_subframe, width="452", height="41")
frame_salinity.place(x="15", y="70")

frame_temperature = tk.Frame(frame, bg=color_bg_subframe, width="452", height="41")
frame_temperature.place(x="15", y="119")

frame_currents = tk.Frame(frame, bg=color_bg_subframe, width="452", height="41")
frame_currents.place(x="15", y="168")

frame_laminar_height = tk.Frame(frame, bg=color_bg_subframe, width="452", height="41")
frame_laminar_height.place(x="15", y="217")

frame_viscosity = tk.Frame(frame, bg=color_bg_subframe, width="452", height="41")
frame_viscosity.place(x="15", y="266")

frame_density = tk.Frame(frame, bg=color_bg_subframe, width="452", height="41")
frame_density.place(x="15", y="315")

frame_depth = tk.Frame(frame, bg=color_bg_subframe, width="452", height="41")
frame_depth.place(x="15", y="364")

frame_placement_depth = tk.Frame(frame, bg=color_bg_subframe, width="452", height="41")
frame_placement_depth.place(x="15", y="413")

frame_results2 = tk.Frame(frame, bg=color_bg_subframe, width="350", height="300")   # width="350", height="300"
frame_results2.place(x="500", y="70")

frame_results = tk.Frame(frame, bg=color_bg_subframe, width="350", height="290")
frame_results.place(x="500", y="85")

frame_results.pack_propagate(False)

#                                          TITLE AND PARAMETERS

Title_cfg = font.Font(family='Nunito', size=25, weight="bold")
title = tk.Label(frame, text="Turbine Calculator", fg=color_font, bg=color_bg)
title['font'] = Title_cfg
title.config(anchor="center")

title.grid(row=0, column=1, pady=10)

parameters_cfg = font.Font(family='Nunito', size=15)
unit_cfg = font.Font(family='Nunito', size=10)

salinity = tk.Label(frame, text=str_salinity, fg=color_font, bg=color_bg_subframe)
salinity['font'] = parameters_cfg
# salinity.pack()
salinity.grid(row=1, column=0, sticky="W", padx=20, pady=10)

textbox_input_salinity = tk.Entry(frame, width=15, bg=color_textbox, fg=color_font, justify='right')
textbox_input_salinity.grid(row=1, column=1, sticky="e", padx=75)
textbox_input_salinity.insert("end", "20")

salinity_unit = tk.Label(frame, text="g/L", fg=color_font, bg=color_bg_subframe)
salinity_unit['font'] = unit_cfg
salinity_unit.grid(row=1, column=1, sticky="e", padx=30)

temperature = tk.Label(frame, text=str_temperature, fg=color_font, bg=color_bg_subframe)
temperature['font'] = parameters_cfg
# temperature.pack(anchor="nw", padx=20, pady=10)
temperature.grid(row=2, column=0, sticky="W", padx=20, pady=10)

textbox_input_temperature = tk.Entry(frame, width=15, bg=color_textbox, fg=color_font, justify='right')
textbox_input_temperature.grid(row=2, column=1, sticky="e", padx=75)
textbox_input_temperature.insert("end", "-20")

temperature_unit = tk.Label(frame, text="ºC", fg=color_font, bg=color_bg_subframe)
temperature_unit['font'] = unit_cfg
temperature_unit.grid(row=2, column=1, sticky="e", padx=30)

currents = tk.Label(frame, text=str_currents, fg=color_font, bg=color_bg_subframe)
currents['font'] = parameters_cfg
# currents.pack(anchor="nw", padx=20, pady=10)
currents.grid(row=3, column=0, sticky="W", padx=20, pady=10)

textbox_input_currents = tk.Entry(frame, width=15, bg=color_textbox, fg=color_font, justify='right')
textbox_input_currents.grid(row=3, column=1, sticky="e", padx=75)
textbox_input_currents.insert("end", "0")

currents_unit = tk.Label(frame, text="cm/s", fg=color_font, bg=color_bg_subframe)
currents_unit['font'] = unit_cfg
currents_unit.grid(row=3, column=1, sticky="e", padx=30)

laminar_height = tk.Label(frame, text=str_laminar_height, fg=color_font, bg=color_bg_subframe)
laminar_height['font'] = parameters_cfg
laminar_height.grid(row=4, column=0, sticky="W", padx=20, pady=10)

textbox_input_laminar_height = tk.Entry(frame, width=15, bg=color_textbox, fg=color_font, justify='right')
textbox_input_laminar_height.grid(row=4, column=1, sticky="e", padx=75)
textbox_input_laminar_height.insert("end", "0")

laminar_height_unit = tk.Label(frame, text="0", fg=color_font, bg=color_bg_subframe)    # todo unit laminar height
laminar_height_unit['font'] = unit_cfg
laminar_height_unit.grid(row=4, column=1, sticky="e", padx=30)

viscosity = tk.Label(frame, text=str_viscosity, fg=color_font, bg=color_bg_subframe)
viscosity['font'] = parameters_cfg
viscosity.grid(row=5, column=0, sticky="W", padx=20, pady=10)

textbox_input_viscosity = tk.Entry(frame, width=15, bg=color_textbox, fg=color_font, justify='right')
textbox_input_viscosity.grid(row=5, column=1, sticky="e", padx=75)
textbox_input_viscosity.insert("end", "0.3")

viscosity_unit = tk.Label(frame, text="cp", fg=color_font, bg=color_bg_subframe)
viscosity_unit['font'] = unit_cfg
viscosity_unit.grid(row=5, column=1, sticky="e", padx=30)

density = tk.Label(frame, text=str_density, fg=color_font, bg=color_bg_subframe)
density['font'] = parameters_cfg
density.grid(row=6, column=0, sticky="W", padx=20, pady=10)

textbox_input_density = tk.Entry(frame, width=15, bg=color_textbox, fg=color_font, justify='right')
textbox_input_density.grid(row=6, column=1, sticky="e", padx=75)
textbox_input_density.insert("end", "900")

density_unit = tk.Label(frame, text="Kg/m3", fg=color_font, bg=color_bg_subframe)
density_unit['font'] = unit_cfg
density_unit.grid(row=6, column=1, sticky="e", padx=30)

depth = tk.Label(frame, text=str_depth, fg=color_font, bg=color_bg_subframe)
depth['font'] = parameters_cfg
depth.grid(row=7, column=0, sticky="W", padx=20, pady=10)

textbox_input_depth = tk.Entry(frame, width=15, bg=color_textbox, fg=color_font, justify='right')
textbox_input_depth.grid(row=7, column=1, sticky="e", padx=75)
textbox_input_depth.insert("end", "0")

depth_unit = tk.Label(frame, text="m", fg=color_font, bg=color_bg_subframe)
depth_unit['font'] = unit_cfg
depth_unit.grid(row=7, column=1, sticky="e", padx=30)

placement_depth = tk.Label(frame, text=str_placement_depth, fg=color_font, bg=color_bg_subframe)
placement_depth['font'] = parameters_cfg
placement_depth.grid(row=8, column=0, sticky="W", padx=20, pady=10)

textbox_input_placement_depth = tk.Entry(frame, width=15, bg=color_textbox, justify='right')
textbox_input_placement_depth.grid(row=8, column=1, sticky="e", padx=75)
textbox_input_placement_depth.insert("end", "0")

placement_depth_unit = tk.Label(frame, text="m", fg=color_font, bg=color_bg_subframe)
placement_depth_unit['font'] = unit_cfg
placement_depth_unit.grid(row=8, column=1, sticky="e", padx=30)

#                                                  BUTTONS

button_cfg = font.Font(family='Nunito', size=12)

button_clear = tk.Button(frame, text=str_clear, fg=color_font, bg=color_main_bg, height=1, width=10, command=clear_all)  # , command=FuzzySystem.calculate()
button_clear['font'] = button_cfg
button_clear.grid(row=8, column=3, sticky="sw", pady=10)

button_map = tk.Button(frame, text=str_map, fg=color_font, bg=color_main_bg, height=1, width=10, command=map_action)  # , command=FuzzySystem.calculate()
button_map['font'] = button_cfg
button_map.grid(row=8, column=3, padx=15, pady=10)

button_calculate = tk.Button(frame, text=str_calculate, fg=color_font, bg=color_main_bg, height=1, width=10, command=calculate)  # , command=FuzzySystem.calculate()
button_calculate['font'] = button_cfg
button_calculate.grid(row=8, column=3, sticky="se", padx=15, pady=10)

'''button_language = tk.Button(frame, text="C", fg=color_font, bg=color_main_bg, height=1, width=1, command=spanish())
button_language['font'] = button_cfg
button_language.grid(row=0, column=3, sticky="se", padx=15, pady=10)'''


def gui():
    root.mainloop()