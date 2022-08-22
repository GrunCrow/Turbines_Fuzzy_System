import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image


from Fuzzy_System import FuzzySystem

'''
Paleta de colores:
Letras mas claras: #585866
Medio: #8F8FA6
Medio claro: #B0AFCC
Resalte más oscuro: #3B3966
'''

color_main_bg = "#8683EA"
color_bg = "#C6C5E6"
color_bg_subframe = "#D1D0F2"

color_font = "#292930"

color_textbox = "#DCDBFF"

'''res = None
label_resultado = None'''

# todo añadir constraints para añadir valores, 2 opciones:
    # - imponer que el valor sea entre x e y
    # si es menos de x acercar al valor x y si es mas de y acercar a y


def cargar():
    input_salinidad = 35
    input_temperatura = 20
    input_corriente = 255
    input_altura_laminal = 80
    input_viscosidad = 1.55
    input_densidad = 1000
    input_profundidad = 3500
    input_profundidad_colocacion = 70

    return input_salinidad, input_temperatura, input_corriente, input_altura_laminal, input_viscosidad, input_densidad, input_profundidad, input_profundidad_colocacion


def get_inputs():
    input_salinidad = textbox_input_salinidad.get()
    input_temperatura = textbox_input_temperatura.get()
    input_corriente = textbox_input_corriente.get()
    input_altura_laminal = textbox_input_altura_laminal.get()
    input_viscosidad = textbox_input_viscosidad.get()
    input_densidad = textbox_input_densidad.get()
    input_profundidad = textbox_input_profundidad.get()
    input_profundidad_colocacion = textbox_input_profundidad_colocacion.get()

    return input_salinidad, input_temperatura, input_corriente, input_altura_laminal, input_viscosidad, input_densidad, input_profundidad, input_profundidad_colocacion


def calcular():
    clear_resultados()

    input_salinidad, input_temperatura, input_corriente, input_altura_laminal, input_viscosidad, input_densidad, input_profundidad, input_profundidad_colocacion = get_inputs()
    input_salinidad, input_temperatura, input_corriente, input_altura_laminal, input_viscosidad, input_densidad, input_profundidad, input_profundidad_colocacion = cargar()

    if input_salinidad and input_temperatura and input_corriente and input_altura_laminal and input_viscosidad and input_densidad and input_profundidad and input_profundidad_colocacion:
        # FuzzySystem.calcular()
        resultado = FuzzySystem.calcular(input_salinidad, input_temperatura, input_corriente, input_altura_laminal, input_viscosidad, input_densidad, input_profundidad, input_profundidad_colocacion)

        img = Image.open("turbinas_results.png")
        new_img = img.resize((320, 240))
        new_img.save("resized_turbinas_results.png")
        image = ImageTk.PhotoImage(Image.open("resized_turbinas_results.png"))

        res = tk.Label(frame_resultados, image=image, padx=20)
        res.pack()

        resultado = round(resultado, 3)
        result = str(resultado) + '%'
        resultado_cfg = font.Font(family='Nunito', size=12, weight="bold")
        label_resultado = tk.Label(frame_resultados, anchor="center", pady=10, text=result, fg=color_font, bg=color_bg_subframe)
        label_resultado['font'] = resultado_cfg
        label_resultado.pack()


def clear_textbox():
    textbox_input_salinidad.delete(0, 'end')
    textbox_input_temperatura.delete(0, 'end')
    textbox_input_corriente.delete(0, 'end')
    textbox_input_altura_laminal.delete(0, 'end')
    textbox_input_viscosidad.delete(0, 'end')
    textbox_input_densidad.delete(0, 'end')
    textbox_input_profundidad.delete(0, 'end')
    textbox_input_profundidad_colocacion.delete(0, 'end')


def clear_resultados():
    not_empty = frame_resultados.winfo_children()
    if not_empty:
        for widgets in frame_resultados.winfo_children():
            widgets.destroy()


def clear_all():
    clear_textbox()
    clear_resultados()



root = tk.Tk()
root.resizable(False, False)
root.title("Calculadora de Turbina con un Sistema Difuso")
root.geometry("900x500")
root.configure(bg=color_main_bg)

'''canvas = tk.Canvas(root, height=500, width=900, bg=color_main_bg)
canvas.pack()'''

#                                              FRAMES Y SUBFRAMES
frame = tk.Frame(root, bg=color_bg)
frame.place(relwidth=0.97, relheight=0.95, relx=0.015, rely=0.025)

frame.grid_rowconfigure(9, weight=1)
frame.grid_columnconfigure(3, weight=1)

frame_salinidad = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_salinidad.place(x="15", y="70")

frame_temperatura = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_temperatura.place(x="15", y="119")

frame_corriente = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_corriente.place(x="15", y="168")

frame_altura_laminal = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_altura_laminal.place(x="15", y="217")

frame_viscosidad = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_viscosidad.place(x="15", y="266")

frame_densidad = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_densidad.place(x="15", y="315")

