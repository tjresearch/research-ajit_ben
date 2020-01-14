import cv2
import numpy as np
import math

src = cv2.imread("cubeblack.jpeg")  # read input image
'''gray_img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
img_contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contours = sorted(img_contours, key=cv2.contourArea)
cv2.drawContours(src, img_contours, -1, (0, 255, 0), 3)
cv2.imshow("Image with background removed", src)
cv2.waitKey(0)
for i in img_contours:
    if cv2.contourArea(i) > 1000000:
        break
mask = np.zeros(src.shape[:2], np.uint8)
cv2.drawContours(mask, [i],-1, 255, -1)
new_img = cv2.bitwise_and(src, src, mask=mask)
cv2.imshow("Original Image", src)
cv2.imshow("Image with background removed", new_img)
cv2.waitKey(0)'''
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
hsl = cv2.cvtColor(src, cv2.COLOR_BGR2HLS) # equal to HSL
luv = cv2.cvtColor(src, cv2.COLOR_BGR2LUV)
red = src[:, :, 2]
green = src[:, :, 1]
blue = src[:, :, 0]
_, red_bw = cv2.threshold(red, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
_, green_bw = cv2.threshold(green, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
_, blue_bw = cv2.threshold(blue, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
centers = []
# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
# Change thresholds
params.minThreshold = 0
params.maxThreshold = 200
params.filterByArea = True
params.minArea = 10
params.maxArea = 10000
# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1
# params.maxCircularity = 0.79
params.filterByConvexity = True
params.minConvexity = 0.1
params.maxConvexity = 1
params.filterByInertia = False
params.maxInertiaRatio = .5
params.minInertiaRatio = 0
params.filterByColor = False
detector = cv2.SimpleBlobDetector_create(params)
# detector = cv2.SimpleBlobDetector()
keypoints = detector.detect(red_bw)
for keypoint in keypoints:
    centers.append(keypoint)
    # cv2.circle(src, (round(keypoint.pt[0]), round(keypoint.pt[1])), 3, (0, 0, 255), -1)
# print(keypoints)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

# im_with_keypoints = cv2.drawKeypoints(red_bw, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
# cv2.imshow("Keypoints", im_with_keypoints)
# cv2.waitKey(0)
keypoints = detector.detect(green_bw)
for keypoint in keypoints:
    centers.append(keypoint)
    # cv2.circle(src, (round(keypoint.pt[0]), round(keypoint.pt[1])), 3, (0, 0, 255), -1)
# print(keypoints)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

# im_with_keypoints = cv2.drawKeypoints(green_bw, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
# cv2.imshow("Keypoints", im_with_keypoints)
# cv2.waitKey(0)
keypoints = detector.detect(blue_bw)
# print(keypoints)
for keypoint in keypoints:
    centers.append(keypoint)
    # cv2.circle(src, (round(keypoint.pt[0]), round(keypoint.pt[1])), 3, (0, 0, 255), -1)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

# im_with_keypoints = cv2.drawKeypoints(blue_bw, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

for center1 in centers:
    for center2 in centers:
        if center1 != center2:
            if (center1.pt[0] - center2.pt[0]) ** 2 + (center2.pt[1] - center1.pt[1]) ** 2 < 5:
                centers.remove(center2)
print(len(centers))
# for center in centers:
# cv2.circle(src, (round(center.pt[0]), round(center.pt[1])), 3, (0, 0, 0), -1)
# Show blobs


def checkpoint(x, y):
    for center in centers:
        if (center.pt[0] - x) ** 2 + (y - center.pt[1]) ** 2 < 200:
            return center
    return None


def checktriple(center1, center2, center3):
    a1 = center2.pt[0]-center1.pt[0]
    a2 = center2.pt[1]-center1.pt[1]
    b1 = center3.pt[0]-center1.pt[0]
    b2 = center3.pt[1]-center1.pt[1]
    face = []
    for i in range(3):
        for j in range(3):
            thing = checkpoint(center1.pt[0] + a1*i + b1*j, center1.pt[1] + a2*i + b2*j)
            face.append(thing)
            if thing is None:
                return None
    return face


def findface():
    for center1 in centers:
        for center2 in centers:
            for center3 in centers:
                if center1 != center2 != center3 and center1 != center3:
                    face = checktriple(center1, center2, center3)
                    if face is not None:
                        for center in face:
                            centers.remove(center)
                        return face
    return None


faces = []
for i in range(3):
    faces.append(findface())
# faces.append(centers)
print(len(faces))
facecenter = []
cube = []
for face in faces:
    facecenter.append(face[4])
for face in faces:
    mindist = 1000
    for i in range(9):
        dist = 0
        for things in facecenter:
            if things != face[4]:
                dist += math.sqrt((face[i].pt[0] - things.pt[0]) ** 2 + (face[i].pt[1] - things.pt[1]) ** 2)
        if dist < mindist:
            mindist = dist
            minindex = i
    if minindex == 2:
        for i in range(3):
            temp = face[3*i]
            face[3*i] = face[3*i+2]
            face[3*i+2] = temp
    if minindex == 6:
        for i in range(3):
            temp = face[i]
            face[i] = face[i+6]
            face[i+6] = temp
    if minindex == 8:
        for i in range(4):
            temp = face[i]
            face[i] = face[8-i]
            face[8-i] = temp
    # cv2.circle(src, (round(face[minindex].pt[0]), round(face[minindex].pt[1])), 3, (128, 0, 128), -1)
    # cv2.circle(src, (round(face[0].pt[0]), round(face[0].pt[1])), 3, (128, 0, 128), -1)
cube = []
for face in faces:
    temp = []
    for center in face:
        r = red_bw[round(center.pt[1])][round(center.pt[0])]
        b = blue_bw[round(center.pt[1])][round(center.pt[0])]
        g = green_bw[round(center.pt[1])][round(center.pt[0])]
        if b == 0 and g == 0:
            temp.append(4)
        elif b == 0:
            temp.append(2)
        elif g == 0 and r == 255:
            temp.append(0)
        elif g == 255 and r == 0:
            temp.append(1)
        else:
            g = src[round(center.pt[1])][round(center.pt[0])][1]
            r = src[round(center.pt[1])][round(center.pt[0])][2]
            # cv2.circle(src, (round(center.pt[0]), round(center.pt[1])), 3, (128, 0, 128), -1)
            if g / r < 0.8:
                temp.append(3)
            else:
                temp.append(5)
        cv2.circle(src, (round(center.pt[0]), round(center.pt[1])), 3, (0, 0, 0), -1)
        '''hue = hsv[center.pt[1]][center.pt[0]]
        if 0.01 <= hue <= 0.08:
            temp.append(03)
        elif 0.1 <= hue <= 0.28:
            temp.append(5)
        elif 0.32 <= hue <= 0.49:
            temp.append(0)
        elif 0.56 <= hue <= 0.68:
            temp.append(2)
        elif '''
    cube.append(temp)
    # cv2.circle(src, (round(face[0].pt[0]), round(face[0].pt[1])), 3, (128, 0, 128), -1)
print(cube)
# cv2.imshow("Keypoints", im_with_keypoints)
# cv2.waitKey(0)
# cv2.imshow("cube", src)
# cv2.waitKey(0)
cv2.imwrite("cubewithcenters.jpg", src)


