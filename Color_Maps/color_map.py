from Turbines_Fuzzy_System.Color_Maps import image_detector

'''
Functions to get the value of the parameter depending of the RGB value where the user has clicked
'''

# current in knots firstly and then changed to cm/s
def get_current(current_red, current_green, current_blue):
    current = -1000

    if (current_red == 192) & (current_green == 192) & (current_blue == 192):
        current = -2000
    elif current_red == 2 & current_green == 2 & current_blue == 2:
        current = 0
    elif current_red <= 28 & current_green <= 28 & current_blue <= 28:  # 7000
        current = 0.25
    elif current_red <= 52 & current_green <= 52 & current_blue <= 52:  # 6000
        current = 0.5
    elif current_red <= 79 & current_green <= 79 & current_blue <= 79:  # 5000
        current = 0.75
    elif current_red <= 101 & current_green <= 101 & current_blue <= 101:  # 4000
        current = 1
    elif current_red <= 112 & current_green <= 112 & current_blue <= 112:  # 3000
        current = 1.25
    elif current_red <= 119 & current_green <= 119 & current_blue <= 119:  # 2000
        current = 1.5
    elif current_red <= 126 & current_green <= 126 & current_blue <= 126:  # 1000
        current = 1.75
    elif current_red <= 134 & current_green <= 134 & current_blue <= 134:  # 500
        current = 2
    elif current_red <= 138 & current_green <= 138 & current_blue <= 138:  # 125
        current = 2.5
    elif current_red <= 141 & current_green <= 141 & current_blue <= 141:  # 125
        current = 3
    elif current_red <= 147 & current_green <= 147 & current_blue <= 147:  # 125
        current = 3.5
    elif current_red <= 154 & current_green <= 154 & current_blue <= 154:  # 125
        current = 4
    elif current_red <= 157 & current_green <= 157 & current_blue <= 157:  # 125
        current = 4.5
    elif current_red <= 160 & current_green <= 160 & current_blue <= 160:  # 125
        current = 5
    '''elif current_red < 255 & current_green < 255 & current_blue < 255:  # 0
        current = 0'''

    # from knot to cm/s
    if current > 0:
        current *= 51.4444

    return round(current, 2)

# ERRORS:
    # if salinity = -1000 -> no value founded
    # else if salinity = -2000 -> clicked on the ground -> not possible as turbine need to be placed at the sea/ocean
def get_salinity(salinity_red, salinity_green, salinity_blue):
    salinity = -1000

    if (salinity_red == 192) & (salinity_green == 192) & (salinity_blue == 192):
        salinity = -2000
    elif (salinity_red <= 28) & (salinity_green <= 28) & (salinity_blue <= 28):
        salinity = 0
    elif (salinity_red <= 38) & (salinity_green <= 38) & (salinity_blue <= 38):  # 7000
        salinity = 2.5
    elif (salinity_red <= 48) & (salinity_green <= 48) & (salinity_blue <= 48):  # 6000
        salinity = 5
    elif (salinity_red <= 58) & (salinity_green <= 58) & (salinity_blue <= 58):  # 5000
        salinity = 7.5
    elif (salinity_red <= 64) & (salinity_green <= 64) & (salinity_blue <= 64):  # 4000
        salinity = 10
    elif (salinity_red <= 70) & (salinity_green <= 70) & (salinity_blue <= 70):  # 3000
        salinity = 15
    elif (salinity_red <= 103) & (salinity_green <= 103) & (salinity_blue <= 103):  # 2000
        salinity = 20
    elif (salinity_red <= 108) & (salinity_green <= 108) & (salinity_blue <= 108):  # 1000
        salinity = 22.5
    elif (salinity_red <= 113) & (salinity_green <= 113) & (salinity_blue <= 113):  # 500
        salinity = 25
    elif (salinity_red <= 118) & (salinity_green <= 118) & (salinity_blue <= 118):  # 250
        salinity = 27.5
    elif (salinity_red <= 123) & (salinity_green <= 123) & (salinity_blue <= 123):  # 125
        salinity = 30
    elif (salinity_red <= 145) & (salinity_green <= 145) & (salinity_blue <= 145):  # 0
        salinity = 32.5
    elif (salinity_red <= 180) & (salinity_green <= 180) & (salinity_blue <= 180):  # 0
        salinity = 35
    elif (salinity_red <= 255) & (salinity_green <= 244) & (salinity_blue <= 207):  # 0
        salinity = -1000

    return salinity

