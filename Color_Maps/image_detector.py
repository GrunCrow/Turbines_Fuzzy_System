import cv2
from Color_Maps import color_recognition as cr

# define image

red = 0
green = 0
blue = 0


def color_detector(img_name):
    img = cv2.imread(img_name)
    cr.load_img(img)

    cv2.resize(img, (0, 0), fx=0.99, fy=0.99)
    cv2.namedWindow('Map')
    cv2.setMouseCallback('Map', cr.single_click)

    clicked = False

    while 1:
        cv2.imshow("Map", img)

        if cr.clicked:
            '''# cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
            cv2.rectangle(img, (20, 20), (750, 60), (cr.b, cr.g, cr.r), -1)
            # Creating text string to display( Color name and RGB values )
            text = cr.recognize_color(cr.r, cr.g, cr.b) + ' R=' + str(cr.r) + ' G=' + str(cr.g) + ' B=' + str(cr.b)

            # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
            cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            # For very light colours we will display text in black colour
            if cr.r + cr.g + cr.b >= 600:
                cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)'''

            global red, green, blue
            red = cr.r
            green = cr.g
            blue = cr.b

            # print(red, green, blue)
            cr.clicked = False
            clicked = True

        # Break the loop when user hits 'esc' key
        if cv2.waitKey(20) & 0xFF == 27 or clicked:
            if clicked:
                cv2.destroyAllWindows()
                return red, green, blue
            break

    cv2.destroyAllWindows()
