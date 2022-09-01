import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image

from Fuzzy_System import FuzzySystem

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

    if not(input_salinity or input_temperature or input_currents or input_laminar_height or input_viscosity or input_density or input_depth or input_placement_depth):
        input_salinity, input_temperature, input_currents, input_laminar_height, input_viscosity, input_density, input_depth, input_placement_depth = load()

    if constraints(input_salinity, input_temperature, input_currents, input_laminar_height, input_viscosity, input_density, input_depth, input_placement_depth):
        # FuzzySystem.calculate()
        result = FuzzySystem.calculate(input_salinity, input_temperature, input_currents, input_laminar_height, input_viscosity, input_density, input_depth, input_placement_depth)

        img = Image.open("turbines_results.png")
        new_img = img.resize((320, 240))
        new_img.save("resized_turbines_results.png")
        image = ImageTk.PhotoImage(Image.open("resized_turbines_results.png"))

        res = tk.Label(frame_results, image=image, padx=20)
        res.pack()

        result = round(result, 3)
        result = str(result) + '%'
        result_cfg = font.Font(family='Nunito', size=12, weight="bold")
        label_result = tk.Label(frame_results, anchor="center", pady=10, text=result, fg=color_font, bg=color_bg_subframe)
        label_result['font'] = result_cfg
        label_result.pack()


def open_popup(parameter, minimum_value, maximum_value):
    top = tk.Toplevel(root)
    top.config(bg=color_bg_error)
    top.geometry("600x100")
    top.resizable(False, False)
    top.title("Error in parameter value")
    # root.eval(f'tk::PlaceWindow {str(top)} center')
    error = "Parameter value " + str(parameter) + " must be between " + str(minimum_value) + " and " + str(maximum_value)
    tk.Label(top, text=error, bg=color_bg_error, font='Nunito 14').place(x=40, y=35)


def constraints(input_salinity, input_temperature, input_currents, input_laminar_height, input_viscosity, input_density, input_depth, input_placement_depth):
    if not (20 <= float(input_salinity) <= 50):
        open_popup("Salinity", 20, 50)
    elif not (-20 <= float(input_temperature) <= 50):
        open_popup("Temperature", -20, 50)
    elif not (0 <= float(input_currents) <= 300):
        open_popup("Currents", 0, 300)
    # todo change Laminar Height values
    elif not (0 <= float(input_laminar_height) <= 100):
        open_popup("Laminar Height", 0, 100)
    elif not (0.3 <= float(input_viscosity) <= 2):
        open_popup("Viscosity", 0.3, 2)
    elif not (900 <= float(input_density) <= 1100):
        open_popup("Density", 90, 1100)
    elif not (0 <= float(input_depth) <= 7000):
        open_popup("Depth", 0, 7000)
    elif not (0 <= float(input_placement_depth) <= 150):
        open_popup("Placement Depth", 0, 150)
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


#                                              MAIN WINDOW
root = tk.Tk()
root.resizable(False, False)
root.title("Turbines Fuzzy System Calculator")
root.geometry("900x500")
root.configure(bg=color_main_bg)


'''canvas = tk.Canvas(root, height=500, width=900, bg=color_main_bg)
canvas.pack()'''

#                                              FRAMES AND SUBFRAMES
frame = tk.Frame(root, bg=color_bg)
frame.place(relwidth=0.97, relheight=0.95, relx=0.015, rely=0.025)

frame.grid_rowconfigure(9, weight=1)
frame.grid_columnconfigure(3, weight=1)

frame_salinity = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_salinity.place(x="15", y="70")

frame_temperature = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_temperature.place(x="15", y="119")

frame_currents = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_currents.place(x="15", y="168")

frame_laminar_height = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_laminar_height.place(x="15", y="217")

frame_viscosity = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_viscosity.place(x="15", y="266")

frame_density = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_density.place(x="15", y="315")

frame_depth = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_depth.place(x="15", y="364")

frame_placement_depth = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
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