# ERRORS:
    # if temperature = -1000 -> no value founded
    # else if temperature = -2000 -> clicked on the ground -> not possible as turbine need to be placed at the sea/ocean
def get_temperature(temperature_red, temperature_green, temperature_blue):
    temperature = -1000

    if (temperature_red == 192) & (temperature_green == 192) & (temperature_blue == 192):
        temperature = -2000
    elif (temperature_red <= 0) & (temperature_green <= 0) & (temperature_blue <= 0):
        temperature = 0
    elif (temperature_red <= 3) & (temperature_green <= 3) & (temperature_blue <= 3):
        temperature = 10
    elif (temperature_red <= 10) & (temperature_green <= 10) & (temperature_blue <= 10):  # 7000
        temperature = 12.5
    elif (temperature_red <= 45) & (temperature_green <= 45) & (temperature_blue <= 45):  # 6000
        temperature = 15
    elif (temperature_red <= 61) & (temperature_green <= 61) & (temperature_blue <= 61):  # 5000
        temperature = 17.5
    elif (temperature_red <= 70) & (temperature_green <= 70) & (temperature_blue <= 70):  # 4000
        temperature = 20
    elif (temperature_red <= 76) & (temperature_green <= 76) & (temperature_blue <= 76):  # 3000
        temperature = 22.5
    elif (temperature_red <= 86) & (temperature_green <= 86) & (temperature_blue <= 86):  # 2000
        temperature = 25
    elif (temperature_red <= 98) & (temperature_green <= 98) & (temperature_blue <= 98):  # 1000
        temperature = 27.5
    elif (temperature_red <= 113) & (temperature_green <= 113) & (temperature_blue <= 113):  # 500
        temperature = 30
    elif (temperature_red <= 127) & (temperature_green <= 127) & (temperature_blue <= 127):  # 250
        temperature = 32.5
    elif (temperature_red <= 147) & (temperature_green <= 147) & (temperature_blue <= 147):  # 125
        temperature = 35
    elif (temperature_red <= 164) & (temperature_green <= 164) & (temperature_blue <= 164):  # 0
        temperature = 37.5
    elif (temperature_red <= 184) & (temperature_green <= 184) & (temperature_blue <= 184):  # 0
        temperature = 40

    return temperature


def color_map():
    # file = "Color_Maps/maps/sea_depth.jpg"
    file = "Color_Maps/maps/map.png"

    salinity_red, salinity_green, salinity_blue,\
    current_red, current_green, current_blue,\
    temperature_red, temperature_green, temperature_blue =\
        image_detector.color_detector(file)

    salinity = get_salinity(salinity_red, salinity_green, salinity_blue)
    print("SALINITY \nRed: " + str(salinity_red) + "\nGreen: " + str(salinity_green) + "\nBlue: " + str(salinity_blue) + "\n")

    current = get_current(current_red, current_green, current_blue)
    print("CURRENT \nRed: " + str(current_red) + "\nGreen: " + str(current_green) + "\nBlue: " + str(current_blue) + "\n")

    temperature = get_temperature(temperature_red, temperature_green, temperature_blue)
    print("TEMPERATURE \nRed: " + str(temperature_red) + "\nGreen: " + str(temperature_green) + "\nBlue: " + str(temperature_blue) + "\n")

    # depth = get_depth(depth_red, depth_green, depth_blue)

    return salinity, current, temperature




