# Task 2: Color Identification on Image or in Video.
# >> Talupula Jahnavi

# Here we import some required Libraries like Opencv (cv2) and pandas.
import cv2
import pandas as pd

# read the image which we select for task.
img = cv2.imread("task3.jpg")

# Here declaring global variables (are used later)
clicked = False
r = g = b = x_pos = y_pos = 0

# Here we read csv file having color info using pandas library
index = ["color", "color_name", "hexadecimal", "R", "G", "B"]
csv = pd.read_csv('colors2.csv', names=index, header=None)

# Here we creat a function to calculate minimum distance from all colors and get the most matching color which we select.
def get_color_name(R, G, B):
    global cname
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# Here we creat another function to get value of  x,y coordinates of mouse double click.
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# Here we give name for Output window.
cv2.namedWindow('image')
# set callback function of mouse.
cv2.setMouseCallback('image', draw_function)

while True:
    # commond for showing our Output
    cv2.imshow("image", img)
    if clicked:
        # Here now we right code for showing our Output.
        # Creating as a background in the form of Rectangle.
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # Creating text string to display RGB Values.
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # for text
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        clicked = False

    # using for breaking the loop, for that used 'esc' key.
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
print('Thank you..!')
