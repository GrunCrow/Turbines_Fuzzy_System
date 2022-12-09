import cv2

# global variables
clicked = False
moving = False
depth_r = depth_g = depth_b = temperature_r = temperature_g = temperature_b = x_pos = y_pos = 0

# default image
# depth_map = cv2.imread("Color_Maps/maps/sea_depth.jpg")
depth_map = cv2.imread("Color_Maps/maps/sea_depth.jpg")
temperature_map = cv2.imread("Color_Maps/maps/sea_surface_temperature.jpg")


def single_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global depth_b, depth_g, depth_r, temperature_b, temperature_g, temperature_r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y

        depth_b, depth_g, depth_r = depth_map[y, x]
        temperature_b, temperature_g, temperature_r = temperature_map[y, x]

        depth_b = int(depth_b)
        depth_g = int(depth_g)
        depth_r = int(depth_r)

        temperature_b = int(temperature_b)
        temperature_g = int(temperature_g)
        temperature_r = int(temperature_r)

        # print("Depth = " + str(depth_r) + " " + str(depth_g) + " " + str(depth_b))
        # print("Temperature = " + str(temperature_r) + " " + str(temperature_g) + " " + str(temperature_b))


# function for detecting left mouse click
def click(event, x, y, flags, param):
    global clicked, x_pos, y_pos
    if event == cv2.EVENT_LBUTTONDOWN:
        x_pos = x
        y_pos = y
        clicked = True


def coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        global x_pos, y_pos, moving
        x_pos = x
        y_pos = y
        moving = True
