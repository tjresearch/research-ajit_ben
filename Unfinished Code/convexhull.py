import cv2
import numpy as np
import math

src = cv2.imread("cube.jpeg") # read input image
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) # convert to grayscale
blur = cv2.blur(gray, (3, 3)) # blur the image
ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)

edges = cv2.Canny(gray, 60, 120)
contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = []

# calculate points for each contour
for c in contours:
    # creating convex hull object for each contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.06 * peri, True)
    # find countours made up for 4 lines
    if len(approx) == 6:
        (x, y, w, h) = cv2.boundingRect(approx)
        if w > 150:
            hull.append(cv2.convexHull(c, clockwise=True))
            # hull.append(approx)
            # hull.append(c)
            # print(c)

drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

# draw contours and hull points
for i in range(len(contours)):
    color_contours = (0, 255, 0)  # green - color for contours
    color = (255, 0, 0)  # blue - color for convex hull
    # draw ith contour
    # cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
    cv2.imwrite('contours.jpeg', drawing)

for i in range(len(hull)):
    # draw ith convex hull object
    color = (255, 0, 0)
    cv2.drawContours(drawing, hull, i, color, 1, 8)
    cv2.imwrite('countours.jpeg', drawing)

# print(hull)
num = len(hull[0])
newhull = []
hexagon = []
for i in range(num):
    j = (i - 1) % num
    k = (i + 1) % num
    # print(hull[0][0][0][1])
    ji = [hull[0][j][0][0] - hull[0][i][0][0], hull[0][j][0][1] - hull[0][i][0][1]]
    ki = [hull[0][k][0][0] - hull[0][i][0][0], hull[0][k][0][1] - hull[0][i][0][1]]
    cp = (ji[0])*(ki[0]) + (ji[1])*(ki[1])
    jmag = math.sqrt(ji[0]**2 + ji[1]**2)
    kmag = math.sqrt(ki[0]**2 + ki[1]**2)
    ang = math.acos(cp/jmag/kmag)
    if math.fabs(math.pi - ang) > 0.2:
        newhull.append(hull[0][i][0])
img = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
for i in range(len(newhull)):
    j = (i + 1) % len(newhull)
    ji = [newhull[j][0] - newhull[i][0], newhull[j][1] - newhull[i][1]]
    jmag = math.sqrt(ji[0]**2 + ji[1]**2)
    if jmag > 10:
        hexagon.append(newhull[i])
for i in range(len(hexagon)):
    j = (i + 1) % len(hexagon)
    cv2.line(img, (hexagon[i][0], hexagon[i][1]), (hexagon[j][0], hexagon[j][1]), (255,0,0),5)
    cv2.circle(img, (hexagon[i][0], hexagon[i][1]), 10, (0, 0, 255), -1)
cv2.imwrite('contours.jpeg', img)
print(hexagon)
xsum = 0
ysum = 0
for i in range(6):
    xsum += hexagon[i][0]
    ysum += hexagon[i][1]
topcenter = (hexagon[])
for i in range(3):
    for j in range(3):

