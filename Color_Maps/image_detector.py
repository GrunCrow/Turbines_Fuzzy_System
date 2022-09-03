import cv2
from Color_Maps import color_recognition as cr

# define image

depth_red = depth_green = depth_blue = temperature_red = temperature_green = temperature_blue = 0


def color_detector(img):
    image = cv2.imread(img)
    overlay = image.copy()

    # cv2.resize(img, (0, 0), fx=0.99, fy=0.99)
    cv2.namedWindow('Map')
    cv2.setMouseCallback('Map', cr.single_click)
    # cv2.setMouseCallback('Map', cr.coordinates)

    clicked = False

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
            global depth_red, depth_green, depth_blue, temperature_red, temperature_green, temperature_blue
            depth_red = cr.depth_r
            depth_green = cr.depth_g
            depth_blue = cr.depth_b

            temperature_red = cr.temperature_r
            temperature_green = cr.temperature_g
            temperature_blue = cr.temperature_b

            # print(red, green, blue)
            cr.clicked = False
            clicked = True

        # Break the loop when user hits 'esc' key
        if cv2.waitKey(20) & 0xFF == 27 or clicked:
            if clicked:
                cv2.destroyAllWindows()
                return depth_red, depth_green, depth_blue, temperature_red, temperature_green, temperature_blue
            break

    cv2.destroyAllWindows()
