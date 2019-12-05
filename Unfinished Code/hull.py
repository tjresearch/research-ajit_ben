import cv2
import numpy as np
import math

src = cv2.imread("cube1.jpeg")  # read input image
edges = cv2.Canny(src, 60, 120)
cv2.imwrite('edges.jpeg', edges)
src = cv2.imread("edges.jpeg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) # convert to grayscale
blur = cv2.blur(gray, (3, 3))  # blur the image
ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
hull = []
# calculate points for each contour
for i in range(len(contours)):
    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

# draw contours and hull points
for i in range(len(contours)):
    color_contours = (0, 255, 0)  # green - color for contours
    color = (255, 0, 0)  # blue - color for convex hull
    # draw ith contour
    # cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
    # draw ith convex hull object
    # cv2.drawContours(drawing, hull, i, color, 1, 8)
maxwidth = 0
best = 0
for i in range(len(hull)):
    peri = cv2.arcLength(hull[i], True)
    if peri > maxwidth:
        maxwidth = peri
        best = i
cv2.drawContours(drawing, hull, best, (255, 0, 0), 1, 8)
# for i in range(len(hull[best])):
    # cv2.circle(drawing, (hull[best][i][0][0], hull[best][i][0][1]), 10, (0, 0, 255), -1)

hull = [hull[best]]
num = len(hull[0])
newhull = []
hexagon = []

# for i in range(num):
#     j = (i + 1) % num
#     ji = [hull[0][j][0][0] - hull[0][i][0][0], hull[0][j][0][1] - hull[0][i][0][1]]
#     jmag = math.sqrt(ji[0]**2 + ji[1]**2)
#     # print(jmag)
#     if jmag > 40:
#         hexagon[0].append(hull[0][i])
# num = len(hexagon[0])

angles = []
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
    angles.append(ang)
    if math.fabs(math.pi - ang) > 0.1:
        newhull.append(hull[0][i][0])


for i in range(len(newhull)):
    j = (i + 1) % len(newhull)
    ji = [newhull[j][0] - newhull[i][0], newhull[j][1] - newhull[i][1]]
    jmag = math.sqrt(ji[0]**2 + ji[1]**2)
    if jmag > maxwidth/24:
        hexagon.append(newhull[i])

# for i in range(len(newhull)):
    # cv2.circle(drawing, (newhull[i][0], newhull[i][1]), 10, (0, 0, 255), -1)
# for i in range(len(hexagon[0])):
    # cv2.circle(drawing, (hexagon[0][i][0][0], hexagon[0][i][0][1]), 10, (0, 0, 255), -1)
for i in range(len(hexagon)):
    cv2.circle(drawing, (hexagon[i][0], hexagon[i][1]), 10, (0, 0, 255), -1)
    # j = (i + 1) % len(hexagon)
    # cv2.line(drawing, (hexagon[i][0], hexagon[i][1]), (hexagon[j][0], hexagon[j][1]), (255,255,0),5)
xsum = 0
ysum = 0
for i in range(len(hexagon)):
    xsum += hexagon[i][0]
    ysum += hexagon[i][1]
cv2.circle(drawing, (xsum//6, ysum//6), 10, (0, 0, 255), -1)
cv2.imwrite("contours.jpeg", drawing)

