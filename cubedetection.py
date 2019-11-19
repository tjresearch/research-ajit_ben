import time
import cv2
from PIL import Image

cube = cv2.VideoCapture('small.mp4')

time.sleep(0.1)

# set the lists for all 6 sides to white for initialize
top = ("W", "W", "W", "W", "W", "W", "W", "W", "W")
bottom = ("W", "W", "W", "W", "W", "W", "W", "W", "W")
left = ("W", "W", "W", "W", "W", "W", "W", "W", "W")
right = ("W", "W", "W", "W", "W", "W", "W", "W", "W")
front = ("W", "W", "W", "W", "W", "W", "W", "W", "W")
back = ("W", "W", "W", "W", "W", "W", "W", "W", "W")
# set flags that all side are not completed
top_complete = False
bottom_complete = False
left_complete = False
right_complete = False
front_complete = False
back_complete = False

# initialize working face to nil
face = []


# routine for counting number of each color has appeaded on each face. Used at the end to ensure there is
# 9 of each colour before exiting
def count_colours(fcheck, countall):
    (wcount, bcount, rcount, gcount, ycount, ocount) = countall
    for pos in range(9):
        if fcheck[pos] == "W":
            wcount += 1
        elif fcheck[pos] == "B":
            bcount += 1
        elif fcheck[pos] == "R":
            rcount += 1
        elif fcheck[pos] == "G":
            gcount += 1
        elif fcheck[pos] == "Y":
            ycount += 1
        elif fcheck[pos] == "O":
            ocount += 1
    countall = (wcount, bcount, rcount, gcount, ycount, ocount)
    return countall

    # routine for drawing the read faces on the screen


def draw_face(colorss, x, y):
    toprow = colorss[0:3]
    midrow = colorss[3:6]
    lastrrow = colorss[6:9]
    tile_color = (0, 0, 0)
    # draw a black square as background
    cv2.rectangle(image, (0 + x, 0 + y), (65 + x, 65 + y), (0, 0, 0), -1)

    # draw the coloured squares for top row
    for pos in range(3):
        if toprow[pos] == "W":
            tile_color = (255, 255, 255)
        elif toprow[pos] == "G":
            tile_color = (0, 255, 0)
        elif toprow[pos] == "B":
            tile_color = (255, 0, 0)
        elif toprow[pos] == "R":
            tile_color = (0, 0, 255)
        elif toprow[pos] == "O":
            tile_color = (0, 100, 255)
        elif toprow[pos] == "Y":
            tile_color = (50, 255, 255)
        elif toprow[pos] == "N":
            tile_color = (0, 0, 0)
        cv2.rectangle(image, (20 * pos + 5 + x, 5 + y), (20 * pos + 20 + x, 20 + y), tile_color, -1)

    # draw the coloured squares for middle row
    for pos in range(3):
        if midrow[pos] == "W":
            tile_color = (255, 255, 255)
        elif midrow[pos] == "G":
            tile_color = (0, 255, 0)
        elif midrow[pos] == "B":
            tile_color = (255, 0, 0)
        elif midrow[pos] == "R":
            tile_color = (0, 0, 255)
        elif midrow[pos] == "O":
            tile_color = (0, 100, 255)
        elif midrow[pos] == "Y":
            tile_color = (50, 255, 255)
        elif middle_row[pos] == "N":
            tile_color = (0, 0, 0)
        cv2.rectangle(image, (20 * pos + 5 + x, 25 + y), (20 * pos + 20 + x, 40 + y), tile_color, -1)

    # draw the coloured squares for bottom row
    for pos in range(3):
        if lastrrow[pos] == "W":
            tile_color = (255, 255, 255)
        elif lastrrow[pos] == "G":
            tile_color = (0, 255, 0)
        elif lastrrow[pos] == "B":
            tile_color = (255, 0, 0)
        elif lastrrow[pos] == "R":
            tile_color = (0, 0, 255)
        elif lastrrow[pos] == "O":
            tile_color = (0, 100, 255)
        elif lastrrow[pos] == "Y":
            tile_color = (50, 255, 255)
        elif lastrrow[pos] == "N":
            tile_color = (0, 0, 0)
        cv2.rectangle(image, (20 * pos + 5 + x, 45 + y), (20 * pos + 20 + x, 60 + y), tile_color, -1)

# loop for capturing frames from camera in raw YUV format for the purpose of adjusting brightness


