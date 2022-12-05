import cv2
from Color_Maps import color_recognition as cr

# define image

depth_red = depth_green = depth_blue = temperature_red = temperature_green = temperature_blue = 0


def zoom_at(img, zoom, coord=None):
    """
    Simple image zooming without boundary checking.
    Centered at "coord", if given, else the image center.

    img: numpy.ndarray of shape (h,w,:)
    zoom: float
    coord: (float, float)
    """
    # Translate to zoomed coordinates
    h, w, _ = [zoom * i for i in img.shape]

    if coord is None:
        cx, cy = w / 2, h / 2
    else:
        cx, cy = [zoom * c for c in coord]

    img = cv2.resize(img, (0, 0), fx=zoom, fy=zoom)
    img = img[int(round(cy - h / zoom * .5)): int(round(cy + h / zoom * .5)),
          int(round(cx - w / zoom * .5)): int(round(cx + w / zoom * .5)),
          :]

    return img


def color_detector(img):
    image = cv2.imread(img)
    overlay = image.copy()

    # cv2.resize(img, (0, 0), fx=0.99, fy=0.99)
    cv2.namedWindow('Map')
    cv2.setMouseCallback('Map', cr.single_click)
    # cv2.setMouseCallback('Map', cr.coordinates)

    clicked = False
    num_clicks = 0

    while 1:
        cv2.imshow("Map", overlay)

        '''if cr.moving:
            # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
            # cv2.rectangle(overlay, (0, 0), (1440, 40), (0, 0, 0), -1)
            #alpha = 0.4  # Transparency factor.
            # Following line overlays transparent rectangle over the image
            # image_new = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

            # Creating text string to display( Color name and RGB values )
            text = "X: " + str(cr.x_pos) + " Y: " + str(cr.y_pos)

            # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
            cv2.putText(overlay, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)'''

        if cr.clicked:
            if num_clicks == 0:
                overlay = zoom_at(overlay, 2, (cr.x_pos, cr.y_pos))
                print(cr.x_pos, cr.y_pos)
                num_clicks += 1
                cr.clicked = False
            else:
                global depth_red, depth_green, depth_blue, temperature_red, temperature_green, temperature_blue
                depth_red = cr.depth_r
                depth_green = cr.depth_g
                depth_blue = cr.depth_b
                print(depth_red, depth_green, depth_blue)

                temperature_red = cr.temperature_r
                temperature_green = cr.temperature_g
                temperature_blue = cr.temperature_b

                # print(red, green, blue)
                cr.clicked = False
                clicked = True

        # Break the loop when user hits 'esc' key
        if cv2.waitKey(20) & 0xFF == 27 or clicked:
            if clicked:
                clicked = False
                num_clicks = 0
                cv2.destroyAllWindows()
                return depth_red, depth_green, depth_blue, temperature_red, temperature_green, temperature_blue
            break

    cv2.destroyAllWindows()
