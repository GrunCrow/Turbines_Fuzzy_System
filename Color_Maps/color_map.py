from Color_Maps import image_detector


def get_depth(depth_red, depth_green, depth_blue):
    depth = 8000
    if depth_red == 0 & depth_green == 0 & depth_blue == 0:
        depth = 0
    elif depth_red <= 8 & depth_green <= 50 & depth_blue <= 110:
        depth = 8000
    elif depth_red <= 9 & depth_green <= 82 & depth_blue <= 157:  # 7000
        depth = 7000
    elif depth_red <= 34 & depth_green <= 114 & depth_blue <= 182:  # 6000
        depth = 6000
    elif depth_red <= 66 & depth_green <= 146 & depth_blue <= 198:  # 5000
        depth = 5000
    elif depth_red <= 109 & depth_green <= 175 & depth_blue <= 214:  # 4000
        depth = 4000
    elif depth_red <= 161 & depth_green <= 203 & depth_blue <= 226:  # 3000
        depth = 3000
    elif depth_red <= 199 & depth_green <= 220 & depth_blue <= 240:  # 2000
        depth = 2000
    elif depth_red <= 224 & depth_green <= 236 & depth_blue <= 248:  # 1000
        depth = 1000
    elif depth_red <= 236 & depth_green <= 244 & depth_blue <= 252:  # 500
        depth = 500
    elif depth_red <= 242 & depth_green <= 248 & depth_blue <= 254:  # 250
        depth = 250
    elif depth_red <= 245 & depth_green <= 250 & depth_blue <= 255:  # 125
        depth = 125
    elif depth_red < 255 & depth_green < 255 & depth_blue < 255:  # 0
        depth = 50

    return depth


def get_temperature(temperature_red, temperature_green, temperature_blue):
    temperature = 0

    if (temperature_red == 0) & (temperature_green == 0) & (temperature_blue == 0):
        temperature = 40
    elif (temperature_red <= 16) & (temperature_green <= 20) & (temperature_blue <= 88):
        temperature = -5
    elif (temperature_red <= 17) & (temperature_green <= 26) & (temperature_blue <= 92):
        temperature = 2
    elif (temperature_red <= 32) & (temperature_green <= 43) & (temperature_blue <= 114):  # 7000
        temperature = 4
    elif (temperature_red <= 48) & (temperature_green <= 53) & (temperature_blue <= 128):  # 6000
        temperature = 6
    elif (temperature_red <= 64) & (temperature_green <= 64) & (temperature_blue <= 140):  # 5000
        temperature = 8
    elif (temperature_red <= 85) & (temperature_green <= 71) & (temperature_blue <= 143):  # 4000
        temperature = 10
    elif (temperature_red <= 108) & (temperature_green <= 82) & (temperature_blue <= 147):  # 3000
        temperature = 12
    elif (temperature_red <= 132) & (temperature_green <= 91) & (temperature_blue <= 150):  # 2000
        temperature = 15
    elif (temperature_red <= 155) & (temperature_green <= 101) & (temperature_blue <= 153):  # 1000
        temperature = 17
    elif (temperature_red <= 166) & (temperature_green <= 108) & (temperature_blue <= 147):  # 500
        temperature = 20
    elif (temperature_red <= 178) & (temperature_green <= 115) & (temperature_blue <= 144):  # 250
        temperature = 22
    elif (temperature_red <= 191) & (temperature_green <= 125) & (temperature_blue <= 138):  # 125
        temperature = 24
    elif (temperature_red <= 205) & (temperature_green <= 136) & (temperature_blue <= 135):  # 0
        temperature = 26
    elif (temperature_red <= 218) & (temperature_green <= 161) & (temperature_blue <= 152):  # 0
        temperature = 28
    elif (temperature_red <= 230) & (temperature_green <= 189) & (temperature_blue <= 170):  # 0
        temperature = 30
    elif (temperature_red <= 245) & (temperature_green <= 218) & (temperature_blue <= 188):  # 0
        temperature = 32
    elif (temperature_red <= 255) & (temperature_green <= 244) & (temperature_blue <= 207):  # 0
        temperature = 35

    return temperature


def color_map():
    file = "Color_Maps/maps/sea_depth.jpg"

    depth_red, depth_green, depth_blue, temperature_red, temperature_green, temperature_blue =\
        image_detector.color_detector(file)

    depth = get_depth(depth_red, depth_green, depth_blue)

    temperature = get_temperature(temperature_red, temperature_green, temperature_blue)

    return depth, temperature