pos_frame = cube.get(cv2.CAP_PROP_POS_FRAMES)
while cube.isOpened():
    flag, image = cube.read()
    if flag:
        # The frame is ready and already captured
        cv2.imshow('video', image)
        pos_frame = cube.get(cv2.CAP_PROP_POS_FRAMES)

        # grab the raw NumPy array representing the image, then initialize the timestamp
        # image = Image.open(frame)
        # find the mean of all the image
        (Y, U, V, DA) = cv2.mean(image)
    else:
        # The next frame is not ready, so we try to read it again
        cube.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
        # It is better to wait for a while for the next frame to be ready
        cv2.waitKey(1000)

    if cv2.waitKey(10) == 27:
        break
    if cube.get(cv2.CAP_PROP_POS_FRAMES) == cube.get(cv2.CAP_PROP_FRAME_COUNT):
        # If the number of captured frames is equal to the total number of frames,
        # we stop
        break

    # Main loop for capturing frames from camera in raw YUV format
retval, image = cube.read()
while retval:
    # grab the raw NumPy array representing the image, then initialize the timestamp

    # create serval biniary masks to issolate the colours we are looking for
    White_Yellow_mask = cv2.inRange(image, (100, 40, 90), (255, 255, 255))
    Red_mask = cv2.inRange(image, (0, 0, 143), (255, 255, 255))
    Green_mask = cv2.inRange(image, (60, 50, 50), (150, 170, 110))
    Center_Green_Mask = cv2.inRange(image, (20, 60, 50), (80, 130, 110))
    Blue_Mask = cv2.inRange(image, (20, 95, 50), (90, 200, 115))

    # Combined all the biniary masks together to get one image with all needed data
    Combined_image = cv2.bitwise_or(White_Yellow_mask, Red_mask)
    Combined_image = cv2.bitwise_or(Green_mask, Combined_image)
    Combined_image = cv2.bitwise_or(Center_Green_Mask, Combined_image)
    Combined_image = cv2.bitwise_or(Blue_Mask, Combined_image)

    # look for countours in the combined binary mask
    im2, contours2, hierarchy = cv2.findContours(Combined_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    candidates = []
    index = 0
    # loop through the cpountours to find the ones we want
    for c in contours2:
        # approxPolyDP to find strainght line contours
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.06 * peri, True)
        # find countours made up for 4 lines
        if len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            # find aspect ratio of boundary rectangle around the countours
            ar = w / float(h)
            # get the area of ther countour
            area = cv2.contourArea(contours2[index])
            # if the countour has AR close to 1 i.e close to square not rectangle and area of countour is
            # close to area of box around countouour i.e not diamonmd or robus add it to candidates list
            if 1.3 > ar > .7 and 90 > w > 30 and area / (w * h) > .4:
                candidates.append((x, y, w, h))
        index += 1

    new = candidates
    # loop through all the countours in the candidantes list
    for d in new:
        neighbors = 0
        (x, y, w, h) = d
        for (x2, y2, w2, h2) in new:
            # count up how many neighbors closer than width * 3.5 each countour in candidanteslist has
            if abs(x - x2) < (w * 3.5) and abs(y - y2) < (h * 3.5):
                neighbors += 1
        # any candidantes with less than 5 neighbors remove
        if neighbors < 5:
            candidates.remove(d)

    # sort candidates if there's 9 of them
    tmp = []
    if len(candidates) == 9:
        # Write to tmp the center y,x of candidantes so that we can sort in y direction
        for (x3, y3, w3, h3) in candidates:
            tmp.append((y3 + (h3 / 2), x3 + (w3 / 2)))
        tmp = sorted(tmp)
        # cut into sets of 3 i.e the 3 rows of colours
        top_row = tmp[0:3]
        tmp = tmp[3:9]
        tmp = sorted(tmp)
        middle_row = tmp[0:3]
        bottom_row = tmp[3:6]

        # sort top_row
        temp_row = []
        # write to temp_row the center x,y for sorting in x direction
        for (y4, x4) in top_row:
            temp_row.append((x4, y4))
        # sort top_row
        top_row = temp_row
        top_row = sorted(top_row)

        # sort middle_row
        temp_row = []
        for (y4, x4) in middle_row:
            temp_row.append((x4, y4))
        middle_row = temp_row
        middle_row = sorted(middle_row)

        # sort bottom_row
        temp_row = []
        for (y4, x4) in bottom_row:
            temp_row.append((x4, y4))
        bottom_row = temp_row
        bottom_row = sorted(bottom_row)

        face = []
        # loop through the 3 positions in each row for the purpose to detacting colour of each tile
        for pos in range(3):
            # cut out a 10x10 cube around center of contour
            x, y = top_row[pos]
            cube = image[y - 5:y + 5, x - 5:x + 5]
            # find the mean of that cube
            (Y, U, V, DA) = cv2.mean(cube)
            # identify each color and write the detected colour to the face list
            if Y > 120 and float(U / V) > 0.9:
                face.append("W")
            elif U > 130 and U > V and float(U / Y) > 1.15:
                face.append("B")
            elif 2 > float(U / V) > 1.1:
                face.append("G")
            elif V > 120 and float(U / Y) > 0.7:
                if float(U / Y) < 1.9:
                    face.append("O")
                else:
                    face.append("R")
            elif Y > 110 and float(V / U) > 0.95:
                face.append("Y")

        # just doing same as above but for middle row
        for pos in range(3):
            x, y = middle_row[pos]
            cube = image[y - 5:y + 5, x - 5:x + 5]
            (Y, U, V, DA) = cv2.mean(cube)
            if Y > 120 and float(U / V) > 0.9:
                face.append("W")
            elif U > 130 and U > V and float(U / Y) > 1.15:
                face.append("B")
            elif pos == 1 and 1.9 > float(U / V) > 1:
                face.append("G")
            elif 1.9 > float(U / V) > 1.1:
                face.append("G")
            elif V > 120 and float(U / Y) > 0.7:
                if float(U / Y) < 1.9:
                    face.append("O")
                else:
                    face.append("R")
            elif Y > 110 and float(V / U) > 0.95:
                face.append("Y")

        # one more time for bottom row
        for pos in range(3):
            x, y = bottom_row[pos]
            cube = image[y - 5:y + 5, x - 5:x + 5]
            (Y, U, V, DA) = cv2.mean(cube)
            if Y > 120 and float(U / V) > 0.9:
                face.append("W")
            elif U > 130 and U > V and float(U / Y) > 1.15:
                face.append("B")
            elif 2 > float(U / V) > 1.1:
                face.append("G")
            elif V > 120 and float(U / Y) > 0.7:
                if float(U / Y) < 1.9:
                    face.append("O")
                else:
                    face.append("R")
            elif Y > 110 and float(V / U) > 0.95:
                face.append("Y")

    # convert the image from raw YUV format to RGB for user viewing
    image = cv2.cvtColor(image, cv2.COLOR_YUV2RGB)
    # if there was 9 colours dectected then check middle tile to know which face to update.
    if len(face) == 9:
        # draw the current face in top left of viewing image
        draw_face(face, 0, 0)
        # based unpon which colour the center tile is update that face for the detected colours and
        # switch the flag that face has been read completly
        if face[4] == "W":
            top = face
            top_complete = True
        elif face[4] == "G":
            front = face
            front_complete = True
        elif face[4] == "R":
            right = face
            right_complete = True
        elif face[4] == "O":
            left = face
            left_complete = True
        elif face[4] == "B":
            back = face
            back_complete = True
        elif face[4] == "Y":
            bottom = face
            bottom_complete = True

    # draw the all the faces on the viewing image
    draw_face(left, 0, 350)
    draw_face(front, 65, 350)
    draw_face(top, 65, 285)
    draw_face(bottom, 65, 415)
    draw_face(right, 130, 350)
    draw_face(back, 195, 350)

    # draw circles of all the candidates on the viewing image
    for (x, y, w, h) in candidates:
        cv2.circle(image, (x + w / 2, y + h / 2), int(w / 1.8), (255, 0, 255), 3)

    # Display the viewing image
    cv2.imshow("Orginial", image)

    # check to see if all faces have been read
    if top_complete and bottom_complete and front_complete and back_complete and left_complete and right_complete:
        # if all faces read then count up how many of each colour has been detacted
        countall = (0, 0, 0, 0, 0, 0)
        countall = count_colours(top, countall)
        countall = count_colours(bottom, countall)
        countall = count_colours(front, countall)
        countall = count_colours(back, countall)
        countall = count_colours(left, countall)
        countall = count_colours(right, countall)
        (wcount, bcount, rcount, gcount, ycount, ocount) = countall
        # if there is 9 of each colour then write result to file and break from loop
        if bcount == 9 and rcount == 9 and gcount == 9 and wcount == 9 and ycount == 9 and ocount == 9:
            cubefile = open('/home/pi/Sage/MacTwist.txt', "w")
            cubefile.write("Front" + "\n")
            for ch in front:
                cubefile.write(ch)
            cubefile.write("\n")
            cubefile.write("Bottom" + "\n")
            for ch in bottom:
                cubefile.write(ch)
            cubefile.write("\n")
            cubefile.write("Left" + "\n")
            for ch in left:
                cubefile.write(ch)
            cubefile.write("\n")
            cubefile.write("Right" + "\n")
            for ch in right:
                cubefile.write(ch)
            cubefile.write("\n")
            cubefile.write("Top" + "\n")
            for ch in top:
                cubefile.write(ch)
            cubefile.write("\n")
            cubefile.write("Back" + "\n")
            for ch in back:
                cubefile.write(ch)
            cubefile.write("\n")
            cubefile.close()
            break

        # Check for key pressed
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    retval, image = cube.read()
# close video file
