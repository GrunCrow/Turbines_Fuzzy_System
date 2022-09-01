from Color_Maps import image_detector


def color_map():
    file = "Color_Maps/maps/sea_depth.jpg"
    red, green, blue = image_detector.color_detector(file)

    print(red, green, blue)




