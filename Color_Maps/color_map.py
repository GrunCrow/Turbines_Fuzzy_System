from Color_Maps import image_detector


def set_depth(depth_red, depth_green, depth_blue):
    # 245 250 254 to 185 214 232
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

    print(depth)
    return depth

def color_map():
    # file = "Color_Maps/maps/sea_depth.jpg"
    file = "Color_Maps/maps/sea_depth.jpg"
    depth_red, depth_green, depth_blue = image_detector.color_detector(file)

    depth = set_depth(depth_red, depth_green, depth_blue)

    return depth

    # print(depth_red, depth_green, depth_blue)