salinity = tk.Label(frame, text="Salinity", fg=color_font, bg=color_bg_subframe)
salinity['font'] = parameters_cfg
# salinidad.pack()
salinity.grid(row=1, column=0, sticky="W", padx=20, pady=10)

textbox_input_salinity = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font, justify='right')
textbox_input_salinity.grid(row=1, column=1, sticky="w", padx=30)
textbox_input_salinity.insert("end", "20")

temperature = tk.Label(frame, text="Temperature", fg=color_font, bg=color_bg_subframe)
temperature['font'] = parameters_cfg
# temperature.pack(anchor="nw", padx=20, pady=10)
temperature.grid(row=2, column=0, sticky="W", padx=20, pady=10)

textbox_input_temperature = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font, justify='right')
textbox_input_temperature.grid(row=2, column=1, sticky="w", padx=30)
textbox_input_temperature.insert("end", "-20")

currents = tk.Label(frame, text="Currents", fg=color_font, bg=color_bg_subframe)
currents['font'] = parameters_cfg
# currents.pack(anchor="nw", padx=20, pady=10)
currents.grid(row=3, column=0, sticky="W", padx=20, pady=10)

textbox_input_currents = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font, justify='right')
textbox_input_currents.grid(row=3, column=1, sticky="w", padx=30)
textbox_input_currents.insert("end", "0")


laminar_height = tk.Label(frame, text="Laminar Height", fg=color_font, bg=color_bg_subframe)
laminar_height['font'] = parameters_cfg
laminar_height.grid(row=4, column=0, sticky="W", padx=20, pady=10)

textbox_input_laminar_height = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font, justify='right')
textbox_input_laminar_height.grid(row=4, column=1, sticky="w", padx=30)
textbox_input_laminar_height.insert("end", "0")


viscosity = tk.Label(frame, text="Viscosity", fg=color_font, bg=color_bg_subframe)
viscosity['font'] = parameters_cfg
viscosity.grid(row=5, column=0, sticky="W", padx=20, pady=10)

textbox_input_viscosity = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font, justify='right')
textbox_input_viscosity.grid(row=5, column=1, sticky="w", padx=30)
textbox_input_viscosity.insert("end", "0.3")

density = tk.Label(frame, text="Density", fg=color_font, bg=color_bg_subframe)
density['font'] = parameters_cfg
density.grid(row=6, column=0, sticky="W", padx=20, pady=10)

textbox_input_density = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font, justify='right')
textbox_input_density.grid(row=6, column=1, sticky="w", padx=30)
textbox_input_density.insert("end", "900")

depth = tk.Label(frame, text="Depth", fg=color_font, bg=color_bg_subframe)
depth['font'] = parameters_cfg
depth.grid(row=7, column=0, sticky="W", padx=20, pady=10)

textbox_input_depth = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font, justify='right')
textbox_input_depth.grid(row=7, column=1, sticky="w", padx=30)
textbox_input_depth.insert("end", "0")

placement_depth = tk.Label(frame, text="Placement Depth", fg=color_font, bg=color_bg_subframe)
placement_depth['font'] = parameters_cfg
placement_depth.grid(row=8, column=0, sticky="W", padx=20, pady=10)

textbox_input_placement_depth = tk.Entry(frame, width=20, bg=color_textbox, justify='right')
textbox_input_placement_depth.grid(row=8, column=1, sticky="w", padx=30)
textbox_input_placement_depth.insert("end", "0")

#                                                  BUTTONS

button_cfg = font.Font(family='Nunito', size=12)

clear = tk.Button(frame, text="Clear", fg=color_font, bg=color_main_bg, height=1, width=10, command=clear_all)  # , command=FuzzySystem.calculate()
clear['font'] = button_cfg
clear.grid(row=8, column=3, sticky="sw", pady=10)

calculate = tk.Button(frame, text="Calculate", fg=color_font, bg=color_main_bg, height=1, width=10, command=calculate)  # , command=FuzzySystem.calculate()
calculate['font'] = button_cfg
calculate.grid(row=8, column=3, sticky="se", padx=15, pady=10)


def gui_no_maps():
    root.mainloop()
