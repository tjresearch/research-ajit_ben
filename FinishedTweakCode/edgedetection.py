import cv2
import numpy as np

image = cv2.imread('actualCube.jpeg', 0)

image1 = np.zeros(image.shape)
for i in range(len(image)):
    for j in range(len(image[0])):
        if image[i][j] > 45:
            image1[i][j] = 0
        else:
            image1[i][j] = 255 - image[i][j]

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Using the Canny filter to get contours
edges = cv2.Canny(gray, 60, 120)
# Using the Canny filter with different parameters
edges_high_thresh = cv2.Canny(gray, 60, 120)
# Stacking the images to print them together
# For comparison
images = np.hstack((gray, edges, edges_high_thresh))
contours2, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1:]
candidates = []
good_contour = []
index = 0
for c in contours2:
    # approxPolyDP to find strainght line contours
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.06 * peri, True)
    # find countours made up for 4 lines
    if len(approx) == 6:
        (x, y, w, h) = cv2.boundingRect(approx)
        # find aspect ratio of boundary rectangle around the countours
        ar = w / float(h)
        # get the area of ther countour
        area = cv2.contourArea(contours2[index])
        # if the countour has AR close to 1 i.e close to square not rectangle and area of countour is
        # close to area of box around countouour i.e not diamonmd or robus add it to candidates list
        # print(x, y, w, h)
        if w > 120: # w == 122 and h == 53:
            good_contour.append(c)
            print(w)
    index += 1
cv2.drawContours(edges, good_contour, -1, (255, 255, 0), 3)
cv2.imwrite('countours.jpeg', edges)
cv2.drawContours(edges,contours2, -1, (255, 255, 255), 3)
image2 = np.zeros(image.shape)
for i in range(len(image)):
    for j in range(len(image[0])):
        image2[i][j] = min(image1[i][j]+edges[i][j], 255)
cv2.imwrite('contours.jpeg', image2)

# Display the resulting frame
cv2.imwrite('edges.jpeg', edges)
cv2.imwrite('edges.jpeg', edges_high_thresh)