frame_profundidad = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_profundidad.place(x="15", y="364")

frame_profundidad_colocacion = tk.Frame(frame, bg=color_bg_subframe, width="437", height="41")
frame_profundidad_colocacion.place(x="15", y="413")

frame_resultados2 = tk.Frame(frame, bg=color_bg_subframe, width="350", height="300") # width="350", height="300"
frame_resultados2.place(x="500", y="70")

frame_resultados = tk.Frame(frame, bg=color_bg_subframe, width="350", height="290")
frame_resultados.place(x="500", y="85")

frame_resultados.pack_propagate(False)


Title_cfg = font.Font(family='Nunito', size=25, weight="bold")
title = tk.Label(frame, text="Calculadora de Turbina", fg=color_font, bg=color_bg)
title['font'] = Title_cfg
title.config(anchor="center")

#title.pack(pady=10)
title.grid(row=0, column=1, pady=10)

parametros_cfg = font.Font(family='Nunito', size=15)

salinidad = tk.Label(frame, text="Salinidad", fg=color_font, bg=color_bg_subframe)
salinidad['font'] = parametros_cfg
#salinidad.pack()
salinidad.grid(row=1, column=0, sticky="W", padx=20, pady=10)

textbox_input_salinidad = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font)
textbox_input_salinidad.grid(row=1, column=1, sticky="w", padx=30)
# input_salinidad.insert("20-50")

temperatura = tk.Label(frame, text="Temperatura", fg=color_font, bg=color_bg_subframe)
temperatura['font'] = parametros_cfg
#temperatura.pack(anchor="nw", padx=20, pady=10)
temperatura.grid(row=2, column=0, sticky="W", padx=20, pady=10)

textbox_input_temperatura = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font)
textbox_input_temperatura.grid(row=2, column=1, sticky="w", padx=30)

corriente = tk.Label(frame, text="Corriente", fg=color_font, bg=color_bg_subframe)
corriente['font'] = parametros_cfg
#corriente.pack(anchor="nw", padx=20, pady=10)
corriente.grid(row=3, column=0, sticky="W", padx=20, pady=10)

textbox_input_corriente = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font)
textbox_input_corriente.grid(row=3, column=1, sticky="w", padx=30)

altura_laminal = tk.Label(frame, text="Altura Laminal", fg=color_font, bg=color_bg_subframe)
altura_laminal['font'] = parametros_cfg
altura_laminal.grid(row=4, column=0, sticky="W", padx=20, pady=10)

textbox_input_altura_laminal = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font)
textbox_input_altura_laminal.grid(row=4, column=1, sticky="w", padx=30)

viscosidad = tk.Label(frame, text="Viscosidad", fg=color_font, bg=color_bg_subframe)
viscosidad['font'] = parametros_cfg
viscosidad.grid(row=5, column=0, sticky="W", padx=20, pady=10)

textbox_input_viscosidad = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font)
textbox_input_viscosidad.grid(row=5, column=1, sticky="w", padx=30)

densidad = tk.Label(frame, text="Densidad", fg=color_font, bg=color_bg_subframe)
densidad['font'] = parametros_cfg
densidad.grid(row=6, column=0, sticky="W", padx=20, pady=10)

textbox_input_densidad = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font)
textbox_input_densidad.grid(row=6, column=1, sticky="w", padx=30)

profundidad = tk.Label(frame, text="Profundidad", fg=color_font, bg=color_bg_subframe)
profundidad['font'] = parametros_cfg
profundidad.grid(row=7, column=0, sticky="W", padx=20, pady=10)

textbox_input_profundidad = tk.Entry(frame, width=20, bg=color_textbox, fg=color_font)
textbox_input_profundidad.grid(row=7, column=1, sticky="w", padx=30)

profundidad_colocacion = tk.Label(frame, text="Profundidad de Colocación", fg=color_font, bg=color_bg_subframe)
profundidad_colocacion['font'] = parametros_cfg
profundidad_colocacion.grid(row=8, column=0, sticky="W", padx=20, pady=10)

textbox_input_profundidad_colocacion = tk.Entry(frame, width=20, bg=color_textbox)
textbox_input_profundidad_colocacion.grid(row=8, column=1, sticky="w", padx=30)

#                                                  BOTONES

button_cfg = font.Font(family='Nunito', size=12)

limpiar = tk.Button(frame, text="Limpiar", fg=color_font, bg=color_main_bg, height=1, width=10, command=clear_all) #, command=FuzzySystem.calcular()
limpiar['font'] = button_cfg
limpiar.grid(row=8, column=3, sticky="sw", pady=10)

calculate = tk.Button(frame, text="Calcular", fg=color_font, bg=color_main_bg, height=1, width=10, command=calcular) #, command=FuzzySystem.calcular()
calculate['font'] = button_cfg
calculate.grid(row=8, column=3, sticky="se", padx=15, pady=10)


def gui_sin_mapas():
    root.mainloop()
